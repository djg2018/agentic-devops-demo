const express = require('express');
const app = express();

app.get('/', (req, res) => {
  res.send('Hello, Agentic AI World on Google Cloud!');
  res.send('If you are seeing this message, then the deployment is successful');
});

const PORT = process.env.PORT || 8080;
app.listen(PORT, () => {
  console.log(`Server running on port ${PORT}`);
});
// trigger redeploy
