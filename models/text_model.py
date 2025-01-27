import requests
from bs4 import BeautifulSoup  

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
        response = requests.post(self.api_url, json=payload, headers=headers)
        if response.status_code == 200:
            return response.json().get("response", "")
        else:
            raise Exception(f"API request failed: {response.status_code} - {response.text}")

    def summarize_text(self, text):
        """Send text to the LLaMA 3 API for summarization."""
        prompt = (
            "Summarize the following text in a concise way in the same language as the text. "
            "Ensure the output is in HTML format with the following structure:\n"
            "<h3>Summary:</h3>\n"
            "<h4><b>Key Points:</b></h4>\n"
            "<ul>\n"
            "  <li>Point 1</li>\n"
            "  <li>Point 2</li>\n"
            "  <li>Point 3</li>\n"
            "</ul>\n"
            "<h4>Conclusion:</h4>"
            "<p> conclusion here </p>\n"
            "Here is the text to summarize:\n\n"
            f"{text}"
        )
        return self._make_api_request(prompt)

    def generate_questions(self, text):
        """Send text to the LLaMA 3 API to generate questions."""
        prompt = (
            "Generate 5 multiple-choice questions based on the following text. in the same language as the text."
            "Ensure the questions are directly related to the key points in the text. "
            "Ensure the output is in HTML format with the following structure:\n"
            "<h3>Questions:</h3>\n"
            "<div>\n"
            "  <p><b>Question 1:</b> [Question text]</p>\n"
            "  <br><button class='option correct'>A) Option 1</button>\n"
            "  <br><button class='option'>B) Option 2</button>\n"  # Correct answer marked with 'correct' class
            "  <br><button class='option'>C) Option 3</button>\n"
            "  <br><button class='option'>D) Option 4</button>\n"
            "</div>\n"
            "<div>\n"
            "  <p><b>Question 2:</b> [Question text]</p>\n"
            "  <br><button class='option'>A) Option 1</button>\n"
            "  <br><button class='option correct'>B) Option 2</button>\n"  # Correct answer marked with 'correct' class
            "  <br><button class='option'>C) Option 3</button>\n"
            "  <br><button class='option'>D) Option 4</button>\n"
            "</div>\n"
            "...\n"
            "Here is the text to generate questions from:\n\n"
            f"{text}"
        )
        return self._make_api_request(prompt)

   