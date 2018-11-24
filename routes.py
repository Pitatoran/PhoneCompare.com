from server import app
from flask import request, render_template, redirect, url_for, session, flash
app.secret_key = 'secret_key' # Use random key generator, used for session to worke properly

from system import systemManager

system = systemManager()
system.systemLoad()
phoneList = system.phoneList

session = None         # For logged in user

# Protection from access unless logged in
def loginRequired(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        if 'logged_in' in session:
            return f(*args, **kwargs)
        else:
            flash('You need to login first.')
            return redirect(url_for('index'))
    return wrap

# Root page, always directed here
@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html', phoneList=phoneList)

@app.route('/search', methods=['GET', 'POST'])
def search():
    errorMessages = []
    if request.method == 'POST':
        if "searchBtn" in request.form:
            searchPhone = request.form['search']
            results = system.searchPhone(searchPhone)
            print(results)
        return render_template('search.html', results=results)

    return render_template('search.html', phone=None)

@app.route('/compare', methods=['GET', 'POST'])
def compare():
    if request.method == 'POST':
        if "phoneOne" in request.form:
            searchPhone = request.form['phoneOne']
            phoneOne = system.getPhone(searchPhone)

            print("HERE")
            print(phoneOne.picture)
            print(phoneOne.phoneName)

            if "phoneTwo" in request.form:
                searchPhone = request.form['phoneTwo']
                phoneTwo = system.getPhone(searchPhone)

                return render_template('compare.html', phoneOne=phoneOne, phoneTwo=phoneTwo)

            return render_template('compare.html', phoneOne=phoneOne, phoneTwo=None)

    return render_template('compare.html', phoneOne=None, phoneTwo=None)

@app.route("/phone/<phoneName>/")
def phoneProfile(phoneName):
    phoneProfile = system.getPhone(phoneName)
    if phoneProfile == None:
        return render_template('phoneProfile.html', phone=None)

    return render_template('phoneProfile.html', phone=phoneProfile)

if __name__ == "__main__":
    app.run(debug=True)
