class MainController:
    def __init__(self, model, view):
        self.model = model
        self.view = view

    def summarize_text(self, text):
        """Handle text summarization."""
        try:
            summary = self.model.summarize_text(text)
            self.view.show_summary(summary)
        except Exception as e:
            self.view.show_error(str(e))

    def generate_questions(self, text):
        """Handle question generation."""
        try:
            questions = self.model.generate_questions(text)
            self.view.show_questions(questions)
        except Exception as e:
            self.view.show_error(str(e))