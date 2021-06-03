from flask import Flask, request

app = Flask(__name__)

string = ""

@app.route("/")
def hello():
    return "Hello, World !"

# @app.route("/abc/<string:username>/<string:name>", methods=["POST", "GET"])
# def abc(username, name):
#     return "I got a username - " + username + " name - " + name

# @app.route("/post", methods=["POST", "GET"])
# def post():
#     data = request.json
#     print(data)
#     return data

@app.route("/<s>")
def concat(s):
    global string
    string += " "+s
    return string

if __name__ == "__main__":
    app.run(debug=True)
