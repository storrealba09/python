#!/usr/bin/node-v10.15.0-linux-x64/bin/node
//import {PythonShell} from 'python-shell';
let {PythonShell} = require('python-shell')
let options = {
  mode: 'text',
  pythonPath: '/usr/local/bin/python3.7',
  pythonOptions: ['-u'], // get print results in real-time
  scriptPath: '/home/sysadmin/',
  //args: ['value1', 'value2', 'value3']
};

PythonShell.run('script.py', options, function (err, results) {
  if (err) throw err;
  // results is an array consisting of messages collected during execution
  console.log('results: %j', results);
});
