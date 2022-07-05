function displayVisitorCount(data) {
  const visitors = data
  const visitorsDiv = document.getElementById("visitors");
  const heading = document.createElement("h4");
  heading.innerHTML = 'Total number of page visits: ' + visitors;
  visitorsDiv.appendChild(heading);
}   

fetch("https://cro240ve32.execute-api.us-east-1.amazonaws.com/Prod/get")
  .then((response) => {
    if (response.ok) {
      return response.json();
    } else {
      throw new Error("NETWORK RESPONSE ERROR");
    }
  })
  .then(data => {
    console.log(data);
	displayVisitorCount(data['count']);
  })
  .catch((error) => console.error("GET ERROR:", error));
  
let empty_json = {};

fetch("https://cro240ve32.execute-api.us-east-1.amazonaws.com/Prod/put")
  .then((response) => {
    if (response.ok) {
      return response.json();
    } else {
      throw new Error("NETWORK RESPONSE ERROR");
    }
  })
  .then(data => {
    console.log(data);
  })
  .catch((error) => console.error("PUT ERROR:", error));