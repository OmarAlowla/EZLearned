from PyQt5.QtWidgets import QDialog, QVBoxLayout, QLabel, QPushButton, QScrollArea, QWidget, QSizePolicy
from bs4 import BeautifulSoup  # For parsing HTML

class QuestionsWindow(QDialog):
    def __init__(self, questions_html):
        super().__init__()
        self.setWindowTitle("Questions")
        self.setGeometry(150, 150, 1000, 400)

        # Create a scroll area
        self.scroll_area = QScrollArea(self)
        self.scroll_area.setWidgetResizable(True)  # Allow the widget to resize

        # Create a container widget for the scroll area
        self.container = QWidget()
        self.layout = QVBoxLayout(self.container)

        # Parse the questions and answers from the HTML string
        self.questions = self.parse_questions(questions_html)

        # Add each question and its buttons to the layout
        for question_data in self.questions:
            question_text = question_data["question"]
            options = question_data["options"]
            correct_answer = question_data["correct_answer"]

            # Create a label for the question
            question_label = QLabel(question_text, self.container)
            question_label.setWordWrap(True)
            self.layout.addWidget(question_label)

            # Create buttons for each option
            for option in options:
                button = QPushButton(option, self.container)
                button.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed) 
                button.clicked.connect(
                    lambda checked, b=button, ca=correct_answer, opts=options: self.on_option_clicked(b, ca, opts)
                )
                self.layout.addWidget(button)

        # Set the container widget as the scroll area's widget
        self.scroll_area.setWidget(self.container)

        # Create a main layout for the dialog
        main_layout = QVBoxLayout(self)
        main_layout.addWidget(self.scroll_area)

        # Set the main layout
        self.setLayout(main_layout)

    def parse_questions(self, questions_html):
        """Parse the questions and answers from the HTML string."""
        soup = BeautifulSoup(questions_html, "html.parser")
        questions = []

        # Find all question divs
        for question_div in soup.find_all("div"):
            question_text = question_div.find("p").text.strip() if question_div.find("p") else ""
            options = []
            correct_answer = ""

            # Find all buttons (options)
            for button in question_div.find_all("button", class_="option"):
                option_text = button.text.strip()
                options.append(option_text)

                # Check if the button is the correct answer
                if "correct" in button.get("class", []):
                    correct_answer = option_text

            if question_text and options:
                questions.append({
                    "question": question_text,
                    "options": options,
                    "correct_answer": correct_answer,
                })

        return questions

    def on_option_clicked(self, button, correct_answer, options):
        """Handle button clicks for options."""
        print(f"Selected option: {button.text()}")
        print(f"Correct answer: {correct_answer}")

        # Disable all buttons in the current question
        for i in range(self.layout.count()):
            widget = self.layout.itemAt(i).widget()
            if isinstance(widget, QPushButton) and widget.text() in options:
                widget.setEnabled(False)

        # Check if the selected option is correct
        if button.text() == correct_answer:
            print("Correct answer selected!")
            button.setStyleSheet("background-color: #4CAF50; color: white;")  # Green for correct
        else:
            print("Incorrect answer selected!")
            button.setStyleSheet("background-color: #f44336; color: white;")  # Red for incorrect
            # Find and highlight the correct answer
            for i in range(self.layout.count()):
                widget = self.layout.itemAt(i).widget()
                if isinstance(widget, QPushButton) and widget.text() == correct_answer:
                    widget.setStyleSheet("background-color: #4CAF50; color: white;")  # Green for correct

        # Reapply the stylesheet to update the button styles
        self.setStyleSheet(self.styleSheet())