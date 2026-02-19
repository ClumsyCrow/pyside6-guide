import sys

from PySide6.QtWidgets import (
    QApplication,
    QCheckBox,
    QComboBox,
    QDoubleSpinBox,
    QLabel,
    QMainWindow,
    QPushButton,
    QSlider,
    QSpinBox,
    QVBoxLayout,
    QWidget,
)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # Formatting Code goes here

        ## Formatting the Main Window
        self.setWindowTitle("Coffee Order")
        self.setContentsMargins(12, 12, 12, 12)
        self.resize(350, 240)

        layout = QVBoxLayout()
        title_label = QLabel("Coffee Shop")

        ## Formatting Customer Name Layout


        ## Formatting Decaf Option Layout


        ## Formatting Sweetness ComboBox Layout


        ## Formatting Creamer ComboBox Layout

        
        ## Formatting Order Output Layout

        
        ## Compiling Layouts


    # Methods and Functions go here

    

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()

    app.exec()