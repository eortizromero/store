# -*- coding: utf-8 -*-

from flask import Flask, render_template, request, redirect, url_for, session
from flakoo import Flakoo

app = Flask(__name__)

@app.route('/')
@app.route('/home')
def home():
	# if 'server' in session:
	# 	return redirect(url_for('browse'))
	return render_template('home.html')

@app.route('/server', methods=['POST', 'GET'])
def server(vals=None):
	# if 'server' in session:
	# 	return redirect(url_for('browse'))
	if request.method == 'POST':
		server_ip = request.form['server']
		if not server_ip or server_ip == '':
			return "Field ´server´ is required"
		connect = Flakoo(server=server_ip)
		serv = connect.run_server()
		if not serv:
			return redirect(url_for('error'))
		else:
			vals = {
				'list_db': connect.list_database(),
			}
			return render_template('manager_database.html', vals=vals)

	return redirect(url_for('home'))

@app.route('/error')
def error(vals=None):

	vals = {
		'error_name': 'You need a Odoo Address similar to http://midominio.com:8069 o http://192.168.1.24:8069'
	}
	return render_template('error/error.html', vals=vals)

@app.route('/manager/database')
def manager(vals=None):

	vals = {
		'list_db': list_db,
	}
	return render_template('manager_database.html', vals=vals)

@app.route('/browse')
def browse():
	return "Welcome to Store"

app.secret_key = 'ODOOCONTAINERXCONNECTION'

if __name__ == '__main__':
	app.run(debug=True)