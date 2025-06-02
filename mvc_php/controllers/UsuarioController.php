<?php
require_once "models/Usuario.php";

class UsuarioController {
    public function mostrar($id) {
        $usuario = new Usuario($id);
        require "views/usuario_view.php";
    }
}
