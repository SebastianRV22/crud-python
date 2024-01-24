<<<<<<< HEAD
from flask import Flask, render_template, request, redirect, url_for
import mysql.connector

app = Flask(__name__)

# Configuración de la conexión a la base de datos
db = mysql.connector.connect(
    host="beji2tmzdrly6vw0zt45-mysql.services.clever-cloud.com",
    user="udcmajmvsdshwu4g",
    password="2x0747YB7Aq2PkmHCGwg",
    database="beji2tmzdrly6vw0zt45"
)

# Cursor para ejecutar comandos SQL
cursor = db.cursor()

# Ruta para crear un nuevo registro
@app.route('/create', methods=['POST'])
def create():
    if request.method == 'POST':
        title = request.form['title']
        description = request.form['description']
        
        # Insertar datos en la base de datos
        cursor.execute("INSERT INTO tasks (title, description) VALUES (%s, %s)", (title, description))
        db.commit()

        return redirect(url_for('index'))

# Ruta para mostrar todos los registros
@app.route('/')
def index():
    # Obtener datos de la base de datos
    cursor.execute("SELECT * FROM tasks")
    data = cursor.fetchall()

    return render_template('index.html', data=data)

# Ruta para eliminar un registro
@app.route('/delete/<int:id>')
def delete(id):
    # Eliminar el registro de la base de datos
    cursor.execute("DELETE FROM tasks WHERE id = %s", (id,))
    db.commit()

    return redirect(url_for('index'))

# Ruta para actualizar un registro (página de edición)
@app.route('/edit/<int:id>')
def edit(id):
    # Obtener datos de la tarea para prellenar el formulario de edición
    cursor.execute("SELECT * FROM tasks WHERE id = %s", (id,))
    task = cursor.fetchone()

    return render_template('edit.html', task=task)

# Ruta para procesar la actualización de un registro
@app.route('/update/<int:id>', methods=['POST'])
def update(id):
    if request.method == 'POST':
        title = request.form['title']
        description = request.form['description']

        # Actualizar el registro en la base de datos
        cursor.execute("UPDATE tasks SET title = %s, description = %s WHERE id = %s", (title, description, id))
        db.commit()

        return redirect(url_for('index'))

if __name__ == "__main__":
    app.run(debug=True)
=======
from flask import Flask, render_template, request, redirect, url_for
import mysql.connector

app = Flask(__name__)

# Configuración de la conexión a la base de datos
db = mysql.connector.connect(
    host="beji2tmzdrly6vw0zt45-mysql.services.clever-cloud.com",
    user="udcmajmvsdshwu4g",
    password="2x0747YB7Aq2PkmHCGwg",
    database="beji2tmzdrly6vw0zt45"
)

# Cursor para ejecutar comandos SQL
cursor = db.cursor()

# Ruta para crear un nuevo registro
@app.route('/create', methods=['POST'])
def create():
    if request.method == 'POST':
        title = request.form['title']
        description = request.form['description']
        
        # Insertar datos en la base de datos
        cursor.execute("INSERT INTO tasks (title, description) VALUES (%s, %s)", (title, description))
        db.commit()

        return redirect(url_for('index'))

# Ruta para mostrar todos los registros
@app.route('/')
def index():
    # Obtener datos de la base de datos
    cursor.execute("SELECT * FROM tasks")
    data = cursor.fetchall()

    return render_template('index.html', data=data)

# Ruta para eliminar un registro
@app.route('/delete/<int:id>')
def delete(id):
    # Eliminar el registro de la base de datos
    cursor.execute("DELETE FROM tasks WHERE id = %s", (id,))
    db.commit()

    return redirect(url_for('index'))

# Ruta para actualizar un registro (página de edición)
@app.route('/edit/<int:id>')
def edit(id):
    # Obtener datos de la tarea para prellenar el formulario de edición
    cursor.execute("SELECT * FROM tasks WHERE id = %s", (id,))
    task = cursor.fetchone()

    return render_template('edit.html', task=task)

# Ruta para procesar la actualización de un registro
@app.route('/update/<int:id>', methods=['POST'])
def update(id):
    if request.method == 'POST':
        title = request.form['title']
        description = request.form['description']

        # Actualizar el registro en la base de datos
        cursor.execute("UPDATE tasks SET title = %s, description = %s WHERE id = %s", (title, description, id))
        db.commit()

        return redirect(url_for('index'))

if __name__ == "__main__":
    app.run(debug=True)
>>>>>>> 846e55b3ddd838bcb01f5f5a65d39e47d81d153e
