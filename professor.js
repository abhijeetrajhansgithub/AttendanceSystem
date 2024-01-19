// professor.js

// Function to generate a random 9-digit code
function generateRandomCode() {
  return Math.floor(Math.random() * 900000000 + 100000000);
}

// Function to update the code display
function updateCodeDisplay() {
  var codeDisplay = document.getElementById('code-display');
  codeDisplay.textContent = generateRandomCode();
}

// Initial code display
updateCodeDisplay();

// Update code display every 15 seconds
setInterval(updateCodeDisplay, 15000);