<?php
// Connect to the database
$conn = new mysqli("localhost", "root", "", "vulnerable_db");

// Check connection
if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
}

// Create database if it doesn't exist
$dbCreationQuery = "CREATE DATABASE IF NOT EXISTS `vulnerable_db`";
if ($conn->query($dbCreationQuery) === TRUE) {
    echo "<script>console.log('Database created or already exists');</script>";
} else {
    die("Database creation failed: " . $conn->error);
}

// Switch to the newly created database
$conn->select_db("vulnerable_db");

// Create `users` table
$usersTableQuery = "CREATE TABLE IF NOT EXISTS `users` (
    `name` VARCHAR(40),
    `lastname` VARCHAR(40),
    `password` VARCHAR(40)
)";
if ($conn->query($usersTableQuery) === TRUE) {
    echo "<script>console.log('Table `users` created or already exists');</script>";
} else {
    die("Table creation failed: " . $conn->error);
}

// Create `votes` table
$votesTableQuery = "CREATE TABLE IF NOT EXISTS `votes` (
    `username` VARCHAR(40),
    `vote` VARCHAR(6)
)";
if ($conn->query($votesTableQuery) === TRUE) {
    echo "<script>console.log('Table `votes` created or already exists');</script>";
} else {
    die("Table creation failed: " . $conn->error);
}

if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    // Registration
    if (isset($_POST['register'])) {
        $name = $_POST['name'];
        $lastname = $_POST['lastname'];
        $password = md5($_POST['password']); // Weak hashing (MD5)

        $query = "INSERT INTO users (name, lastname, password) VALUES ('$name', '$lastname', '$password')";
        $conn->query($query);
        echo "<script>alert('Registration successful');</script>";
    }

    // Login
    if (isset($_POST['login'])) {
        $name = $_POST['name'];
        $password = md5($_POST['password']); // Weak hashing (MD5)

        $query = "SELECT * FROM users WHERE name = '$name' AND password = '$password'"; // SQL Injection vulnerability
        $result = $conn->query($query);

        if ($result->num_rows > 0) {
            echo "<script>alert('Login successful');</script>";
            $loggedInUser = $name;
        } else {
            echo "<script>alert('Login failed');</script>";
        }
    }

    // Voting
    if (isset($_POST['vote'])) {
        $username = $_POST['username'];
        $vote = $_POST['vote']; // No validation, prone to XSS

        $query = "INSERT INTO votes (username, vote) VALUES ('$username', '$vote')"; // No CSRF protection
        $conn->query($query);
        echo "<script>alert('Vote submitted for $vote');</script>";
    }
}
?>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Vulnerable One-Pager</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            text-align: center;
        }
        input, button {
            margin: 10px;
        }
    </style>
</head>
<body>
    <h1>Vote for Your Next President</h1>
    <div id="status"></div>

    <!-- Registration/Login -->
    <form method="POST">
        <input type="text" name="name" placeholder="Enter Name" required>
        <input type="text" name="lastname" placeholder="Enter Last Name">
        <input type="password" name="password" placeholder="Enter Password" required>
        <button type="submit" name="register">Register</button>
        <button type="submit" name="login">Login</button>
    </form>

    <!-- Voting -->
    <form method="POST">
        <input type="hidden" name="username" value="<?php echo isset($loggedInUser) ? $loggedInUser : ''; ?>">
        <p>Vote for:</p>
        <button type="submit" name="vote" value="Trump">Trump</button>
        <button type="submit" name="vote" value="Harris">Harris</button>
    </form>
</body>
</html>
