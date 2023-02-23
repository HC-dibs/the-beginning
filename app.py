from flask import Flask

app = Flask(__name__) #object of a class always give it a name

@app.route("/") #selects a path on a url
def hello_world():
  return "lets get it hans"
# @ is a decorator in python

if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)