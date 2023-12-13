<?php
$servername = "localhost";
$username = "root";
$password = "";
$dbname = "tdss";

// Create connection
$conn = new mysqli($servername, $username, $password, $dbname);
// Check connection
if ($conn->connect_error) {
  die("Connection failed: " . $conn->connect_error);
}

if($_POST){
$name=$_POST["name"];
$password=$_POST["psw"];
$email=$_POST["email"];

$sql = "INSERT INTO student (name, password,email)
VALUES ('$name','$password','$email')";

if ($conn->query($sql) === TRUE) {
  echo "New record created successfully";
} else {
  echo "Error: " . $sql . "<br>" . $conn->error;
}

$conn->close();
}
?>
<html>
<head></head>
<body> 
<form method="post">
  <div class="container">
    <center><h1>Register</h1>
    <p>Please fill in this form to create an account.</p>
	<label for="name"><b>Name</b></label>
    <input type="text" placeholder="Enter Name" name="name" id="name" required><br>

    <label for="email"><b>Email</b></label>
    <input type="text" placeholder="Enter Email" name="email" id="email" required><br>

    <label for="psw"><b>Password</b></label>
    <input type="password" placeholder="Enter Password" name="psw" id="psw" required><br>

    <label for="psw-repeat"><b>Repeat Password</b></label>
    <input type="password" placeholder="Repeat Password" name="psw-repeat" id="psw-repeat" required><br></center>
   
    <center><p>By creating an account you agree to our <a href="#">Terms & Privacy</a>.</p></center>
    <center><button type="submit" class="registerbtn">Submit</button></center>
  </div>

  <div class="container signin">
    <center><p>Already have an account? <a href="#">Sign in</a>.</p></center>
  </div>
</form>
</body>
</html> 
