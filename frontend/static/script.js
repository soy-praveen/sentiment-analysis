document.getElementById('analyze-form').addEventListener('submit', function(event) {
    event.preventDefault(); // Prevents the default form submission behavior

    const url = document.getElementById('url').value;

    fetch('/analyze', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/x-www-form-urlencoded',
        },
        body: new URLSearchParams({ url: url })
    })
    .then(response => response.json())
    .then(data => {
        // Display the result in the result div
        document.getElementById('result').textContent = JSON.stringify(data);
    })
    .catch(error => {
        console.error('Error:', error);
    });
});
