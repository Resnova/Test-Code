<html>
    <body>
        <?php
            $con = mysql_connect("localhost","root","");
            if (!$con){
                die('Could not connect: ' . mysql_error());
            }
            mysql_select_db("resnova_test", $con);
            $sql="INSERT INTO test_table (first_number, second_number)
                VALUES('$_POST[first_number]','$_POST[second_number]')";
            if (!mysql_query($sql,$con)){
                die('Error: ' . mysql_error());
            }
            echo "1 record added";
            mysql_close($con)
        ?>
    </body>
</html>