
const express = require('express');
const app = express();

app.get('/', (req, res) => {
  res.send(`
    <html>
      <head>
        <title>Agentic DevOps Demo</title>
        <style>
          body {
            background-color: #0f172a;
            color: #38bdf8;
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
            text-align: center;
          }
          .message {
            font-size: 2rem;
            max-width: 700px;
            line-height: 1.5;
          }
        </style>
      </head>
      <body>
        <div class="message">
          ⚙️ Welcome to the <strong>Agentic DevOps</strong> Demo Platform<br>
          🤖 Powered by <strong>AI Agents</strong> for Smart Triage and Auto-Remediation
        </div>
      </body>
    </html>
  `);
});

const PORT = process.env.PORT || 8080;
app.listen(PORT, () => {
  console.log(`Server running on port ${PORT}`);
});

