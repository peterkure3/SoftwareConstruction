# Group Name: Agile Architects

**Names:** 

**KURE PETER**

**NIRINGIYE ALLAN SMITH**

**NYUMBE WILSON**

**MUTUA BRIAN**

# Code Review and Maintainability Challenge Documentation

## Findings:

### Inconsistent Naming Convention:

- Variables inconsistently named (`username`, `password`, `email` in `/register`, `user`, `pass` in `/login`).

### Lack of Comments:

- No comments explaining the logic behind authentication and registration.

### Minimal Error Handling:

- Error messages lack detail for troubleshooting (`"Invalid credentials"`, `"Password must be at least 8 characters long"`).

### Hardcoded Credentials:

- Credentials are hardcoded (`username === "admin" && password === "admin"`), posing a security risk.

### No Input Validation:

- Lack of input validation for username, password, and email fields.

### Magic Numbers:

- Magic numbers used (`8` in password length check).

### Mixed Business Logic:

- Business logic mixed with route handling (`Authentication logic` comment).

### Unclear Route and Middleware Handling:

- No clear indication of other routes or middleware.

## Priority:

1. **Hardcoded Credentials** - Security concern.
2. **Inconsistent Naming Convention** - Improves readability and maintainability.
3. **Minimal Error Handling** - Better user experience and troubleshooting.
4. **Input Validation** - Prevents invalid data entry.
5. **Lack of Comments** - Enhances code understanding.
6. **Magic Numbers** - Increases code readability and maintainability.
7. **Mixed Business Logic** - Separation of concerns.
8. **Unclear Route and Middleware Handling** - Clarity in code structure.

## Refactoring Plan:

### Changes Made:

1. **Hardcoded Credentials:**
   - Store credentials securely (e.g., environment variables).
2. **Inconsistent Naming Convention:**
   - Use consistent variable names (`username`, `password`, `email` throughout).
3. **Minimal Error Handling:**
   - Provide more informative error messages.
4. **Input Validation:**
   - Validate input fields (e.g., using middleware).
5. **Lack of Comments:**
   - Add comments explaining authentication and registration logic.
6. **Magic Numbers:**
   - Define constants for magic numbers (`MIN_PASSWORD_LENGTH`).
7. **Mixed Business Logic:**
   - Move authentication logic to separate functions.
8. **Unclear Route and Middleware Handling:**
   - Organize routes and middleware clearly.

## Before Refactoring:

```javascript
// Example code for microservice handling user authentication
const express = require('express');
const app = express();

app.use(express.json());

app.post('/login', (req, res) => {
    // Authentication logic
    const { username, password } = req.body;
    if (username === "admin" && password === "admin") {
        res.send("Login successful");
    } else {
        res.status(401).send("Invalid credentials");
    }
});

app.post('/register', (req, res) => {
    // Registration logic
    const { username, password, email } = req.body;
    if (password.length < 8) {
        res.status(400).send("Password must be at least 8 characters long");
    } else {
        res.send("User registered successfully");
    }
});

// Other routes and middleware...

app.listen(3000, () => {
    console.log("Server is running on port 3000");
});
```

# After Refactoring

```javascript
    // Example code for microservice handling user authentication
const express = require('express');
const app = express();
const { validateRegistration, authenticateUser } = require('./authMiddleware');

app.use(express.json());

app.post('/login', authenticateUser);

app.post('/register', validateRegistration);

// Other routes and middleware...

app.listen(3000, () => {
    console.log("Server is running on port 3000");
});
```

## Middleware

```javascript
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
```
