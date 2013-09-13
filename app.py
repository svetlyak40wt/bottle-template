from bottle import route, run, default_app

@route('/')
def index():
    return "It works! You are in the Bottle now!"

application = default_app()

if __name__ == '__main__':
    run(host='localhost', port=8000, debug=True)
