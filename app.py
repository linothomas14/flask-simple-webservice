from flask import Flask
from flask import jsonify, make_response

app = Flask(__name__)

@app.route('/')
def hello_world():
    message = {
        'note' : 'Lino lagi belajar jenkins uhuy',
    }
    value = {
        
        'full_name' : "Yulyano Thomas Djaya",
        'nick_name' : "Lino",
        'last_education' : "Gunadarma University",
        'location' : "Bogor"
    }
    res = {
        'msg' : message,
        'value' : value
    }
    return  make_response(jsonify(res)), 200

@app.route('/hello/<name>')
def hello_name(name):
   return 'Hello %s!' % name
 
if __name__ == '__main__':
   app.run()