from config import app
from views.home_controller import HomeController
from views.univer_controller import UniverController

if __name__ == '__main__':
    hc = HomeController()
    uc = UniverController()

    app.run()
    #test branch dev