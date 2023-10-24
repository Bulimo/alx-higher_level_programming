#!/usr/bin/node
const request = require('request');
const apiUrl = process.argv[2];

request(apiUrl, (error, response, body) => {
  if (!error && response.statusCode === 200) {
    const tasks = JSON.parse(body);

    // Create an object to store the count of completed tasks per user
    const completedTaskCount = {};

    // Iterate through the tasks
    for (const task of tasks) {
      if (task.completed) {
        const userId = task.userId;
        if (!completedTaskCount[userId]) {
          completedTaskCount[userId] = 1;
        } else {
          completedTaskCount[userId]++;
        }
      }
    }

    // Print the number of completed tasks for each user
    console.log(completedTaskCount);
  } else {
    console.error('Error:', error || `HTTP Status Code: ${response.statusCode}`);
  }
});
