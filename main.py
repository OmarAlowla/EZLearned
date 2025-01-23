import sys
import os
from PyQt5.QtWidgets import QApplication
from models.text_model import TextModel
from controllers.main_controller import MainController
from views.main_window import MainWindow
from dotenv import load_dotenv
load_dotenv()

def load_stylesheet(file_path):
    absolute_path = os.path.join(os.path.dirname(__file__), file_path)
    with open(absolute_path, "r") as file:
        return file.read()

def main():
    app = QApplication(sys.argv)

    # Load the CSS file and apply the styles
    stylesheet = load_stylesheet("styles/style.css")
    app.setStyleSheet(stylesheet)

    # Initialize model, view, and controller
    api_url = os.getenv("API_URL")  # Replace with your API URL
    model = TextModel(api_url)
    view = MainWindow(None)  # Controller will be set next
    controller = MainController(model, view)
    view.controller = controller  # Set the controller for the view

    # Show the main window
    view.show()

    # Run the application
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()