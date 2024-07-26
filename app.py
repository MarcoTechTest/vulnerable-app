from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def home():
    return "Welcome to the vulnerable app!"

@app.route('/vulnerable', methods=['GET', 'POST'])
def vulnerable():
    if request.method == 'POST':
        # Example of a command injection vulnerability
        command = request.form['command']
        os.system(command)
        return "Command executed!"
    return '''
        <form method="post">
            Command: <input type="text" name="command">
            <input type="submit">
        </form>
    '''

if __name__ == "__main__":
    app.run(debug=True)
