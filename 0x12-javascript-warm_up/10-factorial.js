#!/usr/bin/node

// Recursive function to compute factorial
function computeFactorial(n) {
  if (isNaN(n)) {
    return 1; // Factorial of NaN is 1
  }
  // Base case: factorial of 0 is 1
  if (n === 0) {
    return 1;
  } else {
    // Recursive case: compute factorial
    return n * computeFactorial(n - 1);
  }
}

// Get the first argument passed to the script
const arg = process.argv[2];

// Convert the argument to an integer
const num = parseInt(arg);

// Compute factorial using the recursive function
const factorial = computeFactorial(num);

// Print the computed factorial
console.log(factorial);
