#!/usr/bin/env python3

from bottle import route, run, template, request
import pyfiglet

@route('/figlet_text')
def input():
    return template('''
    <form action = "/login" method="post">
    String:
    <input name="text" value="input text">
    <p>
    <select name="font"
    %for a in fonts:
    <option>{{a}}</option>
    %end
    </select>
    <p>
    <input type="submit">
    <p>
    </fork>
    ''', fonts=pyfiglet.FigletFont.getFonts())

@route('/login', method='POST')
def output():
    string = pyfiglet.figlet_format(request.forms.get("text"), font=request.forms.get("font"))
    return "<pre>" + string + "</pre>"

run(host='localhost', port=8080)
