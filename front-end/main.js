var counterContainer = document.querySelector(".website-counter");



var apiUrl = "https://anan1.azurewebsites.net/api/HttpTrigger1?code=8NlbWxxBhYwIOQx65KywV_PmLAvc4HJiojR-ZyVl-bGvAzFuZkOCYA%3D%3D"; // Azure Function URL'si


var counterContainer = document.querySelector(".website-counter");


async function updateVisitorCount() {
  try {
    const response = await fetch(apiUrl);
    if (response.ok) {
      const count = await response.text();
      counterContainer.innerHTML = count;
    } else {
      console.error('Error updating visitor count.');
    }
  } catch (error) {
    console.error('Error:', error);
  }
}


updateVisitorCount();


