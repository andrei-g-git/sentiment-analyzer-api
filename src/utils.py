from webbrowser import get


import os

class Utils:
    def get_valid_path(self, relative_path):
        return os.path.join(
            os.path.dirname(__file__), 
            relative_path
        )

    def strip_and_lower(self, text):     
        return text.strip().lower()     

    # def scale_number(self, value, old_min, old_max, new_min, new_max):
    #     return (new_max - new_min) * (value - old_min) / (old_max - old_min) + new_max   

    def scale_number(self, value, min, max, scaledMin, scaledMax):
        return (scaledMax-scaledMin)*(value-min)/(max-min)+scaledMin