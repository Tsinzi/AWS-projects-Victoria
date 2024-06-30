app = Flask(__name__)
@app.route("/")
def head():
    return "Hello Tsinzi"
@app.route("/second")
def head2():
    return "Hello Tsinzi"
@app.route("/forth/<string:id>")
def forth(id):
    return f"ID of this page is{id}"
if __name__ == '__main__':
     #app.run(debug=True, port=30000)
     app.run(host= '0.0.0.0', port=8080)