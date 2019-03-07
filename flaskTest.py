# -*- coding: utf-8 -*-
'''
@author: TC
@file: flaskTest.py
@time: 2019/3/6 23:40
'''

from flask import Flask, jsonify, request
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

@app.route("/user/<name>")
def showName(name):
    return name

@app.route("/aa/<index>/<name>")
def show_jsonify(index, name):
    return jsonify({'index':index, 'name':name}), 200

if __name__ == "__main__":
    app.run()