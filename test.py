from flask import Flask, render_template

app = Flask(__name__)

@app.route('/hi')
def hello():
    return 'hi,welcome'

# @app.route('/')
# def fun():
#     return render_template('test.html',name='hh')

@app.route('/projects/')
def projects_01():
    return 'I am 01'


@app.route('/projects')
def projects_02():
    return 'I am 02'

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5003)
