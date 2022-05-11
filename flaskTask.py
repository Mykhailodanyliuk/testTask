from flask import Flask, request

app = Flask(__name__)


@app.route('/likes')
def likes():
    names_string = request.args.get('names', type=str)
    names = names_string.split(',')
    error = False
    error_message = 'None'
    if names[0] == '':
        data = 'Це ніхто не вподобав'
    elif any(not name.isalpha() or len(name) > 10 for name in names):
        data = None
        error = True
        error_message = 'Неправильно введено імена'
    elif len(names) == 1:
        data = f'{names[0]} вподобав це'
    elif len(names) == 2:
        print('hjkjhkjh,')
        data = f'{names[0]} та {names[1]} вподобали це'
    elif len(names) == 3:
        data = f'{names[0], names[1]} та {names[3]} вподобали це'
    else:
        data = f'{names[0]} , {names[1]} та ще {len(names) - 2} людини вподобали це'

    response = f''' "error": "{error}", "data": "{data}", "error_message": "{error_message}" '''

    return response


if __name__ == "__main__":
    app.run(port=8000)
