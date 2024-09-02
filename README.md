# Technical Interview Sim

This project is a dynamic technical interview simulator built using Streamlit and OpenAI's GPT model. The simulator guides the user through a technical interview process, generating responses in real-time based on user input. It includes an ice breaker, follow-up questions, a dynamic coding challenge, and a final Q&A session.

## Features

- **Dynamic Conversation Flow:** The interview process is interactive, with the interviewer's responses generated in real-time based on the interviewee's answers.
- **Coding Challenge:** The user is presented with a dynamic coding challenge, and their code is executed and evaluated within the app.
- **Final Q&A Session:** The interview concludes with a Q&A session where the user can ask any remaining questions, with responses generated dynamically.

## Getting Started

### Prerequisites

- Python 3.7 or later
- Streamlit
- OpenAI API Key

### Installation

1. **Clone the repository:**

```bash
git clone https://github.com/RobelK1738/Technical-Interview-Sim cd technical-interview-sim
```


2. **Install the required Python packages:**

You can install the required packages using `pip`:

```bash
pip install -r requirements.txt
```


Ensure that `streamlit` and `openai` are included in your `requirements.txt`.

3. **Set up the OpenAI API Key:**

You need an OpenAI API key to interact with the GPT model. Set it as an environment variable:

```bash
export OPENAI_API_KEY="your-openai-api-key"
```


Replace `"your-openai-api-key"` with your actual OpenAI API key.

### Running the App

To run the Streamlit app, use the following command:

```bash
chmod +x streamlit.py
./streamlit.py
```


This will launch the Streamlit app in your default web browser.

## How It Works

1. **Initial Setup:**
   - The conversation starts with a greeting and an ice breaker question.
   - The interview progresses based on the user's responses.

2. **Coding Challenge:**
   - The interviewer presents a coding challenge.
   - The user writes and executes their code within the app.
   - The code is evaluated, and the interviewer provides feedback dynamically.

3. **Final Q&A:**
   - The interview concludes with a Q&A session, where the user can ask any remaining questions.

## Contributing

If you'd like to contribute to this project, feel free to fork the repository and submit a pull request. We welcome contributions that improve functionality, add features, or enhance the user experience.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgements

- [Streamlit](https://streamlit.io/)
- [OpenAI](https://www.openai.com/)

## Contact

For any questions or inquiries, please contact [robel.kebede@bison.howard.edu] or [noahahmed.seid@bison.howard.edu].
