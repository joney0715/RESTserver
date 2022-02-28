#REST server

from flask import Flask, make_response, jsonify

app = Flask(__name__)

#GET과 POST의 기능 구분
@app.route('/test', methods=['GET'])
def test_main():
    return make_response(jsonify(massege="This is GET test main page"), 200)

#URI에 파라미터를 입력하고 입력된 파라미터를 response
@app.route('/test/<param>', methods=['GET'])
def get_test(param):
    output = "Input word is " + param
    return make_response(jsonify(massage=output), 200)

@app.route('/test', methods=['POST'])
def post_test():
    return make_response(jsonify(massege="This is POST test main page"), 200)


if __name__ == '__main__':
    app.run()


