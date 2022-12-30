from flask import Flask, jsonify, request, abort, render_template
from gameDAO import GameDAO

app = Flask(__name__, static_url_path='', static_folder='staticpages')

@app.route("/")
def home():
    results = GameDAO.getAll()
    return jsonify(results)

@app.route('/games')
def getAll():
    results = GameDAO.getAll()
    return jsonify(results)

@app.route('/games/<int:id>')
def findById(id):
	foundgame = GameDAO.findByID(id)
	if not foundgame:
		return jsonify(foundgame),204
	return jsonify(foundgame)

@app.route('/games', methods=['POST'])
def create():

    if not request.json:
        abort(400)
    game = {
        "Name": request.json['Name'],
        "Platform": request.json['Platform'],
        "Developer": request.json['Developer'],
        "Publisher": request.json['Publisher'],
        "Price": request.json['Price'],
    }
    values =(game['Name'], game['Platform'], game['Developer'], game['Publisher'], game['Price'])
    newId = GameDAO.create(values)
    game['id'] = newId
    return jsonify(game)

@app.route('/games/<int:id>', methods=['PUT'])
def update(id):
    foundgame = GameDAO.findByID(id)
    if not foundgame:
        abort(404)

    if not request.json:
        abort(400)
    reqJson = request.json
    if 'Price' in reqJson and type(reqJson['Price']) is not int:
        abort(400)

    if 'Name' in reqJson:
        foundgame['Name'] = reqJson['Name']
    if 'Platform' in reqJson:
        foundgame['Platform'] = reqJson['Platform']
    if 'Developer' in reqJson:
        foundgame['Developer'] = reqJson['Developer']
    if 'Publisher' in reqJson:
        foundgame['Publisher'] = reqJson['Publisher']
    if 'Price' in reqJson:
        foundgame['Price'] = reqJson['Price']
    values = (foundgame['Name'],foundgame['Platform'],foundgame['Developer'],foundgame['Publisher'],foundgame['Price'],foundgame['id'])
    GameDAO.update(values)
    return jsonify(foundgame)

@app.route('/games/<int:id>' , methods=['DELETE'])
def delete(id):
    GameDAO.delete(id)
    return jsonify({"done":True})

if __name__ == '__main__' :
    app.run(debug= True)