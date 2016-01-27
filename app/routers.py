"""Search from app directory app module (now found from __init__.py)"""
from app import app
#render_template gives you access to Jinja2 template
from flask import render_template, request, make_response

#This is comment also, but you can use # only in one line comments

@app.route('/')
def index():
    name = 'Aku'
    address = 'Ankkalinna'
    response = make_response(render_template('template_index.html', title=address, name=name))
    response.headers.add('Cache-control','no-cache')
    response.headers.add('diipadaapa','jippii')
    return response

@app.route('/user/<name>')
def user(name):
    print("User-Agent: " + request.headers.get('User-Agent'))
    return render_template('template_user.html',name=name)

#Example how you can define route methods
@app.route('/user',methods=['GET','POST'])
def userParams():
    name = request.args.get('name')
    return render_template('template_user.html',name=name)
    
#print('This is not any more included in index() function')
