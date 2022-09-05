import json
import redis
from redis import StrictRedis
import os
import flask
from flask import Flask
from flask import Flask, render_template, request

#convert data from json to my redis database
r = redis.StrictRedis(host='localhost', port=6379, db=0)
with open('/Users/yiwenchen/desktop/nosql/redis/data.json',encoding="utf8") as data_file:
    test_data = json.load(data_file)
    for x in test_data:
        r.set(str(x['state']), int(x['cases']))


app = Flask(__name__)


@app.route('/')
def index():
    outdat = "Hello"
    return render_template('index.html', data = outdat)

@app.route('/', methods=['POST'])
def my_form_post():
    state = request.form['state']
    cases = request.form['cases']
    option = request.form['command']
    if option == "Search":
        cases = r.get(state)
        if cases is None:
            text = ("incorrect entry. Please try again")
            return render_template('index.html', data = text)
        else:
            text = ("state:",state,"cases:",cases,"(please ignore the 'b' in front)")
            return render_template('index.html', data = text)
        
    elif option == "Update":
        cases = r.get(state)
        if state is None:
            text = ("please provide name of state")
            return render_template('index.html', data = text)
        else:
            if cases is None:
                r.set(state, cases)
                text = ("state: ", state , "cases: ", cases, ". New Entry Created!")
                return render_template('index.html', data = text)
            else:
                r.set(state, cases)
                text = ("state: ", state , "cases: ", cases, ". UPDATED!")
                return render_template('index.html', data = text)
            
    elif option == "Delete":
        cases = r.get(state)
        if cases is None:
            text = ("incorrect entry. Please try again")
            return render_template('index.html', data = text)
        else:
            r.delete(state, cases)
            text = ("state: ", state , "cases: ", cases, ". DELETED!")
            return render_template('index.html', data = text)

if __name__=='__main__':
     app.run("0.0.0.0",port=80)
