from flask import Flask
import math

app = Flask(__name__)


def abs_sin(x):
    return abs(math.sin(x))


def numerical_integral(lower, upper, N):
    width = (upper - lower) / N
    total = 0
    for i in range(N):
        x = lower + i * width
        total += abs_sin(x) * width
    return total


@app.route('/numerical_integral/<float:lower>/<float:upper>/<int:N>')
def integrate(lower, upper, N):
    result = numerical_integral(lower, upper, N)
    return f"{result:.6f}"


if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1', port=5000)
