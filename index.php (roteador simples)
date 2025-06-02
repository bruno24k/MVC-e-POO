<?php
$controller = $_GET['c'] ?? 'usuario';
$action = $_GET['a'] ?? 'mostrar';
$id = $_GET['id'] ?? 1;

require_once "controllers/" . ucfirst($controller) . "Controller.php";
$controllerName = ucfirst($controller) . "Controller";
$controllerInstance = new $controllerName();
$controllerInstance->$action($id);
