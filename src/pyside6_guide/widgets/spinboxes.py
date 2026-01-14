"""
spinboxes.py
by HundredVisionsGuy
A demo of the two main types of spinboxes
"""

import sys
from PySide6.QtWidgets import (
    QApplication,
    QLabel,
    QMainWindow,
    QVBoxLayout,
    QHBoxLayout,
    QWidget,
    QSpinBox,
    QDoubleSpinBox,
    QPushButton,
)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Would you like to add a tip?")
        self.setContentsMargins(12, 12, 12, 12)
        self.resize(320, 240)

        layout = QVBoxLayout()
        self.instructions = "Make an app that gets two different numbers: "
        self.instructions += "a whole number (integer) and a number with "
        self.instructions += "a decimal point (float). Put them each in "
        self.instructions += "a horizontal layout, and add two buttons: "
        self.instructions += "one that gets then displays the inputs, and "
        self.instructions += "one that resets the inputs and displays these "
        self.instructions += "instructions\n\n"
        self.instructions += "Feel free to modify these instructions once "
        self.instructions += "you are done. Make sure the isntructions are "
        self.instructions += "clear to the user as to what they should do."

        self.instructions_label = QLabel(self.instructions)
        self.instructions_label.setWordWrap(True)

        # Feebox: Asks user how much money they spent
        input_hbox2 = QHBoxLayout()
        feebox_label = QLabel("Payment Fee: ")
        self.feebox_spinbox = QDoubleSpinBox()

        # Feebox: Set Feebox properties
        self.feebox_spinbox.setMinimum(20)
        self.feebox_spinbox.setMaximum(1000)

        self.feebox_spinbox.setPrefix("$")
        self.feebox_spinbox.setSingleStep(10)

        # Tipbox: Asks user for Tip percentage
        input_hbox = QHBoxLayout()
        tipbox_label = QLabel("Tip Percentage: ")
        self.tipbox_spinbox = QSpinBox()
        
        # Tipbox: Set Spinbox properties
        self.tipbox_spinbox.setMinimum(20)
        self.tipbox_spinbox.setMaximum(200)

        self.tipbox_spinbox.setSuffix("%")
        self.tipbox_spinbox.setSingleStep(5)

        # Tipbox: Add layout and label
        input_hbox.addWidget(tipbox_label)
        input_hbox.addWidget(self.tipbox_spinbox)
        input_hbox2.addWidget(feebox_label)
        input_hbox2.addWidget(self.feebox_spinbox)

        # Clear Button: Sets everything to the starting condition
        clear_button = QPushButton("Clear")
        clear_button.clicked.connect(self.clear_board)

        # TODO: Create an output label to display the instructions and results

        # TODO: Re-write the instructions to tell the user what to do.

        """
        Challenge: make a simple calculator app that uses 2 inputs.
            * Pick a math or science formula (like area of circle or force).
            * Change the instructions to explain what the user should do.
            * Format the results by rounding the output to 2 decimal places.
            * Format the output using clear language.
        """

        # add widgets & layouts to main layout
        layout.addLayout(input_hbox2)
        layout.addLayout(input_hbox)
        layout.addWidget(clear_button)
        
        # layout.addWidget(self.instructions_label)

        # [OPTIONAL] Add a stretch to move everything up
        layout.addStretch()

        widget = QWidget()
        widget.setLayout(layout)

        # Set the central widget of the Window.
        self.setCentralWidget(widget)
    
    def clear_board(self):
        self.tipbox_spinbox.setValue(0)
        self.feebox_spinbox.setValue(0)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()

    app.exec()
