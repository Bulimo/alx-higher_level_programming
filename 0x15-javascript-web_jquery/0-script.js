// Find the <header> element using document.querySelector
const headerElement = document.querySelector('header');

// Check if the element is found
if (headerElement) {
  // Update the text color to red (#FF0000)
  headerElement.style.color = '#FF0000';
} else {
  console.log('The <header> element was not found.');
}
