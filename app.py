from flask import Flask, render_template

app = Flask(__name__) #object of a class always give it a name
 
@app.route("/") #selects a path on a url
def hello_world():
  return render_template('home.html')

if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)