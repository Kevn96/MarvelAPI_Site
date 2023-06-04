from flask import Flask, render_template, request
from keys import PUBLIC_KEY, PRIVATE_KEY
from marvel import Marvel
from Buscar_sites_comics import buscarComic

#Chaves para usar a API
marvel = Marvel(PUBLIC_KEY= PUBLIC_KEY,
                PRIVATE_KEY= PRIVATE_KEY)

app = Flask(__name__)

#Caminhos & Backend do site
@app.route("/")
@app.route("/<nomeHeroi>", methods=["GET"])
def buscar():
    #Buscando o valor solicitado na API
    personagens = marvel.characters
    heroiBuscado = request.args.get("buscador")
    listaDeLinks = ''
    if heroiBuscado != None:
        listaDeLinks = buscarComic(heroiBuscado)
    todos_personagens = personagens.all(nameStartsWith=heroiBuscado)['data']['results']

    listaHeros = todos_personagens
    return render_template("heros_oficial.html", listaHeros = listaHeros, listaDeLinks = listaDeLinks)



#Debugar o código
if __name__ == "__main__":
    app.run(host= '0.0.0.0', port= 5000)
    app.run(debug=True)
