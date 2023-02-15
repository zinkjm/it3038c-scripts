const path = require('path');
const hello = "Hello from Node JS Variable!";
console.log(hello);

console.log("Using PATH module:");
console.log(`Hello from file ${path.basename(__filename)}`);
console.log(`Process args: ${process.argv}`)
