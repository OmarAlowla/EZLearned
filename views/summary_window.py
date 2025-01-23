from PyQt5.QtWidgets import QDialog, QVBoxLayout, QLabel, QScrollArea, QWidget, QPushButton
from PyQt5.QtCore import Qt

class SummaryWindow(QDialog):
    def __init__(self, summary, controller):
        super().__init__()
        self.setWindowTitle("Summary")
        self.setGeometry(150, 150, 500, 400)
        self.controller = controller  # Reference to the controller
        self.summary = summary  # Store the summary text

        # Create a scroll area
        self.scroll_area = QScrollArea(self)
        self.scroll_area.setWidgetResizable(True)  # Allow the widget to resize

        # Create a container widget for the scroll area
        self.container = QWidget()
        self.layout = QVBoxLayout(self.container)

        # Create a label for the summary with HTML formatting
        self.summary_label = QLabel(self.container)
        self.summary_label.setWordWrap(True)  # Enable word wrap for long text
        self.summary_label.setTextFormat(Qt.RichText)  # Enable HTML formatting
        self.summary_label.setText(self.format_summary(summary))  # Apply HTML styles
        self.layout.addWidget(self.summary_label)

        # Add a "Generate Questions" button
        self.generate_questions_btn = QPushButton("Generate Questions", self.container)
        self.generate_questions_btn.clicked.connect(self.on_generate_questions_clicked)
        self.layout.addWidget(self.generate_questions_btn)

        # Set the container widget as the scroll area's widget
        self.scroll_area.setWidget(self.container)

        # Create a main layout for the dialog
        main_layout = QVBoxLayout(self)
        main_layout.addWidget(self.scroll_area)

        # Set the main layout
        self.setLayout(main_layout)

    def format_summary(self, summary):
        """Format the summary text with HTML and CSS styles."""
        return f"""
        <html>
            <head>
                <style>
                    h3 {{
                        color: #2c3e50;
                        font-size: 20px;
                        font-weight: bold;
                        margin-bottom: 10px;
                    }}
                    p {{
                        color: #34495e;
                        font-size: 16px;
                        line-height: 1.6;
                        margin-bottom: 10px;
                    }}
                    ul {{
                        list-style-type: disc;
                        margin-left: 20px;
                        margin-bottom: 10px;
                    }}
                    li {{
                        color: #34495e;
                        font-size: 14px;
                        margin-bottom: 5px;
                    }}
                </style>
            </head>
            <body>
                {summary}
            </body>
        </html>
        """

    def on_generate_questions_clicked(self):
        """Handle the 'Generate Questions' button click."""
        # Generate questions based on the summary text
        self.controller.generate_questions(self.summary)