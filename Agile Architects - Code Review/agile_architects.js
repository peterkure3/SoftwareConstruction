// Example code for microservice handling user authentication
const express = require('express');
const app = express();
const { validateRegistration, authenticateUser } = require('./authMiddleware');

app.use(express.json());

// Routes for loggin in and registering
app.post('/login', authenticateUser);

app.post('/register', validateRegistration);

// Other routes and middleware...

// Starts the server on a specified port i.e 3000
app.listen(3000, () => {
    console.log("Server is running on port 3000");
});
