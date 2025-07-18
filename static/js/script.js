document.getElementById('bmiForm').addEventListener('submit', function(event) {
    const height = parseFloat(document.getElementById('height').value);
    const weight = parseFloat(document.getElementById('weight').value);

    if (isNaN(height) || height <= 0 || height > 300) {
        event.preventDefault();
        alert('Please enter a valid height (0-300 cm).');
        return;
    }

    if (isNaN(weight) || weight <= 0 || weight > 500) {
        event.preventDefault();
        alert('Please enter a valid weight (0-500 kg).');
        return;
    }
});
