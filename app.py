# API stuff
from flask import Flask, jsonify, request

app = Flask(__name__)

# route to submit a receipt for processing
@app.route(f'/receipts/process', methods=["POST"])
def submit_receipt():
    """ Submits a receipt for processing.

        :returns: a JSON object with the ID assigned to the receipt
    """

    # TODO
    # 1. validate the input
    # 2. assign an ID to the receipt
    # 3. *possibly* compute the amount of points and save it, or save the whole receipt (more flexible, but more memory)
    # 4. respond

# route to get the points awarded to a given receipt
@app.route(f'/receipts/<receipt_id>/points', methods=["POST"])
def points_awarded(receipt_id: str):
    """ Returns the points awarded for the receipt with the given id

        :param receipt_id: the ID of the receipt
        :returns: the points awarded for the receipt
    """

    # TODO
    # 1. validate the parameter
    # 2. get (or compute) the points of the receipt with this ID
    # 3. respond


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
