#imports
from flask import Flask, request
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

@app.route("/opeani-bothealth", methods=["GET"])
def check_route():
    return "the route is up and running", 200

if __name__ == "__main__":
    app.run(debug = True)
