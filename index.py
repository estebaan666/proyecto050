from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/contacto')
def contacto():
    return render_template('contacto.html')


@app.route('/acercade')
def acercade():
    return render_template('acercade.html')


@app.route('/redes')
def redes():
    return render_template('redes.html')

@app.route('/submito', methods=['POST'])
def submit():
    name = request.form['name']
    email = request.form['email']
    return f'Bienvenido, {name} ({email})'

if __name__ == '__main__':
    app.run(debug=True)
