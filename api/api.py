import time
from flask import Flask

app = Flask(__name__)

@app.route('/time')
def get_current_time():
    return {'time': time.time()}

@app.route('/success')
def success():
    return "Just something to prove this is still active"

if __name__ == "__main__":
    app.run(debug=True)