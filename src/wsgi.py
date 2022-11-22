# File name: wsgi.py
import sys, os, logging
logging.basicConfig(stream=sys.stderr)
PROJECT_DIR = "C:/vscode-projects/sentiment-server/src"
virtual_env = "C:/vscode-projects/sentiment-server/.venv"
activate_this = os.path.join(virtual_env, 'Scripts', 'activate_this.py')
exec(open(activate_this).read(),dict(__file__=activate_this))
sys.path.append(PROJECT_DIR)

from flask_server import app as application