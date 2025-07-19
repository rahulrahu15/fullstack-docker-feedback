from flask import Flask, request, jsonify
from flask_pymongo import PyMongo
from flask_cors import CORS
import os

app = Flask(__name__)
CORS(app)

# MongoDB config
app.config["MONGO_URI"] = os.environ.get("MONGO_URI", "mongodb://mongo:27017/feedback_db")
mongo = PyMongo(app)
feedback_collection = mongo.db.feedbacks

@app.route('/api/feedback', methods=['POST'])
def receive_feedback():
    data = request.get_json()
    name = data.get('name')
    message = data.get('message')

    if not name or not message:
        return jsonify({"error": "Missing name or message"}), 400

    feedback_collection.insert_one({"name": name, "message": message})
    return jsonify({"success": True}), 200

@app.route('/api/feedback', methods=['GET'])
def list_feedback():
    feedbacks = list(feedback_collection.find({}, {"_id": 0}))
    return jsonify(feedbacks), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

