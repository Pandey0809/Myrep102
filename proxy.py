from flask import Flask, jsonify, request
import requests

app = Flask(__name__)

@app.route('/proxy', methods=['GET'])
def get_data():
    # Get the contract number from the GET request
    contract_number = request.args.get('contract_number')

    if contract_number is None:
        return jsonify({"error": "No contract_number provided"}), 400

    # Make a GET request to the API
    response = requests.get(f'http://localhost/api?contract_number={contract_number}')

    # Return the API's response
    return jsonify(response.json())

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)  # Runs the Proxy on all available network interfaces on port 80
