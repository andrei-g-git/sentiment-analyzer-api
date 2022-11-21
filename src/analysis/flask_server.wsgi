import sys
sys.path.insert(0, "/var/www/sentiment-server")

activate_this = "fill this in later"
with open(activate_this) as file:
    exec(file.read(), dict(__file__=activate_this))

from flask_app import app as application    