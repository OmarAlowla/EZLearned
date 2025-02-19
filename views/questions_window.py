from PyQt5.QtWidgets import (
    QDialog, QVBoxLayout, QLabel, QPushButton, QScrollArea, QWidget, QSizePolicy
)
from bs4 import BeautifulSoup  # For parsing HTML

class ResultsWindow(QDialog):
    """A small window to display the quiz results."""
    def __init__(self, correct_count, incorrect_count, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Quiz Results")
        self.setGeometry(200, 200, 300, 150)

        # Create a layout for the results window
        layout = QVBoxLayout(self)

        # Add labels to display the results
        correct_label = QLabel(f"Correct Answers: {correct_count}", self)
        incorrect_label = QLabel(f"Incorrect Answers: {incorrect_count}", self)

        # Add the labels to the layout
        layout.addWidget(correct_label)
        layout.addWidget(incorrect_label)

        # Add an "OK" button to close the window
        ok_button = QPushButton("OK", self)
        ok_button.clicked.connect(self.close)
        layout.addWidget(ok_button)

        # Set the layout for the window
        self.setLayout(layout)

class QuestionsWindow(QDialog):
    def __init__(self, questions_html):
        super().__init__()
        self.setWindowTitle("Questions")
        self.setGeometry(150, 150, 1100, 400)

        # Track user answers and button references
        self.user_answers = {}  # {question_index: selected_option}
        self.buttons = {}  # {question_index: list of buttons}

        # Create a scroll area
        self.scroll_area = QScrollArea(self)
        self.scroll_area.setWidgetResizable(True)  # Allow the widget to resize

        # Create a container widget for the scroll area
        self.container = QWidget()
        self.layout = QVBoxLayout(self.container)

        # Parse the questions and answers from the HTML string
        self.questions = self.parse_questions(questions_html)

        # Add each question and its buttons to the layout
        for index, question_data in enumerate(self.questions):
            question_text = question_data["question"]
            options = question_data["options"]
            correct_answer = question_data["correct_answer"]

            # Create a label for the question
            question_label = QLabel(question_text, self.container)
            question_label.setWordWrap(True)
            self.layout.addWidget(question_label)

            # Create buttons for each option
            self.buttons[index] = []  # Store buttons for this question
            for option in options:
                button = QPushButton(option, self.container)
                button.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
                button.clicked.connect(
                    lambda checked, b=button, idx=index: self.on_option_clicked(b, idx)
                )
                self.layout.addWidget(button)
                self.buttons[index].append(button)  # Add button to the list

        # Add a "Check Results" button
        self.check_results_button = QPushButton("Check Results", self)
        self.check_results_button.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        self.check_results_button.clicked.connect(self.show_results)
        self.layout.addWidget(self.check_results_button)
        self.check_results_button.setStyleSheet("background-color: #3c0694; color: white; margin-top:20px;")

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

    def on_option_clicked(self, button, question_index):
        """Handle button clicks for options."""
        # Disable all buttons in the current question
        for btn in self.buttons[question_index]:
            btn.setEnabled(False)

        # Apply the selected answer style
        button.setStyleSheet("background-color: #3c0694; color: white;")

        # Store the user's answer
        self.user_answers[question_index] = button.text()

    def show_results(self):
        """Calculate and display the results in a new window."""
        correct_count = 0
        incorrect_count = 0

        # Check each question
        for index, question_data in enumerate(self.questions):
            correct_answer = question_data["correct_answer"]
            user_answer = self.user_answers.get(index, None)

            # Update button colors based on correctness
            for button in self.buttons[index]:
                if button.text() == user_answer:
                    if user_answer == correct_answer:
                        button.setStyleSheet("background-color: #4CAF50; color: white;")  # Green for correct
                        correct_count += 1
                    else:
                        button.setStyleSheet("background-color: #f44336; color: white;")  # Red for incorrect
                        incorrect_count += 1
                elif button.text() == correct_answer:
                    button.setStyleSheet("background-color: #4CAF50; color: white;")  # Green for correct

        # Create and show the results window
        self.results_window = ResultsWindow(correct_count, incorrect_count, self)
        self.results_window.exec_()