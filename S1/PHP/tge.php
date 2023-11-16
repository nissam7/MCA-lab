<!DOCTYPE html>
<html lang="en">
<head>
	<meta charset="UTF-8">
	<meta name="viewport" content="width=device-width,intial-scale=1.0">
	<title>Database Data</title>
	<style>
	 table{
		width:50%;
		border-collapse:collapse;
		margin:20px 0;
	}
table,th,td{
	padding:10px;
	text-align:left;
	}
	</style>
</head>
<body>

<?php

$servername="localhost";
$username="root";
$password="";
$database="nissam";

$conn=new mysqli($servername,$username,$password,$database);
if($conn->connect_error)
{
	die("connection failed:".$conn->connect_error);
}
$sql="SELECT * FROM userdata";
$result=$conn->query($sql);

if($result->num_rows>0)
{
	echo"<table><tr><th>ID</th><th>Name</th><th>Email</th></tr>";
	while($row=$result->fetch_assoc())
{
	echo"<tr><td>".$row["id"]."</td><td>".$row["name"]."</td><td>".$row["email"]."</td></tr>";
}
echo"</table>";
}else
{
echo"0 results found";
}
$conn->close();
?>
</body>
</html>
