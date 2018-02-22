setTimeout(function(){
    return "return value after 3 sec"
},3000); // 3000 is milliseconds

setInterval(function(){
    return "it is called after every 3 sec "
},3000); // function is called after every 3 sec

clearInterval(); // see documentation

console.log(__dirname); // gives the path of dir
console.log(__filename); // gives the path of our file

///////////////////////////////////////############################################
var counter = require("path to wanted js file"); // imports the wanted js file to our current working file

// wanted file/////

var counter1 = function(){
    return "fhjhj"
};

module.export = counter1; /// we have to give which function  to export to other file


/// if there are many functions to export

module.export.counter1 = counter1(); // here module.export is a object we are setting attributes to it

// to use in other file we write

var x = require("./filename.js");
var counter = x.counter1()

/////////////////////////////////###############################


////////// Event Module /////////

var event = require("events"); /// importing event module
var myEmitter = new event.EventEmitter();

myEmitter.on("someEvent", function(name){
    console.log(name);
});


myEmitter.emit("someEvent");

///////////////////////