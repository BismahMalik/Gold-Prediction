document.getElementById('predictionForm').addEventListener('submit', function(event) {
    event.preventDefault();
    const inputFeatures = document.getElementById('inputFeatures').value;
    // Convert input features to an array if needed
    const featuresArray = inputFeatures.split(',').map(Number);

    // Send POST request to Flask backend
    fetch('/predict', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ input_features: featuresArray })
    })
    .then(response => response.json())
    .then(data => {
        // Display the predicted value
        document.getElementById('predictionResult').innerHTML = `Gold Rate: ${data.prediction}`;
    })
    .catch(error => {
        console.error('Error:', error);
    });
});