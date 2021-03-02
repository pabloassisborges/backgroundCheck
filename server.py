from os import environ
from bgcheck import app


if __name__ == '__main__':
    app.run(
        host=environ.get('SERVER_HOST', '0.0.0.0'),
        port=int(environ.get('SERVER_PORT', '8080')),
        debug=(not environ.get('FLASK_ENV', 'development').lower() == 'production'),
        threaded=environ.get('FLASK_ENV', 'development').lower() == 'production'
    )
