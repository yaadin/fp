from PyQt6.QtWidgets import QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QMessageBox
from controller.account import register, confirm

class RegisterView(QWidget):
    def __init__(self, on_register_success):
        super().__init__()
        self.setWindowTitle("Register")
        self.user_data = None
        self.on_register_success = on_register_success

        self.layout = QVBoxLayout()

        self.name_input = QLineEdit()
        self.name_input.setPlaceholderText("Name")
        self.layout.addWidget(self.name_input)

        self.email_input = QLineEdit()
        self.email_input.setPlaceholderText("Email")
        self.layout.addWidget(self.email_input)

        self.password_input = QLineEdit()
        self.password_input.setPlaceholderText("Password")
        self.password_input.setEchoMode(QLineEdit.EchoMode.Password)
        self.layout.addWidget(self.password_input)

        self.register_btn = QPushButton("Send Code")
        self.register_btn.clicked.connect(self.send_code)
        self.layout.addWidget(self.register_btn)

        self.code_input = QLineEdit()
        self.code_input.setPlaceholderText("Enter code from email")
        self.layout.addWidget(self.code_input)
        self.code_input.hide()

        self.confirm_btn = QPushButton("Confirm Code")
        self.confirm_btn.clicked.connect(self.confirm_code)
        self.layout.addWidget(self.confirm_btn)
        self.confirm_btn.hide()

        self.setLayout(self.layout)

    def send_code(self):
        name = self.name_input.text()
        email = self.email_input.text()
        password = self.password_input.text()

        self.user_data = register(name, email, password)
        if self.user_data:
            QMessageBox.information(self, "Code Sent", "A code was sent to your email.")
            self.code_input.show()
            self.confirm_btn.show()
        else:
            QMessageBox.warning(self, "Error", "Email already registered.")

    def confirm_code(self):
        code = int(self.code_input.text())
        name, email, password = self.user_data
        success = confirm(name, password, email, code)
        if success:
            QMessageBox.information(self, "Success", "Account created.")
            self.on_register_success()
        else:
            QMessageBox.warning(self, "Error", "Incorrect code.")
