from flask import Flask, request, jsonify
from flask_cors import CORS
from marshmallow import Schema, fields, ValidationError

app = Flask(__name__)
CORS(app)

# Define the expected JSON structure using Marshmallow
class FormDataSchema(Schema):
    firstName = fields.Str(required=True)
    lastName = fields.Str(required=True)
    title = fields.Str(required=True)
    email = fields.Email(required=True)
    agree = fields.Bool(required=True)

@app.route('/submitData', methods=['POST'])
def submit_data():
    schema = FormDataSchema()
    
    try:
        # Validate the incoming data against our schema
        data = schema.load(request.json)
        
        # Process and store the data as required
        # Add your Python logic or call another script/function here to process the data
        print(data)  # just a placeholder; you can store or process the data as needed
        
        return jsonify({"message": "Data received successfully!"})
    
    except ValidationError as e:
        return jsonify({"error": "Invalid data format", "messages": e.messages}), 400

@app.errorhandler(400)
def bad_request(error):
    return jsonify({"error": "Bad Request", "message": str(error)}), 400

@app.errorhandler(500)
def server_error(error):
    return jsonify({"error": "Internal Server Error", "message": "An error occurred processing your request."}), 500

if __name__ == "__main__":
    app.run(debug=True)  # debug mode for development

