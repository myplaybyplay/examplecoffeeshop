from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return "Hello World!"

@app.route('/adam/home')
def adamhome():
    return render_template('home.html')

@app.route('/userstr/<user_str>')
def userview(user_str):
    return 'Hello user str: {}' .format(user_str)

@app.route('/api/user/<int:user_id>')
def apiuserview(user_id):
    message = "This is a sample message \n hello user"
    return render_template('user.html', user=user_id, message=message)

@app.route('/test1')
def test1():
    users = [{
	'name': 'adam',
	'id':12341234,
	'roles': ['admin', 'edit', 'bob', 'herald']
    }, {
	'user': 'adam',
	'id': 34564,
	'roles': ['user', 'edit']
    }]
    return render_template('test1.html', users=users)

@app.route('/test2')
def test2():
    users = [{
	'name': 'adam',
	'id':12341234,
	'roles': ['admin', 'edit', 'bob', 'herald']
    }, {
	'user': 'adam',
	'id': 34564,
	'roles': ['user', 'edit']
    }]
    return render_template('test2.html', users=users)





if __name__ == "__main__":
    app.run(debug = True)

