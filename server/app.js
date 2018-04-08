const port = process.env.PORT || 3000,
express = require('express'),
app = express(),
http = require('http').Server(app),
io = require('socket.io')(http),
path = require('path'),
bodyParser = require('body-parser');

app.use(bodyParser.json());
app.use(bodyParser.urlencoded({ extended: false }));
app.use(express.static(__dirname + '/public'));

io.on('connection', function (client) {
  console.log('connected');
});

app.get('/', (req, res) => {
  res.sendFile(path.join(__dirname + '/public/index.html'));
});

app.post('/api/direction', (req, res) => {
  io.emit('direction', req.body);
  console.log(req.body);
  res.sendStatus(200);
});

app.post('/api/spotlight', (req, res) => {
  io.emit('spotlight', {});
  res.sendStatus(200);
});

http.listen(port);
