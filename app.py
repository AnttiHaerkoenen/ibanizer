from bottle import Bottle, run

import iban_tools


app = Bottle(__name__)


@app.route('/')
def answer(iban='FI8173391393722111'):
    if iban_tools.is_valid_iban(iban):
        return f"{iban} is a valid IBAN."
    else:
        return f"{iban} is not a valid IBAN."


if __name__ == '__main__':
    run(app, host='localhost', port=8080)
