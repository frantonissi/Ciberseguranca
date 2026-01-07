
<?php

$con = "mysql:host=localhost;dbname:exemplo";
$pdo = new PDO($con, "admin" , "senhafoda123)");

$email = $_GET["email"];
$senha = $_GET["senha"];

//echo $email . " " . $senha;

//if ($email == "admin" and $senha == "admin123"){
//	echo " " .  "Bem vindo administrador";
//}else {
//	echo "Vc nao pode acessar";
//}

$sql = $pdo->prepare("select * from usuarios where usuario = '".$email."' and senha = '".$senha."';");
$sql->execute();
$linhas = $sql->fetchAll();

print_r($linhas);

?>