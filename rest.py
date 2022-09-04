from crypt import methods
from distutils.log import debug
from flask import Flask,request,jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

app=Flask(__name__)


@app.route("/hello-w", methods=['GET'])
def get_hello():
    return jsonify({"message":'hello from rd rest server' })



if __name__ == "__main__":
    app.run(debug=True)