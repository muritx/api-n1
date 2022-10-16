from flask import Flask, request
from bd import aparelhos
from flask_cors import CORS

app = Flask(__name__)

cors = CORS(app, resource={r"/*":{"origins": "*"}})

def main():
    port = int(os.environ.get("PORT",5000))
    app.run(host="0.0.0.0", port=port)

if __name__ == "__main__":
    main()

@app.route("/aparelhos", methods=['GET'])
def aparelhos_get():
    return aparelhos

@app.route("/aparelhos", methods=['POST'])
def aparelhos_creat():
    novo_aparelho = request.json
    aparelhos.append(novo_aparelho)
    return aparelhos

@app.route("/aparelhos", methods=['DELETE'])
def aparelhos_delet():
    delet_aparelho = request.json
    if delet_aparelho in aparelhos:
        aparelhos.remove(delet_aparelho)
        return aparelhos
    else:
        return "<h1>Aparelho não encontrado!</h1>"
    
@app.route("/aparelhos", methods=['PUT'])
def aparelho_put():
    put_aparelho = request.json
    id = put_aparelho.get("id")
    nome = put_aparelho.get("nome")
    
    aparelhos[id]["nome"] = nome
        
    return aparelhos 
 
@app.route("/aparelhos", methods=['PATCH'])
def aparelho_patch():
    patch_aparelho = request.json
    id = patch_aparelho.get("id")
    nome = patch_aparelho.get("nome")
    marca = patch_aparelho.get("marca")
    
    aparelhos[id]["nome"] = nome
    aparelhos[id]["marca"] = marca
        
    return aparelhos  
app.run()