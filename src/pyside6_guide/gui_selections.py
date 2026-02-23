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
    QHBoxLayout,
    QWidget,
    QLineEdit,
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
        customer_name_hbox = QHBoxLayout()
        customer_name_label = QLabel("Your name: ")
        self.customer_name_input = QLineEdit()
        self.customer_name_input.setPlaceholderText("Enter your name")

        customer_name_hbox.addWidget(customer_name_label)
        customer_name_hbox.addWidget(self.customer_name_input)
        ## Formatting Decaf Option Layout


        ## Formatting Sweetness ComboBox Layout


        ## Formatting Creamer ComboBox Layout

        
        ## Formatting Order Output Layout

        
        ## Compiling Layouts
        layout.addLayout(customer_name_hbox)

        
        layout.addStretch()
        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)


    # Methods and Functions go here

    

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()

    app.exec()