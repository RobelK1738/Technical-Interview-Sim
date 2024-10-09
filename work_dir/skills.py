

##### Begin of generate_information #####

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

# Function to request detailed information about a specific topic
# Parameters:
#   topic (str): The subject or topic about which information is requested.
# Returns:
#   str: A detailed response about the topic from GPT or an error message if an exception occurs.
def get_information_about_topic(query: str):
    # Prepare a message list that sets the context for the GPT model and asks for information on the topic
    messages = [
        {"role": "system", "content": "You are a knowledgeable assistant."},  # Establishes the role of the assistant
        {"role": "user", "content": f"Provide detailed information about the topic: {query}."}  # The user's prompt asking for topic details
    ]
    
    # Use the ask_gpt function to get the information from the GPT model
    try:
        response = ask_gpt(messages)  # Send the formatted message and receive a response
        return response  # Return the detailed information from GPT
    except Exception as e:
        # Return an error message if an issue occurs
        return f"An error occurred: {e}"

# Example usage of the function:
# generate_information("Football")

#### End of generate_information ####

        

##### Begin of summarize_information #####

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


#### End of summarize_information ####

        