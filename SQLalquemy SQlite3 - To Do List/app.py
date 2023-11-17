from flask import Flask, render_template, request, jsonify, redirect, url_for
from models import db, Tasks

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///" + "C:\\Users\\PERSONAL\\PycharmProjects\\pythonFlask\\SQLalquemy SQlite3 - To Do List\\database\\tasks.db"
# Disable track modifications
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

#Iniciar app
db.init_app(app)

#página principal
@app.route('/')
def home():
    try:
        tasks = Tasks.query.all()
        return  render_template('index.html', list_tasks = tasks)
    except Exception:
        Exception("[SERVER]: error ->")
        return jsonify({"msg": "Ha ocurrido un error"}), 500

#Acceder visualmente a la base de datos
@app.route('/api/tasks')
def getTasks():
    try:
        # Obtener todos los datos de la DB
        tasks = Tasks.query.all()
        toReturn = [ task.serialize() for task in tasks ]
        return jsonify(toReturn), 200
    except Exception:
        Exception("[SERVER]: error ->")
        return jsonify({"msg": "Ha ocurrido un error"}), 500

#Identificar si una tarea está hecha o no
@app.route('/api/task/done/<rowid>')
def doneTask(rowid):
    try:
        task = Tasks.query.filter_by(rowid=int(rowid)).first()
        task.done = not(task.done)
        db.session.commit()
        return redirect(url_for('home'))
    except Exception:
        Exception("[SERVER]: error ->")
        return jsonify({"msg": "Ha ocurrido un error"}), 500

#Eliminar un fila de la DB
@app.route('/api/task/delete/<rowid>')
def deleteTask(rowid):
    try:
        #Buscamos según el rowid el objeto a eliminar
        taskToDelete = Tasks.query.filter_by(rowid=int(rowid)).delete()
        db.session.commit()
        return redirect(url_for('home'))
    except Exception:
        Exception("[SERVER]: error ->")
        return jsonify({"msg": "Ha ocurrido un error"}), 500

#Crear una fila según los datos que se obtengan del input desde el index.html
@app.route('/create-task', methods=['POST'])
def create():
    try:
        # Obtener los datos que envía el formulario usando request.form.get()
        content = request.form.get('content-task')
        # Crear el objeto "task" y añadirlo a la db
        task = Tasks(content=content, done=False)
        
        db.session.add(task)
        db.session.commit()
        return redirect(url_for('home'))
    except Exception:
        Exception("[SERVER]: error ->")
        return jsonify({"msg": "Ha ocurrido un error"}), 500


if __name__ == '__main__':
    app.run(debug=True, port=4000)