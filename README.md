# **EZLearned**

**EZLearned** is a user-friendly application designed to simplify learning and understanding of long texts. The application uses artificial intelligence (AI) to summarize texts and generate questions based on the content. This allows users to quickly grasp the essence of a text and test their understanding through interactive questions.

---

## **Features**

1. **Text Summarization**:
   - Users can input a long text, and the application generates a concise summary.
   - The summary includes key points and a brief conclusion to make the content easily understandable.

2. **Question Generation**:
   - Based on the summary, the application generates multiple-choice questions.
   - The questions are designed to test the understanding of key concepts.

3. **Interactive Learning**:
   - Users can answer the questions and receive immediate feedback.
   - Correct answers are highlighted in green, while incorrect answers are highlighted in red. The correct answer is also displayed.

4. **Scrollable Windows**:
   - Both the summary and questions are displayed in scrollable windows to facilitate navigation with long content.

5. **User-Friendly Interface**:
   - The application features an intuitive user interface that allows users to input texts, generate summaries, and answer questions.

---

## **Technical Implementation**

- **Programming Language**: Python
- **GUI Library**: PyQt5 for the user interface
- **AI Integration**: Utilizes an AI API (e.g., LLaMA 3) for text summarization and question generation
- **HTML/CSS**: Styling of summaries and questions for better readability
- **Modular Structure**: The project is divided into Model-View-Controller (MVC) to improve maintainability and extensibility.

---

## **Workflow**

1. **Text Input**:
   - The user inputs a long text into the input field.

2. **Generate Summary**:
   - The application sends the text to the AI API to create a summary.
   - The summary is displayed in a scrollable window.

3. **Generate Questions**:
   - The user clicks the "Generate Questions" button to create questions based on the summary.
   - The questions are displayed in a new window.

4. **Answer Questions**:
   - The user answers the questions and receives immediate feedback.

---

## **Benefits**

- **Time-Saving**: Users can quickly understand long texts without having to read the entire content.
- **Interactivity**: The question generation promotes active learning and helps reinforce the material.
- **User-Friendly**: The intuitive interface makes the application accessible to everyone, regardless of technical knowledge.

---

## **Future Enhancements**

1. **Export Functionality**:
   - Ability to export summaries and questions as PDF or text files.

2. **Topic-Based Questions**:
   - Generation of questions on specific topics or sections of the text.

3. **Multilingual Support**:
   - Extending the application to process texts in various languages.

4. **User Accounts**:
   - Introduction of user accounts to save progress and provide personalized learning recommendations.

---

## **Getting Started**

### **Prerequisites**

- Python 3.x
- PyQt5
- Requests library
- BeautifulSoup library

### **Installation**

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/EZLearned.git
   cd EZLearned
   ```

2. Install the required dependencies:
   ```bash
   pip install PyQt5 requests beautifulsoup4
   ```

3. Run the application:
   ```bash
   python main.py
   ```

---

## **Contributing**

Contributions are welcome! Please follow these steps:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature/YourFeatureName`).
3. Commit your changes (`git commit -m 'Add some feature'`).
4. Push to the branch (`git push origin feature/YourFeatureName`).
5. Open a pull request.

---

## **License**

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

## **Acknowledgments**

- Thanks to the developers of PyQt5 for the powerful GUI framework.
- Special thanks to the AI API providers for enabling text summarization and question generation.

---


**EZLearned** is a powerful tool for students, learners, and anyone who wants to learn quickly and efficiently. By combining AI-powered text summarization with interactive questions, the application offers a modern solution for understanding and reinforcing knowledge.
