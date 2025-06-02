<?php
class Usuario {
    public $id;
    public $nome;

    public function __construct($id) {
        $this->id = $id;
        $this->nome = "Usuário " . $id;
    }
}
