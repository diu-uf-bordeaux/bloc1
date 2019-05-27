const PORT = 80;
const express = require('express');
const app = express();

app.use(express.static('public'));

app.get('/',function() {
    
})



app.listen(PORT, function () {
    console.log(`Server is running on port ${PORT}!`)
})
  