<?php
$db=new mysqli("localhost","root","","nissam");
if($db->connect_error)
{
	die("connection failed:".$db->connect_error);
}
$result=$db->query("SELECT * FROM users");
while($row=$result->fetch_assoc())
{
	echo"Name:".$row['name']."<br>";
}
$db->close();
?>
