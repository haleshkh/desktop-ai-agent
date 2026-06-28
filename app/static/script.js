async function sendCommand() {

    const query = document.getElementById("query").value;

    const result = document.getElementById("result");

    result.innerHTML = "Processing...";

    const response = await fetch("/chat", {

        method: "POST",

        headers: {
            "Content-Type": "application/json"
        },

        body: JSON.stringify({
            query: query
        })

    });

    const data = await response.json();

    result.innerHTML = data.response;

}