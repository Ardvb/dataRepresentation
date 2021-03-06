from flask import Flask, url_for, request, redirect, abort, jsonify, make_response
from WhiskeyDAO import WhiskeyDAO
from SuppliersDAO import SuppliersDAO

app = Flask(__name__, static_url_path='', static_folder='staticpages')


@app.route('/') # Message for root
def index():
    return "Hi there"

# get all whiskeys
@app.route('/whiskeys')
def getAll():
    results = WhiskeyDAO.getAll()
    return jsonify(results)

# find By id (codenr)
@app.route('/whiskeys/<codenr>')
def findById(codenr):
    foundWhiskey = WhiskeyDAO.findById(codenr)
    return jsonify(foundWhiskey)

# create whiskey
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
    
    return jsonify(WhiskeyDAO.create(whiskey))
    

# update whiskey

@app.route('/whiskeys/<codenr>', methods=['PUT'])
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

# delete whiskey
# curl -X DELETE http://127.0.0.1:5000/whiskeys/1
@app.route('/whiskeys/<codenr>', methods=['DELETE'])
def delete(codenr):
    WhiskeyDAO.delete(codenr)

    return jsonify({"done":True})
    
# get all suppliers
@app.route('/suppliers')
def getAlls():
    results = SuppliersDAO.getAll()
    return jsonify(results)

# find By id (snr)
@app.route('/suppliers/<snr>')
def findByIds(snr):
    foundSupplier =SuppliersDAO.findById(snr)
    return jsonify(foundSupplier)

# create supplier

@app.route('/suppliers', methods=['POST'])
def creates():
    
    if not request.json:
        abort(400)

    supplier = {
        "snr": request.json["snr"],
        "name": request.json["name"],
        "country": request.json["country"]
    }
    
    return jsonify(SuppliersDAO.create(supplier))
   

# update supplier

@app.route('/suppliers/<snr>', methods=['PUT'])
def updates(snr):
    foundSuppliers = SuppliersDAO.findById(snr)
    
    if foundSuppliers == {}:
        return jsonify({}), 404
    
    currentSupplier = foundSuppliers
   
    if 'name' in request.json:
        currentSupplier['name'] = request.json['name']
    if 'country' in request.json:
        currentSupplier['country'] = request.json['country']
   
    SuppliersDAO.update(currentSupplier)
    return jsonify(foundSuppliers)

# delete supplier

@app.route('/suppliers/<snr>', methods=['DELETE'])
def deletes(snr):
    SuppliersDAO.delete(snr)

    return jsonify({"done":True})
    
# error message
@app.errorhandler(404)
def not_found404(error):
    return make_response( jsonify( {'error':'Not found' }), 404)

# error message
@app.errorhandler(400)
def not_found400(error):
    return make_response( jsonify( {'error':'Bad Request' }), 400)


if __name__ == "__main__":
    app.run(debug=True)