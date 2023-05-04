#!/usr/bin/node
// script that computes the number of tasks completed by user id.

const request = require('request');
const url = process.argv[2];

request(url, (err, res, data) => {
  if (err) {
    console.log(err);
  } else {
    const todos = JSON.parse(data);
    const completedTask = {};

    todos.forEach((todo) => {
      if (todo.completed) {
        if (completedTask[todo.userId]) {
          completedTask[todo.userId]++;
        } else {
          completedTask[todo.userId] = 1;
        }
      }
    });
    console.log(completedTask);
  }
});
