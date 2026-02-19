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
        self.resize(350, 240)

        layout = QVBoxLayout()
        self.instructions = "Enter your payment fee and how much you'd like to tip.\n"
        self.instructions += "Tips are greatly appreciated and mandatory  :)"

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

        # Calculate Button: Uses values from both spinboxes to calculate tip cost
        calc_button = QPushButton("Calculate")
        calc_button.clicked.connect(self.calculate_tip)

        # Output Box: Outputs the final fee
        output_hbox = QHBoxLayout()
        output_label = QLabel("Total Fee: ")
        self.output_value = QLabel("Tip not calculated")

        # Output Box: Adds widgets to "output_hbox"
        output_hbox.addWidget(output_label)
        output_hbox.addWidget(self.output_value)

        """
        Challenge: make a simple calculator app that uses 2 inputs.
            * Pick a math or science formula (like area of circle or force).
            * Change the instructions to explain what the user should do.
            * Format the results by rounding the output to 2 decimal places.
            * Format the output using clear language.
        """

        # add widgets & layouts to main layout
        layout.addWidget(self.instructions_label)
        layout.addLayout(input_hbox2)
        layout.addLayout(input_hbox)
        layout.addWidget(calc_button)
        layout.addLayout(output_hbox)
        layout.addWidget(clear_button)

        # [OPTIONAL] Add a stretch to move everything up
        layout.addStretch()

        widget = QWidget()
        widget.setLayout(layout)

        # Set the central widget of the Window.
        self.setCentralWidget(widget)
    
    # Defines the "clear_board" function
    def clear_board(self):
        self.tipbox_spinbox.setValue(0)
        self.feebox_spinbox.setValue(0)
        self.output_value.setText("Tip not calculated")
    
    # Defines the "calculate_tip" function
    def calculate_tip(self):
        mult = self.tipbox_spinbox.value() / 100
        tip = self.feebox_spinbox.value() * mult
        total_fee = self.feebox_spinbox.value() + tip
        self.output_value.setText("$" + str(total_fee))
        

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()

    app.exec()
