from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/calculate', methods=['POST'])
def calculate():
    expression = request.form['expression']
    try:
        result = eval(expression)
    except Exception as e:
        result = str(e)
    return render_template('result.html', expression=expression, result=result)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')

