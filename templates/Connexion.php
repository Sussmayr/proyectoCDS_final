<?php

$servername="DESKTOP-EV3RATL";
$connexion = array("Database"=>"FaceRecognition",
                "UID"=>"ConnectPHP",
                "PWD"=>"Pass123",
                "CharacterSet"=>"UTF-8");
$conn=sqlsrv_connect($servername,$connexion):
if ($conn){
    echo "Connexion exitosa";
}else{
    echo "fallo la connexion";
}

?>