# Third party libs
from flask_script import Manager
from flask_script import Server

# Our libs
from server.app import create_app
from server.settings import DevConfig

def main():
    app = create_app(DevConfig)
    manager = Manager(app)
    manager.add_command('runserver', Server(host='0.0.0.0'))
    manager.run()

if __name__ == '__main__':
    main()

