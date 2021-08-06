from flask import Flask, render_template, request
from config import SECRET

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        amount = request.form['amount']
        currency = request.form['currency']
        description = request.form['description']
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)
