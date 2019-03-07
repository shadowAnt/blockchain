# -*- coding: utf-8 -*-
'''
@author: TC
@file: flaskTest.py
@time: 2019/3/6 23:40
'''

from flask import Flask
app = Flask(__name__)
@app.route("/")
def hello():
    return "Hello World!"

if __name__ == "__main__":
    app.run()