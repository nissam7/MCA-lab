   <!-- Form starts here -->
   <form  method="post">
      <h2 class="sub-heading-agileits">Booking Details</h2>
      <div class="main-flex-w3ls-sectns">
         <div class="field-agileinfo-spc form-w3-agile-text1">
           Departure <select class="form-control" name="from" id="from">
               <option>From</option>
               <option value="Kochi">Kochi</option>
               <option value="Coimbatore">Coimbatore</option>
               <option value="Dubai">Dubai </option>
               <option value="Mumbai">Mumbai</option>
               
            </select>
         </div>
         <div class="field-agileinfo-spc form-w3-agile-text2">
           Destination  <select class="form-control" name="to" id="to">
               <option>To</option>
               <option value="LosAngeles">LosAngeles</option>
               <option value="Trivandrum">Trivandrum</option>
               <option value="Chennai">Chennai</option>
               <option value="Qatar">Qatar</option>
               
            </select>
         </div>
      </div>
      
      <div class="main-flex-w3ls-sectns">
         <div class="field-agileinfo-spc form-w3-agile-text1">
           Departure Date <input id="datepicker" name="datepicker" type="date" placeholder="Departure Date" value="" required="" class="hasDatepicker">
         </div>
 <div class="field-agileinfo-spc form-w3-agile-text1">
           Departure Time <input id="timepicker" name="timepicker" type="time" placeholder="Departure Time" value="00:00:00" required="" >
         </div>
      </div>
     
      <button type="submit" class="registerbtn">Submit</button>
   </form>
   <!--// Form starts here -->
</div>
</body>
</html>

<?php
$servername = "localhost";
$username = "root";
$password = "";
$dbname = "meenu";

// Create connection
$conn = new mysqli($servername, $username, $password, $dbname);
// Check connection
if ($conn->connect_error) {
  die("Connection failed: " . $conn->connect_error);
}

if($_POST){
$to=$_POST["to"];
$from=$_POST["from"];
$datepicker=$_POST["datepicker"];
$timepicker=$_POST["timepicker"];
$sql = "INSERT INTO `airline` (`des_to`,`des_from`,`datepicker`,`timepicker`) VALUES ('$to','$from','$datepicker','$timepicker')";



$rs = mysqli_query($conn, $sql);

if($rs)
{
	echo "Booked Sucessfully";
}

$conn->close();
}
?>
