from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Python Operations with Flask Routing and Views</h1>'

@app.route('/print/<string:input_string>')
def print_string(input_string):
    print(input_string)
    return f'<p>Printed string: {input_string}</p>'

@app.route('/count/<int:number>')
def count(number):
    numbers_list = '<br>'.join(str(num) for num in range(1, number+1))
    return f'<p>Counting numbers up to {number}:<br>{numbers_list}</p>'

@app.route('/math/<float:num1><operation><float:num2>')
def math(num1, operation, num2):
    result = None
    if operation == '+':
        result = num1 + num2
    elif operation == '-':
        result = num1 - num2
    elif operation == '*':
        result = num1 * num2
    elif operation == 'div':
        if num2 != 0:
            result = num1 / num2
        else:
            return "Division by zero is not allowed."
    elif operation == '%':
        result = num1 % num2

    if result is not None:
        return f'<p>Result of {num1} {operation} {num2} = {result}</p>'
    else:
        return "Invalid operation or numbers provided."

if __name__ == '__main__':
    app.run(port=5555, debug=True)


# Testing code

class TestApp:

    def test_print_text(self):
        '''displays text of route in browser.'''
        response = app.test_client().get('/print/hello')
        assert 'Printed string: hello' in response.data.decode()
