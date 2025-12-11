import sys
from PySide6.QtWidgets import (
    QApplication,
    QLabel,
    QMainWindow,
    QVBoxLayout,
    QWidget,
    QLineEdit,
    QPushButton,
)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Basic App")
        self.setContentsMargins(12, 12, 12, 12)
        self.resize(440, 260)

        layout = QVBoxLayout()
        title_label = QLabel("The Convenience Store")

        # Setting default values for buttons and inputs
        self.greeting_button_default = "Hi"
        self.greeting_label_default = "Enter your name, then press the Hi button"

        # TODO: add a text input for user's name
        self.username_input = QLineEdit()
        self.username_input.setPlaceholderText("Type your name")

        # Second text input field for user's last name
        self.user_last_name_input = QLineEdit()
        self.user_last_name_input.setPlaceholderText("Type your last name")

        # TODO: add a push button to greet user
        greeting_button = QPushButton(self.greeting_button_default)
        greeting_button.clicked.connect(self.get_greeting)

        # TODO: add a label to greet user
        self.greeting_label = QLabel(self.greeting_label_default)

        # Clear button
        clear_button = QPushButton("Clear everything")
        clear_button.clicked.connect(self.clear_board)

        # add widgets & layouts to main layout
        layout.addWidget(title_label)
        layout.addWidget(self.username_input)
        layout.addWidget(self.user_last_name_input)
        layout.addWidget(greeting_button)
        layout.addWidget(self.greeting_label)
        layout.addWidget(clear_button)

        # [OPTIONAL] Add a stretch to move everything up
        layout.addStretch()

        widget = QWidget()
        widget.setLayout(layout)

        # Set the central widget of the Window.
        self.setCentralWidget(widget)

        """
        Challenges:
            * Add another text input (last name, home town, etc.)
            * Add a clear button that, when clicked will
                - clear the text in the name input
                - reset the output text to its initial value
        """

    # Gets user's name and greets them
    def get_greeting(self):
        username = self.username_input.text()
        user_last_name = self.user_last_name_input
        greeting = f"Hi {username}!"
        if username == "":
            greeting = f"You didn't enter a first name, silly!"
            self.greeting_label.setText(greeting)
        elif user_last_name == "":
            greeting = f"You didn't enter a last name, silly!"
            self.greeting_label.setText(greeting)
        else:
            self.greeting_label.setText(greeting)
    
    def clear_board(self):
        reset_greeting = self.greeting_label_default
        self.greeting_label.setText(reset_greeting)
        self.username_input.clear()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()

    app.exec()