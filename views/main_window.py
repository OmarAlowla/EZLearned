from PyQt5.QtWidgets import QMainWindow, QTextEdit, QPushButton, QVBoxLayout, QWidget, QLabel, QMessageBox
from views.summary_window import SummaryWindow

class MainWindow(QMainWindow):
    def __init__(self, controller):
        super().__init__()
        self.controller = controller
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("LearnApp")
        self.setGeometry(100, 100, 600, 400)

        # Create widgets
        self.input_text = QTextEdit(self)
        self.input_text.setPlaceholderText("Enter your text here...")

        self.summarize_button = QPushButton("Summarize Text", self)
        self.summarize_button.clicked.connect(self.on_summarize_clicked)

        # Layout
        layout = QVBoxLayout()
        layout.addWidget(self.input_text)
        layout.addWidget(self.summarize_button)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

    def on_summarize_clicked(self):
        """Handle the 'Summarize Text' button click."""
        text = self.input_text.toPlainText()
        self.controller.summarize_text(text)

    def show_summary(self, summary):
        """Show the summary window."""
        self.summary_window = SummaryWindow(summary, self.controller)
        self.summary_window.show()

    def show_questions(self, questions):
        """Show the questions window."""
        from views.questions_window import QuestionsWindow
        self.questions_window = QuestionsWindow(questions)
        self.questions_window.show()

    def show_error(self, message):
        """Show an error message."""
        QMessageBox.critical(self, "Error", message)