from flask import Flask
from flask import render_template
from flask import request,redirect,url_for
app = Flask(__name__)

@app.route('/')
def primary():
    return render_template('main.html')


def doLogin():
    1+1


@app.route('/today')
def today():
    return render_template('today.html')

@app.route('/login', methods = ['GET','POST'])
def login():
    if request.method == 'POST':
        return redirect(url_for('today'))
        return "You posted"
    else:
        return render_template('main.html')

if __name__ == '__main__':
    app.run(debug=True)
