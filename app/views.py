from app import app
import json
from flask import request, url_for, make_response, render_template
from . import validator

@app.get('/')
def index():
    return render_template('index.html')

@app.post('/get_form')
def get_form():
    data = request.get_json()
    print(data)
    response = make_response('boom')
    return response
    # fild_type = {}
    # args = request.args
    # for fild_name, fild_content in dict(args).items():
    #     fild_type[fild_name] = validator.validate(fild_content)
    # return fild_type
