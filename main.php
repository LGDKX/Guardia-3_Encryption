<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Vote for your next president</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            margin: 0;
            padding: 0;
            text-align: center;
        }
        .container {
            margin: 20px auto;
            max-width: 600px;
        }
        .hidden {
            display: none;
        }
        button {
            padding: 10px 20px;
            margin: 10px;
            cursor: pointer;
        }
        .status {
            margin: 10px;
            font-weight: bold;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>Vote for your next president</h1>
        <div id="status" class="status"></div>
        
        <!-- Registration/Login -->
        <div id="auth-section">
            <input type="text" id="name" placeholder="Enter name" required>
            <input type="text" id="lastname" placeholder="Enter last name" required>
            <input type="password" id="password" placeholder="Enter Password" required>
            <button id="register-btn">Register</button>
            <button id="login-btn">Login</button>
        </div>

        <!-- Voting Section -->
        <div id="vote-section" class="hidden">
            <p>What is your opinion?</p>
            <button class="vote-btn" data-vote="Trump">Trump</button>
            <button class="vote-btn" data-vote="Harris">Harris</button>
        </div>

        <!-- Logout -->
        <div id="logout-section" class="hidden">
            <button id="logout-btn">Logout</button>
        </div>
    </div>

    <script>
        // User state
        let user = {
            loggedIn: false,
            username: null,
            hasVoted: false,
            vote: null,
        };

        const statusEl = document.getElementById("status");
        const authSection = document.getElementById("auth-section");
        const voteSection = document.getElementById("vote-section");
        const logoutSection = document.getElementById("logout-section");

        // Helper to update UI
        function updateUI() {
            if (user.loggedIn) {
                statusEl.textContent = `Welcome, ${user.username}`;
                authSection.classList.add("hidden");
                logoutSection.classList.remove("hidden");

                if (user.hasVoted) {
                    voteSection.classList.add("hidden");
                } else {
                    voteSection.classList.remove("hidden");
                }
            } else {
                statusEl.textContent = "Please register or log in to vote.";
                authSection.classList.remove("hidden");
                voteSection.classList.add("hidden");
                logoutSection.classList.add("hidden");
            }
        }

        // Register User
        document.getElementById("register-btn").addEventListener("click", () => {
            const name = document.getElementById("name").value.trim();
            const lastname = document.getElementById("lastname").value.trim();
            const password = document.getElementById("password").value.trim();

            const formData = new FormData();
            formData.append('name', name);
            formData.append('lastname', lastname);
            formData.append('password', password);
            formData.append('register', true);

            fetch('register', {
                method: 'POST',
                body: formData
            })
            .then(response => response.text())
            .then(data => {
                alert(data); // Show registration success/error
                if (data.includes("successful")) {
                    user = { loggedIn: true, username: name, hasVoted: false, vote: null };
                    updateUI();
                }
            });
        });

        // Login User
        document.getElementById("login-btn").addEventListener("click", () => {
            const name = document.getElementById("name").value.trim();
            const password = document.getElementById("password").value.trim();

            const formData = new FormData();
            formData.append('name', name);
            formData.append('password', password);
            formData.append('login', true);

            fetch('login', {
                method: 'POST',
                body: formData
            })
            .then(response => response.text())
            .then(data => {
                alert(data); // Show login success/error
                if (data.includes("successful")) {
                    user = { loggedIn: true, username: name, hasVoted: false, vote: null };
                    updateUI();
                }
            });
        });

        // Voting
        document.querySelectorAll(".vote-btn").forEach((btn) => {
            btn.addEventListener("click", (e) => {
                const vote = e.target.dataset .vote;
                const username = user.username; // Get the username from the user state
                user.hasVoted = true;
                user.vote = vote;

                const formData = new FormData();
                formData.append('vote', vote);
                formData.append('username', username); // Include username in the vote request

                fetch('vote', {
                    method: 'POST',
                    body: formData
                })
                .then(response => response.text())
                .then(data => {
                    alert(data); // Show vote success/error
                    updateUI();
                });
            });
        });

        // Logout
        document.getElementById("logout-btn").addEventListener("click", () => {
            user = { loggedIn: false, username: null, hasVoted: false, vote: null };
            updateUI();
        });

        // Initialize UI
        updateUI();
    </script>
</body>
</html>