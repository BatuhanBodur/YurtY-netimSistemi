from flask import Flask, render_template
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def index():
    permissions = [
        # Örnek izin verileri
    ]
    return render_template('index.html', permissions=permissions)

if __name__ == '__main__':
    app.run(debug=True)

