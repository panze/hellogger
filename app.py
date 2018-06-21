import socket
from flask import Flask, request
import pprint

app = Flask(__name__)
httpmethods = ['POST', 'GET', 'PUT', 'PATCH', 'DELETE']

@app.route('/', defaults={'path': ''}, methods=httpmethods)
@app.route('/<path:path>', methods=httpmethods)
def hello_logger(path):
    ret = '{}: {} - {}'.format(socket.gethostname(), path, pprint.pformat(request.__dict__, depth=5))
    print(ret)
    return ret

if __name__ == '__main__':
    app.run(debug=True, port=int("80"), host='0.0.0.0')
    

