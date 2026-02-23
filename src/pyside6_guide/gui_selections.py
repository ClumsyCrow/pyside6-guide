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
        self.resize(270, 230)

        layout = QVBoxLayout()
        title_label = QLabel("Coffee Shop")

        ## Formatting Customer Name Layout
        customer_name_hbox = QHBoxLayout()
        customer_name_label = QLabel("Your name: ")
        self.customer_name_input = QLineEdit()
        self.customer_name_input.setPlaceholderText("Enter your name")

        ### Adding Widgets to Layout
        customer_name_hbox.addWidget(customer_name_label)
        customer_name_hbox.addWidget(self.customer_name_input)

        ## Formatting Decaf Option Layout
        decaf_hbox = QHBoxLayout()
        decaf_label = QLabel("Non-caffeine Option: ")
        self.decaf_input = QCheckBox()

        ### Adding Widgets to Layout
        decaf_hbox.addWidget(decaf_label)
        decaf_hbox.addWidget(self.decaf_input)

        ## Formatting Sweetness ComboBox Layout
        sweet_hbox = QHBoxLayout()
        sweet_label = QLabel("Sugar Option: ")
        self.sweet_input = QComboBox()
        self.sweet_input.addItems(["Normal Sugar", "Half Sugar", "No Sugar"])
        self.sweet_input.setEditable(False)

        ### Adding Widgets to Layout
        sweet_hbox.addWidget(sweet_label)
        sweet_hbox.addWidget(self.sweet_input)

        ## Formatting Creamer ComboBox Layout

        
        ## Formatting Order Output Layout

        
        ## Compiling Layouts
        layout.addLayout(customer_name_hbox)
        layout.addLayout(decaf_hbox)
        layout.addLayout(sweet_hbox)
        
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