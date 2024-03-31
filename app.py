from flask import Flask, request, render_template, redirect, url_for

app = Flask(__name__)

todos = []

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/add', methods=['POST'])
def add():
    task = request.form['todo']
    todos.append({"task": task, "done": False})
    return redirect(url_for('index'))

@app.route('/remove/<int:index>', methods=['GET'])
def remove(index):
    del todos[index]
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
