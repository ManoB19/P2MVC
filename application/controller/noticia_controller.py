from flask import render_template
from application import app
from application.model.entity import noticia

@app.route('/noticia')
def lista_noticia():
    return render_template('noticia.html')