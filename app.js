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


app.locals.daniColorCaja = {'arguments': ' 0.5 leftToRight rainbowCycle .001', 'currID':uuidv4()};
app.locals.edgarColorCaja = {'arguments': ' 0.5 leftToRight rainbowCycle .001', 'currID':uuidv4()};
app.locals.edToDani = {'isActive': false, 'currID': uuidv4()}
app.locals.edToDani = {'isActive': false, 'currID': uuidv4()}

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
  console.log(updateColor);
  if(typeOf (updateColor) == 'undefined')
    return;
  if(typeOf (updateColor.brightness) == 'undefined')
    return;
  if(typeOf (updateColor.funName) == 'undefined')
    return;
  if(typeOf (updateColor.sectionOrder) == 'undefined')
    return;
  arguments = brains.toCallAttributes(updateColor);
  app.locals.daniColorCaja = {'arguments':arguments,'currID':uuidv4()};
  console.log(app.locals.daniColorCaja);
});

app.get('/updateDaniBox', (request, response) => {
  response.json(app.locals.daniColorCaja);
});


app.post('/updateEdgarBox', (request, response) => {
  updateColor = request.body;
  if(typeOf (updateColor) == 'undefined')
    return;
  if(typeOf (updateColor['brightness']) == 'undefined')
    return;
  if(typeOf (updateColor['funName']) == 'undefined')
    return;
  arguments = brains.toCallAttributes(updateColor);
  app.locals.edgarColorCaja = {'arguments':arguments,'currID':uuidv4()};
  console.log(app.locals.edgarColorCaja);
});

app.get('/updateEdgarBox', (request, response) => {
  response.json(app.locals.edgarColorCaja);
});


app.get('/daniToEd', (request, response) => {
  app.locals.edToDani.isActive = true;
  app.locals.edToDani.currID = uuidv4();
  response.json(app.locals.edToDani);
  client.messages.create({
    body: 'Poke!',
    to: '+525514377997',
    from: '+17149422514'
  }).then((message) => console.log(message));
});

app.get('/daniToEdContact', (request, response) => {
  response.json(app.locals.edToDani)
});

app.get('/edAcknowledge', (request, response) => {
  app.locals.edToDani.isActive = false;
  response.json(app.locals.edToDani);
});

app.get('/edToDani', (request, response) => {
  app.locals.edToDani.isActive = true;
  app.locals.edToDani.currID = uuidv4();
  response.json(app.locals.edToDani);
  console.log(app.locals.edToDani);
});

app.get('/edToDaniContact', (request, response) => {
  response.json(app.locals.edToDani)
});

app.get('/daniAcknowledge', (request, response) => {
  app.locals.edToDani.isActive = false;
  response.json(app.locals.edToDani);
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
