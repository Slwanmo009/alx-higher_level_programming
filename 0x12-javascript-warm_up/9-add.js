#!/usr/bin/node

// Function to add two integers
function add(a, b) {
  return a + b;
}

// Get the first and second arguments passed to the script
const arg1 = process.argv[2];
const arg2 = process.argv[3];

// Convert arguments to integers
const num1 = parseInt(arg1);
const num2 = parseInt(arg2);

// Check if both arguments are valid integers
if (!isNaN(num1) && !isNaN(num2)) {
  // Calculate the sum using the add function
  const sum = add(num1, num2);
  console.log(sum);
} else {
  console.log('Arguments are not integers');
}
