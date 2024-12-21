#imports
from flask import Flask, request, jsonify
from dotenv import load_dotenv
from assistent_bot_health import create_thread

load_dotenv()

app = Flask(__name__)

@app.route("/opeani-bothealth", methods=["GET"])
def check_route():
    return "the route is up and running", 200

@app.route("/opeani-bothealth/thread_id", methods=["GET"])
def generate_thread_id():
    thread_id = create_thread()
    response = { "thread_id" : thread_id.id }
    return  jsonify(response), 200

if __name__ == "__main__":
    app.run(debug = True)
