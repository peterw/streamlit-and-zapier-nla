# Zapier NLA + Google Docs Streamlit App

This project is a Streamlit application that uses Zapier's NLA  and OpenAI to process user instructions. The application mainly interacts with Google Docs based on the processed instructions and performs actions like creating a new doc, generating content and adding the content to the doc.

## Getting Started

### Prerequisites

You will need the following to run this application:

- An OpenAI API key you can get from [here](https://platform.openai.com/)
- Set up your Zapier NLA [here](https://nla.zapier.com/start/) and enable the following:
"Google Docs: Append Text to Document"
- A Zapier NLA API key you can get from [here](https://nla.zapier.com/credentials/)

### Installing

To install the necessary libraries, run:

```bash
pip install -r requirements.txt
```

### Running the Application

To run the application, navigate to the directory containing the script and run:

```bash
streamlit run main.py
```

Then, open your web browser and go to `http://localhost:8501` to view and interact with the application.

## Usage

In the text box provided, enter your instruction for the application. Then, click the "Submit" button. The application will process your instruction and generate an appropriate output, which will be displayed on the screen.

## License

This project is licensed under the MIT License.
