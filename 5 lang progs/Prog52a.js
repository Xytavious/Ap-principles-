const prompt = require('prompt-sync')();

var len = Number(prompt(" what is the length"));
var wid = Number(prompt(" what is the width"));
var a = len * wid ;
var perim =  (2* len) + (2* wid);
console.log("the area is " + a);
console.log("the perim is " + perim);
/*
what is the length2
 what is the width2
the area is 4
the perim is 8
*/
