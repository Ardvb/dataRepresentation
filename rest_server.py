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
# find By id (codenr)
@app.route('/whiskeys/<int:codenr>')
def findById(codenr):
    foundWhiskey = WhiskeyDAO.findById(codenr)
    return jsonify(foundWhiskey)

# create
# curl -X POST -d "{\"Title\":\"test\", \"Author\":\"some guy\", \"Price\":123}" http://127.0.0.1:5000/whiskeys
@app.route('/whiskeys', methods=['POST'])
def create():
    
    if not request.json:
        abort(400)

    whiskey = {
        "codenr": request.json["codenr"],
        "name": request.json["name"],
        "country": request.json["country"],
        "age": request.json["age"],
        "price": request.json["price"]
    }
    
    #values =(whiskeys['name'],whiskeys['distillery'],whiskeys["age"], whiskeys["price"], whiskeys["country_id"])
    #newId = WhiskeyDAO.create(values)
    #whiskeys['id'] = newId
    return jsonify(WhiskeyDAO.create(whiskey))
    # return "served by Create "

#update
# curl -X PUT -d "{\"Title\":\"new Title\", \"Price\":999}" -H "content-type:application/json" http://127.0.0.1:5000/whiskeys/1
@app.route('/whiskeys/<int:codenr>', methods=['PUT'])
def update(codenr):
    foundWhiskeys = WhiskeyDAO.findById(codenr)
    
    if foundWhiskeys == {}:
        return jsonify({}), 404
    
    currentWhiskey = foundWhiskeys
   
    if 'name' in request.json:
        currentWhiskey['name'] = request.json['name']
    if 'country' in request.json:
        currentWhiskey['country'] = request.json['country']
    if 'age' in request.json:
        currentWhiskey['age'] = request.json['age']
    if 'price' in request.json:
        currentWhiskey['price'] = request.json['price']
   
    WhiskeyDAO.update(currentWhiskey)
    return jsonify(foundWhiskeys)

#delete
# curl -X DELETE http://127.0.0.1:5000/whiskeys/1
@app.route('/whiskeys/<int:codenr>', methods=['DELETE'])
def delete(codenr):
    WhiskeyDAO.delete(codenr)

    return jsonify({"done":True})
    

if __name__ == "__main__":
    app.run(debug=True)