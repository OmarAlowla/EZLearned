import requests
from bs4 import BeautifulSoup  # Remove if not used in your project

class TextModel:
    def __init__(self, api_url):
        self.api_url = api_url

    def _make_api_request(self, prompt):
        """Helper function to make API requests."""
        payload = {
            "prompt": prompt,
            "max_tokens": 9999,
            "model": "llama3",
            "stream": False,
        }
        headers = {"Content-Type": "application/json"}
        try:
            response = requests.post(self.api_url, json=payload, headers=headers)
            response.raise_for_status()
            return response.json().get("response", "")
        except requests.exceptions.RequestException as e:
            raise Exception(f"API request failed: {str(e)}")

    def summarize_text(self, text):
        """Summarizes text in the same language as the input."""
        prompt = (
            "Summarize the following text concisely and the output MUST be in the same language as the input text."
            "The summary should be structured as HTML with the following format:\n\n"
            "<h3>Summary:</h3>\n"
            "<h4><b>Key Points:</b></h4>\n"
            "<ul>\n"
            "  <li>Point 1</li>\n"
            "  <li>Point 2</li>\n"
            "  <li>Point 3</li>\n"
            "</ul>\n"
            "<h4>Conclusion:</h4>\n"
            "<p>Conclusion text here</p>\n\n"
            "Text to summarize:\n\n"
            f"{text}"
        )
        return self._make_api_request(prompt)

    def generate_questions(self, text):
        """Generates questions in the same language as the input text."""
        prompt = (
            "Based on the following text, generate 5 multiple-choice questions. "
                "the questions and answer options MUST BE in the same language as the input text. "
            "Use this HTML format for the output:\n\n"
            "<h3>Questions:</h3>\n"
            "<div>\n"
            "  <p><b>Question 1:</b> [Write the question text here]</p>\n"
            "  <br><button class='option correct'>A) [Correct Option]</button>\n"
            "  <br><button class='option'>B) [Option 2]</button>\n"
            "  <br><button class='option'>C) [Option 3]</button>\n"
            "  <br><button class='option'>D) [Option 4]</button>\n"
            "</div>\n"
            "<div>\n"
            "  <p><b>Question 2:</b> [Write the question text here]</p>\n"
            "  <br><button class='option'>A) [Option 1]</button>\n"
            "  <br><button class='option correct'>B) [Correct Option]</button>\n"
            "  <br><button class='option'>C) [Option 3]</button>\n"
            "  <br><button class='option'>D) [Option 4]</button>\n"
            "</div>\n"
            "...\n\n"
            "Text to generate questions from:\n\n"
            f"{text}\n\n"
            "Remember: The output must be in the same language as the input text."
        )
        return self._make_api_request(prompt)

