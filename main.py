from app.app import create_app

app = create_app('app.config.Development')

if __name__ == '__main__':
    app.run(host=app.config['HOST'], port=app.config['PORT'])
