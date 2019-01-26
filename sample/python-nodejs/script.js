#!/usr/bin/node-v10.15.0-linux-x64/bin/node
let {PythonShell} = require('python-shell')
user = require("os").userInfo().username
let options = {
  mode: 'text',
  pythonPath: `/home/${user}/python/venv/bin/python3.7`,
  pythonOptions: ['-u'], // get print results in real-time
  scriptPath: __dirname + '/../python/',
  //args: ['value1', 'value2', 'value3']
};

PythonShell.run('script.py', options, function (err, results) {
  if (err) throw err;
  // results is an array consisting of messages collected during execution
  console.log('results: %j', results);
});
