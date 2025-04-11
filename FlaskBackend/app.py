from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/process', methods=['POST'])
def process_data():
    try:
        data = request.get_json()
        
        # Process the data (you can add your processing logic here)
        processed_data = {
            'name': data.get('name'),
            'description': data.get('description'),
            'id': data.get('id'),
            'uuid': data.get('uuid'),
            'hash': data.get('hash'),
            'status': 'success',
            'message': 'Data processed successfully'
        }
        
        return jsonify(processed_data)
    except Exception as e:
        return jsonify({
            'status': 'error',
            'message': str(e)
        }), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
