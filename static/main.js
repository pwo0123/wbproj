let socket = new WebSocket('ws://localhost:8000/ws/graph/');
socket.onmessage = function(e){
    console.log(e.data);
}