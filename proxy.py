import requests
from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/proxy', methods=['GET'])
def get_data():
    # Get the contract number from the GET request
    contract_number = request.args.get('contract_number')

    if contract_number is None:
        return jsonify({"error": "No contract_number provided"}), 400

    # Make a GET request to the API
    response = requests.get(f'https://testwebappmocc.azurewebsites.net/api?contract_number={contract_number}')
    # Return the API's response
    return jsonify(response.json())

if __name__ == '__main__':
    app.run(port=8080)  # Runs the Proxy on localhost:7000
