from flask import Flask
from flask import request

app = Flask(__name__)


@app.route('/')
def test():

    temp = request.args.get('input')
    if temp == None:
        return 'test'

    temp = int(temp)
    i = 2
    j = 0

    while temp != 1:
        if temp % i == 0:
            temp = temp / i
            if j < i:
                j = i
        else:
            i += 1

    j = str(j)

    return j


if __name__ == '__main__':
    app.run()
