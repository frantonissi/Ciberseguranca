
<?php


$con = "mysql:host=localhost;dbname=exemplo";
$pdo = new PDO($con, "admin", "senhafoda123"); //aqui o php pede pra entrar no banco de dados, se as credenciais estiverem certas, o PDO deixa acessar


$email = $_GET["email"];
$senha = $_GET["senha"];

$sql = $pdo->prepare("select * from usuarios where usuario = '".$email."' and senha = '".$senha."'"); //o banco usando a conecao PDO pede pra fazer a sql (a verificacao)
$sql -> execute();
$linhas = $sql->fetchAll();//retorna um array com linhas
//print_r($linhas);

if (count($linhas)>0){ //se der certo, vai dar uma linha, entao ele conta uma linha
	echo"bem vindo admin";
}else{
	echo"acesso negado";
}

//echo $email . " " . $senha;

//if ($email == "admin" and $senha == "admin123"){
//	echo " " .  "Bem vindo administrador";
//}else {
//	echo "Vc nao pode acessar";
//}



?>