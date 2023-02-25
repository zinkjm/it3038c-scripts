const readline = require('readline');

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
  prompt: `Enter any number:  `
});

// USE 1: asking a question
rl.question('What is your name? ', (name) => {
  console.log(`Hello, ${name}!`);


// USE 2: prompting any user input and do something depending what it is
rl.prompt();
rl.on(`line`, (line) => {
    if (isNaN(line)) {

        // Resetting what the prompt is
        rl.setPrompt(`That's not a number. Enter a number: `);
        rl.prompt();
    }

    else {
        console.log(`That's a good number, ${name}`);
        rl.close();
    }
    
})
});

// USE 3: when rl is closed, do a task
rl.on(`close`, () => {
    console.log(`Closing now`);
});

