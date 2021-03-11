var createError = require('http-errors');
var express = require('express');
var path = require('path');
var brains = require('./functions/brains');
const {v4:uuidv4} = require('uuid');

var indexRouter = require('./routes/index');
var usersRouter = require('./routes/users');

var app = express();

var accountSid = 'AC4409213628875dbd54038e77c9691740';
var authToken = 'fab725efb3d1baffe7453955c17e4d66';

var twilio = require('twilio');
var client = new twilio(accountSid, authToken);

var daniColorCaja = {'arguments': ' 0.5 leftToRight rainbowCycle .001', 'currID':uuidv4()};
var edgarColorCaja = {'arguments': ' 0.5 leftToRight rainbowCycle .001', 'currID':uuidv4()};
var edToDani = {'isActive': false, 'currID': uuidv4()}
var daniToEd = {'isActive': false, 'currID': uuidv4()}

app.set('views', path.join(__dirname, 'views'));
app.set('view engine', 'jade');

app.use(express.json());
app.use(express.urlencoded({ extended: false }));
app.use(express.static(path.join(__dirname, 'public')));

/*
      START OF BOX LOGIC
*/


app.post('/updateDaniBox', (request, response) => {
  updateColor = request.body;
  arguments = brains.toCallAttributes(updateColor);
  daniColorCaja = {'arguments':arguments,'currID':uuidv4()};
  console.log(daniColorCaja);
});

app.get('/updateDaniBox', (request, response) => {
  response.json(daniColorCaja);
});


app.post('/updateEdgarBox', (request, response) => {
  updateColor = request.body;
  arguments = brains.toCallAttributes(updateColor);
  edgarColorCaja = {'arguments':arguments,'currID':uuidv4()};
  console.log(edgarColorCaja);
});

app.get('/updateEdgarBox', (request, response) => {
  response.json(edgarColorCaja);
});


app.get('/daniToEd', (request, response) => {
  daniToEd.isActive = true;
  daniToEd.currID = uuidv4();
  response.json(daniToEd);
  client.messages.create({
    body: 'Poke!',
    to: '+525514377997',
    from: '+17149422514'
  }).then((message) => console.log(message));
});

app.get('/daniToEdContact', (request, response) => {
  response.json(daniToEd)
});

app.get('/edAcknowledge', (request, response) => {
  daniToEd.isActive = false;
  response.json(daniToEd);
});

app.get('/edToDani', (request, response) => {
  edToDani.isActive = true;
  edToDani.currID = uuidv4();
  response.json(edToDani);
  console.log(edToDani);
});

app.get('/edToDaniContact', (request, response) => {
  response.json(edToDani)
});

app.get('/daniAcknowledge', (request, response) => {
  edToDani.isActive = false;
  response.json(edToDani);
});

/*
      END OF BOX LOGIC
*/

app.use('/', indexRouter);
app.use('/users', usersRouter);

app.use(function(req, res, next) {
  next(createError(404));
});

app.use(function(err, req, res, next) {
  res.locals.message = err.message;
  res.locals.error = {};

  res.status(err.status || 500);
  res.render('error');
});

// app.listen(80, ()=>{
//   console.log("started");
// })

module.exports = app;
