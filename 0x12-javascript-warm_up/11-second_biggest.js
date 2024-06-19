#!/usr/bin/node

// Function to find the second biggest integer
function secondBiggest(arr) {
  if (arr.length < 2) {
    return 0;
  }

  let first = Number.MIN_SAFE_INTEGER;
  let second = Number.MIN_SAFE_INTEGER;

  for (let i = 0; i < arr.length; i++) {
    if (arr[i] > first) {
      second = first;
      first = arr[i];
    } else if (arr[i] > second && arr[i] !== first) {
      second = arr[i];
    }
  }

  return second;
}

// Get command-line arguments excluding the first two elements (which are 'node' and the script path)
const args = process.argv.slice(2);

// Convert arguments to integers
const numbers = args.map(Number);

// Find the second biggest integer
const result = secondBiggest(numbers);

// Print the result
console.log(result);
