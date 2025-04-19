from flask import Flask, request, session, redirect, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return 'ready'

@app.route('/login', methods=['GET', 'POST'))
def login():
    if request.method == 'POST':
        # Verify user
        return redirect('dashboard')
    return render_template('login.html')
@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')

If __name__ == '__main__':
    app.run(debug=True, host='Localhost', port=8080)