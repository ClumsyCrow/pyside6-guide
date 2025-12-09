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

        # TODO: add a text input for user's name
        self.username_input = QLineEdit()
        self.username_input.setPlaceholderText("Type your name")

        # TODO: add a push button to greet user
        greeting_button = QPushButton("The Hi Button")
        greeting_button.clicked.connect(self.get_greeting)

        # TODO: add a label to greet user
        self.greeting_label = QLabel("Enter your name, then press The Hi Button")

        # add widgets & layouts to main layout
        layout.addWidget(title_label)
        layout.addWidget(self.username_input)
        layout.addWidget(greeting_button)
        layout.addWidget(self.greeting_label)

        # [OPTIONAL] Add a stretch to move everything up
        layout.addStretch()

        widget = QWidget()
        widget.setLayout(layout)

        # Set the central widget of the Window.
        self.setCentralWidget(widget)

    # Gets user's name and greets them
    def get_greeting(self):
        username = self.username_input.text()
        greeting = f"Hi {username}!"
        self.greeting_label.setText(greeting)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()

    app.exec()