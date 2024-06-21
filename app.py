from flask import Flask
import random

app = Flask(__name__)

@app.route('/')
def main_page():
    a = random.randint(0, 100)
    b = random.randint(0, 100)
    c = random.randint(0, 100)
    d = random.randint(0, 100)
    return f'<h1>Реши примеры</h2>' \
           f'<p>{a} + {b} =</p>' \
           f'<p>{c} - {d} =</p>'


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)