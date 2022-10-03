from webbrowser import get


import os

class Utils:
    def get_valid_path(self, relative_path):
        return os.path.join(
            os.path.dirname(__file__), 
            relative_path
        )