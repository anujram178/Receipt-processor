from flask import Flask, request

from db import Database
from helpers import calculatePoints
from models.receipt import Receipt

app = Flask(__name__)

# initialize the database
db = Database()


@app.route('/')
def home():
    return "Hello, Flask"


@app.route('/receipts/process', methods=["POST"])
def processReceipt():
    payload = request.get_json()
    # store receipt in db
    receipt = Receipt(payload)
    newId = db.add(receipt)
    return {"id": newId}

@app.route('/receipts/<string:id>/points')
def getPoints(id):
    totalPoints = calculatePoints(db.get(id))
    return {"points": totalPoints}

@app.route('/receipts')
def getAllReceipts():
    receipts = db.get_all()
    print(receipts)
    return {"receipts": receipts}

if __name__ == '__main__':
    app.run(port=8080,debug=True)
