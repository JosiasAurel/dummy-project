
var nodemailer = require('nodemailer');

var transporter = nodemailer.createTransport({
  service: 'gmail', //mail provider
  auth: {
    user: '<yourname@example.com>',
    pass: 'password'
  }
});

var mailOptions = {
  from: '<yourname@example.com>',
  to: 'user@example.com',
  subject: 'Thanks for filling the form',
  html: `<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta http-equiv="X-UA-Compatible" content="IE=Edge">
  <meta name="viewport" content="width=device-width, initial-scale=1">

  <title>BiytCode</title>
  <style type="text/css" media="all">
    body {
    font-size: 15pt;
    font-family : monospace;
    margin: 0;
}

header, footer {
  display: flex;
  justify-content: center;
  background-color: #160240;
}

h2 {
  color: white;
}

div {
  border: solid;
  border-color: transparent;
}

h5 {
  margin-top: 200px;
  margin: 20px;
}
  </style>
  <!-- HTML -->
  

  <!-- Custom Styles -->
  <link rel="stylesheet" href="style.css">
</head>

<body>
  <header style="{
  display: flex;
  justify-content: center;
  background-color: #160240;
}">
    <h2><BrandName></h2>
  </header>
  
  <div>
    <h5>
      Hey <name>,
      Thanks for reaching out to me. Your responses will help design a platform that will suite your learning. please if you have any questions you can reply to this email. 
      
      
    </h5> 
    <h5>Best Regards</h5>
    <footer>
      <h2><BrandName></h2>
    </footer style="{
  display: flex;
  justify-content: center;
  background-color: #160240;
}">
  </div>
</body>
</html>`
};

transporter.sendMail(mailOptions, function(error, info){
  if (error) {
    console.log(error);
  } else {
    console.log('Email sent: ' + info.response);
  }
});
