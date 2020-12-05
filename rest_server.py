from flask import Flask, url_for, request, redirect, abort, jsonify
from WhiskeyDAO import WhiskeyDAO

app = Flask(__name__, static_url_path='', static_folder='staticpages')


@app.route('/')
def index():
    return "Hi there"
#get all
@app.route('/whiskeys')
def getAll():
    results = WhiskeyDAO.getAll()
    return jsonify(results)
# find By id
@app.route('/whiskeys/<int:id>')
def findById(id):
    foundWhiskey = WhiskeyDAO.findById(id)
    return jsonify(foundWhiskey)

# create
# curl -X POST -d "{\"Title\":\"test\", \"Author\":\"some guy\", \"Price\":123}" http://127.0.0.1:5000/whiskeys
@app.route('/whiskeys', methods=['POST'])
def create():
    
    if not request.json:
        abort(400)

    whiskeys = {
        "name": request.json["name"],
        "distillery": request.json["distillery"],
        "age": request.json["age"],
        "price": request.json["price"],
        "country_id": request.json["country_id"]
    }
    
    #values =(whiskeys['name'],whiskeys['distillery'],whiskeys["age"], whiskeys["price"], whiskeys["country_id"])
    #newId = WhiskeyDAO.create(values)
    #whiskeys['id'] = newId
    return jsonify(WhiskeyDAO.create(whiskeys))
    # return "served by Create "

#update
# curl -X PUT -d "{\"Title\":\"new Title\", \"Price\":999}" -H "content-type:application/json" http://127.0.0.1:5000/whiskeys/1
@app.route('/whiskeys/<int:id>', methods=['PUT'])
def update(id):
    foundWhiskeys = list(filter(lambda t: t["id"] == id, whiskeys))
    if len(foundWhiskeys) == 0:
        return jsonify({}), 404
    currentWhiskey = foundWhiskeys[0]
    if 'Name' in request.json:
        currentWhiskey['Name'] = request.json['Name']
    if 'Distillery' in request.json:
        currentWhiskey['Distillery'] = request.json['Distillery']
    if 'Age' in request.json:
        currentWhiskey['Age'] = request.json['Age']
    if 'Price' in request.json:
        currentWhiskey['Price'] = request.json['Price']
    if 'Country_id' in request.json:
        currentWhiskey['Country_id'] = request.json['Country_id']

    return jsonify(currentWhiskey)

#delete
# curl -X DELETE http://127.0.0.1:5000/whiskeys/1
@app.route('/whiskeys/<int:id>', methods=['DELETE'])
def delete(id):
    foundWhiskeys = list(filter(lambda t: t["id"] == id, whiskey))
    if len(foundWhiskeys) == 0:
        return jsonify({}), 404
    whiskey.remove(foundWhiskeys[0])

    return jsonify({"done":True})


if __name__ == "__main__":
    app.run(debug=True)