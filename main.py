from app.controller import Controller
from ctypes import windll

# TODO → Make sharp the image.
windll.shcore.SetProcessDpiAwareness(1)

def start_keyword_analyzer():
    app = Controller()
    app.run()

if __name__ == "__main__":
    start_keyword_analyzer()
    
  