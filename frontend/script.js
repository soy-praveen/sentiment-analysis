document.getElementById("form").addEventListener("submit", async function(e) {
    e.preventDefault();
    
    const link = document.getElementById("ig-link").value;
    
    const response = await fetch("/analyze", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({ link: link })
    });
    
    const result = await response.json();
    document.getElementById("result").innerHTML = `<h2>Sentiment: ${result.sentiment}</h2>`;
});
