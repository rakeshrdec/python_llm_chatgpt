# Streamlit Chatbot with PDF Question Answering

This project is a Streamlit-based chatbot that allows users to upload a PDF file and ask questions related to its content. The chatbot uses OpenAI's API to provide accurate and context-aware answers.

## Features

- Upload a PDF file for analysis.
- Interactively ask questions about the uploaded PDF.
- Real-time answers powered by OpenAI's language model.

---

## Steps to Use

1. **Upload a PDF File:**
   - Run the Streamlit app.
   - Use the upload option to select a PDF file.
   - The PDF's content will be processed and ready for queries.

2. **Ask Questions from the PDF:**
   - Enter your question in the chat interface.
   - The chatbot will analyze the uploaded PDF and provide answers based on its content.

---

## Developer Guide

### Requirements

- Python 3.8+
- OpenAI API Key
- Required Python libraries (listed in `requirements.txt`)

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/your-repo-name/streamlit-chatbot.git
   cd streamlit-chatbot
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Set up your OpenAI API Key:
   - Open the `.env` file (or create one if it doesn't exist).
   - Add your OpenAI API key:
     ```env
     OPENAI_API_KEY=your_openai_api_key_here
     ```

### Running the App

1. Start the Streamlit app:
   ```bash
   streamlit run app.py
   ```

2. Open the app in your browser (usually at `http://localhost:8501`).

### Changing the OpenAI API Key

If you need to update your API key:
1. Open the `.env` file.
2. Replace the existing key with the new one.
3. Restart the app to apply changes.

---

## Project Structure

```
streamlit-chatbot/
├── app.py               # Main Streamlit application
├── utils/               # Utility scripts for PDF processing and chatbot logic
├── requirements.txt     # Python dependencies
├── .env                 # Environment variables (API keys, etc.)
├── README.md            # Project documentation
└── assets/              # Static files (images, etc.)
```

---

## Notes

- Ensure the OpenAI API key has sufficient quota and permissions.
- Large PDFs might take longer to process; consider limiting the size if needed.

---

## License

This project is licensed under the [MIT License](LICENSE).

---

## Contributions

Contributions are welcome! Feel free to open issues or submit pull requests to improve this project.

---

## Acknowledgments

- Powered by [Streamlit](https://streamlit.io/) and [OpenAI](https://openai.com/).
- Inspired by the need for seamless interaction with document-based information.
