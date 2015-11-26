var net = require('net');

var PORT = "3000";
var clients = [];

//Create server, and have it listen for connection on PORT
var server = net.createServer();
server.listen(PORT);
console.log("Listening for connections...")

//Connection event handler
server.on("connection", function(sock) {
    console.log("Received connection from " + sock.address().address);
    //Push client
    clients.push(sock);
    //Handle packets received from client
    sock.on("data", function(buff) {
        var message = buff.toString("utf8");
        clients.forEach(function(csock) {
            csock.write(message);
        })
    })
    //Handle socket closing
    sock.on("close", function() {
        clients.splice(clients.indexOf(sock));
    })
})

//Error event handler
server.on("error", function(err) {
    console.log(err);
})

