<?php

$_GET["email"];
$_GET["senha"];

//echo $email . " " . $senha;

if($email == "admin" and $senha == "admin123") {
    echo " " . "Bem vindo administrador";
}else{
    echo "Acesso negado";
}

?>