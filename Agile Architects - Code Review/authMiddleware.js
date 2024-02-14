// authMiddleware.js

// Authentication logic
const User = require('./models/User');

async function authenticateUser(req, res) {
    const { username, password } = req.body;

    try {
        const user = await User.findOne({ username });

        if (!user) {
            res.status(401).send("Invalid credentials");
            return;
        }

        const isPasswordValid = await user.comparePassword(password);

        if (!isPasswordValid) {
            res.status(401).send("Invalid credentials");
            return;
        }

        res.send("Login successful");
    } catch (error) {
        console.error("Error authenticating user:", error);
        res.status(500).send("Internal server error");
    }
}

// Registration logic with input validation
function validateRegistration(req, res) {
    const { username, password, email } = req.body;
    if (!username || !password || !email) {
        res.status(400).send("All fields are required");
    } else if (password.length < 8) {
        res.status(400).send("Password must be at least 8 characters long");
    } else {
        res.send("User registered successfully");
    }
}

module.exports = { authenticateUser, validateRegistration };