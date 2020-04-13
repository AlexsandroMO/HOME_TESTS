#Created by:  Alexsandro Monteiro
#Date:        13/04/2020
#Site for Tests Python / Flask

#Python any Where
#https://www.pythonanywhere.com/user/AlexsandroMO/
#pip install flask

from flask import Flask, render_template, url_for, request,send_from_directory

#==================================
app = Flask(__name__)

@app.route('/')
@app.route('/home')
def home():
  return render_template('home.html')

@app.route('/apoio')
def apoio():
  return render_template('apoio.html')

@app.route('/documentacao')
def documentacao():
  return render_template('documentacao.html')

@app.route('/template')
def template():
  return render_template('template.html')

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=8080, debug=True)
