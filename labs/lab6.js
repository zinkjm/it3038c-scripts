const http = require("http");
const fs = require("fs");
const os = require("os");
const ip = require('ip');

http.createServer((req, res) => {
  if (req.url === "/") {
      fs.readFile("./public/index.html", "UTF-8", (err, body) => {
       
        res.writeHead(200, {"Content-Type": "text/html"});
      res.end(body);
      
    });
  } else if(req.url.match("/sysinfo")) {
    days = (60 * 60 * 24);
    hours = (60 * 60);
    minutes = 60;
    serverTime = os.uptime();
    serverDays = parseInt(serverTime / days);
    serverHours = parseInt((serverTime % days)/(hours))
    serverMinutes = parseInt((serverTime % days % hours) / (60));
    serverSeconds = parseInt(serverTime % days % hours % minutes);
    totalServerTime = `Days: ${serverDays}, Hours: ${serverHours}, Minutes: ${serverMinutes} Seconds: ${serverSeconds}`
    myHostName=os.hostname();
    freeMemory = os.freemem() / 1000000;
    totalMemory = os.totalmem() / 1000000;
    cpuNumber = os.cpus().length
    html=`
    <!DOCTYPE html>
    <html>
      <head>
        <title>Node JS Response</title>
      </head>
      <body>
        <p>Hostname: ${myHostName}</p>
        <p>IP: ${ip.address()}</p>
        <p>Server Uptime: ${totalServerTime}</p>
        <p>Total Memory: ${totalMemory} MB</p>
        <p>Free Memory: ${freeMemory} MB</p>
        <p>Number of CPUs: ${cpuNumber}</p>
      </body>
    </html>`
    res.writeHead(200, {"Content-Type": "text/html"});
    res.end(html);
  } else {
    res.writeHead(404, {"Content-Type": "text/plain"});
    res.end(`404 File Not Found at ${req.url}`);
  }
}).listen(3000);

console.log("Server listening on port 3000");