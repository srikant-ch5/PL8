//load http module
var http = require("http");

//Create HTTP server and listen on port 8000 for requests
http.createserver(function(request,respomse){
  //set response http header with HTTP status and content type
  response.writeHead(200,{'Cotent-Type':'text/plain'});
  response.end("Hello World\n");

}).listen(8000);

console.log("Server running at http ://127.0.0.1.8000/")
