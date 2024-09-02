import openai
import os
import streamlit as st
import time

# Initialize the OpenAI API key
openai.api_key = os.getenv("OPENAI_API_KEY")

# Helper function to simulate conversation with pauses
def simulate_response(text, pause=10):
    st.write(text)  # Use Streamlit to display text
    time.sleep(pause)

# Function to interact with GPT model
def ask_gpt(messages):
    completion = openai.ChatCompletion.create(
        model="gpt-4o",  # Example model name, replace with your specific model
        messages=messages
    )
    return completion.choices[0].message['content']

def main():
    st.title("Technical Interview Simulator")

    conversation_history = [{"role": "system", "content": "You are a helpful and professional interviewer conducting a technical interview."}]

    # 1. Greetings
    simulate_response("Interviewer: Hi, welcome to the interview! How are you doing today?", 3)
    interviewee_response = st.text_input("You: ", "Type your response here...")
    
    if interviewee_response:
        conversation_history.append({"role": "user", "content": interviewee_response})

        # 2. Ice Breaker (dynamic response)
        assistant_response = ask_gpt(conversation_history)
        simulate_response(f"Interviewer: {assistant_response}", 3)
        conversation_history.append({"role": "assistant", "content": assistant_response})

        # 3. Follow-up based on interviewee's input
        interviewee_response = st.text_input("You (continue): ", "Type your response here...")

        if interviewee_response:
            conversation_history.append({"role": "user", "content": interviewee_response})
            assistant_response = ask_gpt(conversation_history)
            simulate_response(f"Interviewer: {assistant_response}", 3)
            conversation_history.append({"role": "assistant", "content": assistant_response})

            # 4. Introduce DSA question (dynamic response)
            dsa_prompt = (
                "Let's move on to the technical part of the interview. "
                "You are given an array of integers. Write a Python function to find the length of the longest subarray with a sum equal to 0."
            )
            conversation_history.append({"role": "assistant", "content": dsa_prompt})
            simulate_response(f"Interviewer: {dsa_prompt}", 6)

            # 5. Allow clarifying questions
            interviewee_response = st.text_input("You (ask any questions): ", "Type your response here...")
            if interviewee_response:
                conversation_history.append({"role": "user", "content": interviewee_response})
                assistant_response = ask_gpt(conversation_history)
                simulate_response(f"Interviewer: {assistant_response}", 3)
                conversation_history.append({"role": "assistant", "content": assistant_response})

            # 6. Interviewee attempts the question (dynamic response)
            interviewee_attempt = st.text_area("You (describe your approach): ", "Type your response here...")
            if interviewee_attempt:
                conversation_history.append({"role": "user", "content": interviewee_attempt})
                assistant_response = ask_gpt(conversation_history)
                simulate_response(f"Interviewer: {assistant_response}", 4)
                conversation_history.append({"role": "assistant", "content": assistant_response})

                # 7. Execute the user's code
                code_attempt = st.text_area("You (write your code): ", "Type your code here...")
                if st.button("Run Code"):
                    conversation_history.append({"role": "user", "content": code_attempt})

                    try:
                        local_vars = {}
                        exec(code_attempt, {}, local_vars)
                        result = local_vars
                        success_response = "The code ran successfully!"
                    except Exception as e:
                        result = str(e)
                        success_response = f"It seems there's an error in your code: \n{result}"

                    conversation_history.append({"role": "assistant", "content": success_response})
                    simulate_response(f"Interviewer: {success_response}", 4)

                # 8. Congratulation and wrap-up (dynamic response)
                assistant_response = ask_gpt(conversation_history)
                simulate_response(f"Interviewer: {assistant_response}", 4)
                conversation_history.append({"role": "assistant", "content": assistant_response})

                simulate_response("Interviewer: Congratulations on solving the problem! You did a great job thinking through the approach and implementing the solution.", 3)

                # 9. Final Q&A
                simulate_response("Interviewer: Now that we're done with the technical part, you have 5 minutes to ask me any questions you may have about the company, the role, or the hiring process.", 4)
                final_questions = st.text_input("You (ask your final questions): ", "Type your question here...")
                if final_questions:
                    conversation_history.append({"role": "user", "content": final_questions})
                    assistant_response = ask_gpt(conversation_history)
                    simulate_response(f"Interviewer: {assistant_response}", 4)
                    conversation_history.append({"role": "assistant", "content": assistant_response})

                # Final goodbyes
                assistant_response = ask_gpt(conversation_history)
                simulate_response(f"Interviewer: {assistant_response}", 3)
                simulate_response("You: Thank you! It was great talking to you too!", 2)

if __name__ == "__main__":
    main()
