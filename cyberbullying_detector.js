// Define a list of cyberbullying keywords and phrases
const keywords = ["loser", "ugly", "stupid", "fat", "worthless", "dumb", "hate you", "kill yourself","nigga","fucking more on","suicide","short boy","short girl"]

// Define a function to detect cyberbullying
function detectCyberbullying(text) {
  // Convert text to lowercase to ignore case
  text = text.toLowerCase();
  
  // Loop through keywords and phrases to check if they appear in the text
  for (let i = 0; i < keywords.length; i++) {
    if (text.includes(keywords[i])) {
      // If a keyword is found, return true
      return true;
    }
  }
  
  // If no keywords are found, return false
  return false;
}

// Define a function to handle form submission
function handleSubmit(event) {
  event.preventDefault();
  const text = document.querySelector('textarea[name="text"]').value;
  const isCyberbullying = detectCyberbullying(text);
  const resultElement = document.getElementById('results');
  if (isCyberbullying) {
    //resultElement.textContent = "This text contains cyberbullying.";
    alert("This text contains cyberbullying.")
  } else {
    //resultElement.textContent = "This text does not contain cyberbullying.";
    alert("This text does not contain cyberbullying.")
  }
}

// Add a submit event listener to the form
const form = document.querySelector('form');
form.addEventListener('submit', handleSubmit);
