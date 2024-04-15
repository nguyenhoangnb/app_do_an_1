import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Long Sentence Example')
        self.setGeometry(100, 100, 400, 200)

        layout = QVBoxLayout()

        # Create a QLabel
        label = QLabel()
        
        # Set the long sentence as text
        long_sentence = "This is a very long sentence that needs to be displayed in a QLabel without being cut off. PyQt5 allows us to adjust properties such as word wrap to ensure the entire sentence is visible."
        label.setText(long_sentence)

        # Set word wrap to true
        label.setWordWrap(True)

        # Add the label to the layout
        layout.addWidget(label)

        self.setLayout(layout)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
