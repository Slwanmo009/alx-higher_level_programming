#!/usr/bin/node

// Get the first argument passed to the script
const arg = process.argv[2];

// Convert the argument to an integer
const size = parseInt(arg);

// Check if the conversion was successful and print the appropriate output
if (!isNaN(size)) {
  for (let i = 0; i < size; i++) {
    console.log('X'.repeat(size));
  }
} else {
  console.log('Missing size');
}
