var net = require('net');

var HOST = "127.0.0.1";
var PORT = "8801";
var clients = [];

//Create server, and have it listen for connection on PORT
var server = net.createServer();
server.listen(PORT, HOST);
console.log("Listening for connections...")

//Connection event handler
server.on("connection", function(sock) {
    console.log("Received connection from " + sock.address().address);
    //Push client
    clients.push(sock);
    //Handle packets received from client
    sock.on("data", function(buff) {
        console.log(buff.toString("utf8"));
        clients.forEach(function(csock) {
            if (!(sock === csock)) {
                csock.write(buff.toString("utf8"));
            }
        })
    })
})

//Error event handler
server.on("error", function(err) {
    console.log(err);
})

