import auto
import program
import autowork
import manual

#Program

class programHandle(program.Ui_MainWindow):
    def __init__(self, main_window) :
        super().__init__()
        self.setupUi(main_window)
#By Hand Work
class manualHandle(manual.Ui_Form):
    def __init__(self, main_window):
        super().__init__()
        self.setupUi(main_window)

#autoworkHandle
class autoworkHandle(autowork.Ui_Form):
    def __init__(self, main_window):
        super().__init__()
        self.setupUi(main_window)

#autoHandle
class autoHandle(auto.Ui_Form):
    def __init__(self, main_window):
        super().__init__()
        self.setupUi(main_window)
