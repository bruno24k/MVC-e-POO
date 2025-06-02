from flask import Flask, jsonify

app = Flask(__name__)

class Animal:
    def __init__(self, nome):
        self.nome = nome

    def falar(self):
        return "Som genérico"

class Cachorro(Animal):
    def falar(self):
        return "Au au!"

class Gato(Animal):
    def falar(self):
        return "Miau!"

@app.route('/animal/<tipo>/<nome>')
def animal(tipo, nome):
    if tipo == 'cachorro':
        animal = Cachorro(nome)
    elif tipo == 'gato':
        animal = Gato(nome)
    else:
        animal = Animal(nome)
    
    return jsonify({
        'nome': animal.nome,
        'fala': animal.falar()
    })

if __name__ == '__main__':
    app.run(debug=True)
