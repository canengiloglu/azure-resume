import azure.functions as func
import logging
from azure.keyvault.secrets import SecretClient
from azure.identity import DefaultAzureCredential
from azure.cosmos import CosmosClient, PartitionKey

KEY_VAULT_URL = "https://mysecurekeyvault13.vault.azure.net/"


# Azure Function uygulaması
app = func.FunctionApp(http_auth_level=func.AuthLevel.FUNCTION)

@app.route(route="HttpTrigger1")
def HttpTrigger1(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    try:
        # Cosmos DB istemcisi oluştur
        client = CosmosClient(COSMOSDBURL, credential=COSMOSDBKEY)

        # Veritabanı ve container'ı seç
        database = client.get_database_client(DATABASENAME)
        container = database.get_container_client(CONTAINERNAME)

        # Öğeyi oku
        item_id = "1"  # Ziyaretçi sayaç öğesinin id'si
        item = container.read_item(item=item_id, partition_key=item_id)
        logging.info(f"Current item: {item}")

        # Ziyaretçi sayısını artır
        count = int(item.get("count", 0))  # Mevcut sayıyı al
        count += 1
        item["count"] = count  # Güncellenmiş sayıyı yaz

        # Öğeyi güncelle
        container.upsert_item(item)

        # Yanıt olarak güncellenmiş sayıyı döndür
        return func.HttpResponse(
            body=f"Visitor count updated: {count}",
            status_code=200
        )

    except Exception as e:
        logging.error(f"Error: {str(e)}")
        return func.HttpResponse(
            body=f"Error occurred: {str(e)}",
            status_code=500
        )
