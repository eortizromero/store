# -*- coding: utf-8 -*-

from flask import Flask, render_template, request, redirect, url_for, session
from flakoo import Flakoo

app = Flask(__name__)

@app.route('/')
def home():
	if 'server' in session:
		return redirect(url_for('browse'))
	return render_template('home.html')

@app.route('/server', methods=['POST', 'GET'])
def server():
	if 'server' in session:
		return redirect(url_for('browse'))
	if request.method == 'POST':
		server_ip = request.form['server']
		if not server_ip or server_ip == '':
			return "Field ´server´ is required"
		connect = Flakoo(server=server_ip)
		serv = connect.run_server()
		if not serv:
			return "You need a server similar to http://midominio.com:8069 o http://192.168.1.24:8069"
		else:
			session['server'] = server_ip
			return redirect(url_for('browse'))
	# TODO: render a template maybe 


@app.route('/manager/database')
def manager():
	pass

@app.route('/browse')
def browse():
	return "Welcome to Store"

app.secret_key = 'ODOOCONTAINERXCONNECTION'

if __name__ == '__main__':
	app.run(debug=True)