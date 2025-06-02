const express = require('express');
const app = express();
app.get('/', (req, res) => {
  
  // Intentional runtime failure error
  throw new Error("Intentional failure for triage test");
  res.send(`
    <html>
      <head>
        <title>Agentic DevOps Demo</title>
        <style>
          body {
            background-color: #0f172a;
            color: #f8fafc;
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            text-align: center;
            padding: 60px;
          }
          img {
            width: 300px;
            margin: 20px auto;
          }
          h1 {
            font-size: 2.5em;
            color: #38bdf8;
          }
          p {
            font-size: 1.2em;
            max-width: 600px;
            margin: 20px auto;
          }
        </style>
      </head>
      <body>
        <img src="<img src="https://i.imgur.com/NkVrRyk.png" alt="Agentic AI Logo">
        <h1>Agentic AI for DevOps</h1>
        <p>
          Welcome to the future of intelligent automation. This live demo showcases how Agentic AI can analyze, decide, and act — enabling self-healing DevOps pipelines powered by GitHub Actions, Node.js, and cloud-native design.
        </p>
      </body>
    </html>
  `);
});

const PORT = process.env.PORT || 8080;
app.listen(PORT, () => {
  console.log(`Server running on port ${PORT}`);
});
