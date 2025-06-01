const express = require('express');
const app = express();

app.get('/', (req, res) => {
  res.send('Hello, Agentic AI World on Google Cloud!');
});

const PORT = process.env.PORT || 8080;
app.listen(PORT, () => {
  console.log(`Server running on port ${PORT}`);
});
