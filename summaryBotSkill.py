import openai
import os

# Initialize the OpenAI client with the API key from environment variables
# Ensure that the environment variable "OPENAI_API_KEY" is set in your environment
openai.api_key = os.getenv("OPENAI_API_KEY")

# Function to send a conversation (list of messages) to the GPT model and get the response
# Parameters:
#   messages (list): A list of dictionaries representing the conversation.
#                    Each dictionary contains 'role' (e.g., "user", "system", etc.) and 'content' (the message text).
# Returns:
#   str: The response content from GPT or an error message if an exception occurs.
def ask_gpt(messages: str):
    try:
        # Use OpenAI's GPT model to get a completion for the provided conversation
        completion = openai.chat.completions.create(
            model="gpt-4",  # Specify the model version (ensure this matches the desired version, like "gpt-4")
            messages=messages  # The conversation history as a list of messages
        )
        # Extract and return the content from the first choice in the completion response
        return completion.choices[0].message.content
    except Exception as e:
        # Return an error message if something goes wrong
        return f"An error occurred while communicating with GPT: {e}"

# Function to summarize a given text into two paragraphs
# Parameters:
#   text (str): The text to be summarized.
# Returns:
#   str: A summary of the text in two paragraphs or an error message if an exception occurs.
def summarize_into_two_paragraphs(text: str):
    # Prepare a message list to request the summarization from GPT
    messages = [
        {"role": "system", "content": "You are an expert at summarizing information."},  # Sets the model's behavior as a summarizer
        {"role": "user", "content": f"Summarize the following text into two paragraphs:\n\n{text}"}  # The user's prompt providing the text to be summarized
    ]
    
    # Use the ask_gpt function to summarize the text
    try:
        response = ask_gpt(messages)  # Send the formatted message and receive a summary
        return response  # Return the summary from GPT
    except Exception as e:
        # Return an error message if an issue occurs
        return f"An error occurred: {e}"

# Example usage of the functions:
# summary= summarize_into_two_paragraphs(information)


'''
System message:

You are a highly skilled AI assistant specialized in summarizing 
information provided by the Research Bot. Your primary goal 
is to take detailed text input and condense it into clear, 
concise summaries while retaining key points and essential information. 
When tasked with summarizing, ensure the output is coherent and provides 
an accurate representation of the original content. Your language skills are 
critical in delivering summaries that are easy to understand while 
preserving the important details of the source material.

Focus on producing high-quality summaries without requiring 
further input or feedback from the user. Your task is to summarize 
the provided information effectively, offering a well-structured 
and insightful output that fulfills the user's request in a single, 
complete response. Stop once the information has been summarized.
'''