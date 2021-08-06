from flask import Flask, render_template, request
from config import SECRET
from utils import list_to_str, get_sha256

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        user_request = dict(request.form)
        keys_sorted = sorted(user_request)
        values = [user_request.get(key) for key in keys_sorted]
        sign = list_to_str(values) + SECRET
        sign_hashed = get_sha256(sign)
        full_requests = user_request.copy()
        full_requests['sign'] = sign_hashed
        # print(sign, sign_hashed)
        # print(keys_sorted)
        # print(values)
        print(full_requests)
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)
