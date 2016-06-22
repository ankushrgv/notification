var http = require('http');
var server = http.createServer().listen(8002);
var io = require('socket.io').listen(server);
var cookie_reader = require('cookie');
var querystring = require('querystring');
var redis = require('socket.io/node_modules/redis');

//Configure socket.io to store cookie set by Django
io.configure(function(){
    io.set('authorization', function(data, accept){
        if(data.headers.cookie){
            data.cookie = cookie_reader.parse(data.headers.cookie);
            return accept(null, true);
        }
        return accept('error', false);
    });
    io.set('log level', 1);
});

io.sockets.on('connection', function (socket) {

    console.log("Incoming connection");
    // Create redis client
    client = redis.createClient();

    // Subscribe to the Redis events channel
    client.subscribe('notifications.5');

    // Grab message from Redis and send to client
    client.on('message', function(channel, message){
        console.log('on message', message);
        socket.send(message);
    });

    // Unsubscribe after a disconnect event
    socket.on('disconnect', function () {
        client.unsubscribe('notifications.' + socket.handshake.cookie['sessionid']);
    });
});
