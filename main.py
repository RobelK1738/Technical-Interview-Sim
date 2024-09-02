import openai
import os
import time

# Initialize the OpenAI client
client = openai.OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# Helper function to simulate conversation with pauses
def simulate_response(text, pause=10):
    print(text)
    time.sleep(pause)

# Function to interact with GPT model
def ask_gpt(messages):
    completion = client.chat.completions.create(
        model="gpt-4o",  # Example model name, replace with your specific model
        messages=messages
    )
    return completion.choices[0].message.content

# Function to generate a DSA question dynamically
def generate_dsa_question():
    # Initial prompt to generate a DSA question
    prompt = [
        {"role": "system", "content": "You are a helpful and professional interviewer conducting a technical interview."},
        {"role": "assistant", "content": "Please generate a challenging DSA question that can be asked during a technical interview. The question should involve arrays, strings, or algorithms."}
    ]
    
    question = ask_gpt(prompt)
    return question

def main():
    conversation_history = [{"role": "system", "content": "You are a helpful and professional interviewer conducting a technical interview."}]

    # 1. Greetings
    simulate_response("Interviewer: Hi, welcome to the interview! How are you doing today?", 3)
    interviewee_response = input("You: ")
    conversation_history.append({"role": "user", "content": interviewee_response})

    # 2. Ice Breaker (dynamic response)
    assistant_response = ask_gpt(conversation_history)
    simulate_response(f"Interviewer: {assistant_response}", 3)
    conversation_history.append({"role": "assistant", "content": assistant_response})

    # 3. Generate and Ask the DSA question dynamically
    dsa_question = generate_dsa_question()
    conversation_history.append({"role": "assistant", "content": dsa_question})
    simulate_response(f"Interviewer: {dsa_question}", 6)

    # Allow the interviewee to respond (this is where they can describe their approach or ask clarifying questions)
    interviewee_response = input("You: ")
    conversation_history.append({"role": "user", "content": interviewee_response})

    # Process the response dynamically, regardless of whether the interviewee answers or not
    if interviewee_response.strip():
        # If the interviewee responds, process it as usual
        assistant_response = ask_gpt(conversation_history)
        simulate_response(f"Interviewer: {assistant_response}", 3)
        conversation_history.append({"role": "assistant", "content": assistant_response})
    else:
        # If the interviewee does not respond, still continue
        simulate_response("Interviewer: Let's proceed with your attempt.", 3)

    # 4. Interviewee attempts the question (dynamic response)
    interviewee_attempt = input("You (describe your approach): ")
    conversation_history.append({"role": "user", "content": interviewee_attempt})

    assistant_response = ask_gpt(conversation_history)
    simulate_response(f"Interviewer: {assistant_response}", 4)
    conversation_history.append({"role": "assistant", "content": assistant_response})

    # 5. Execute the user's code
    code_attempt = input("You (write your code): ")
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

    # 6. Congratulation and wrap-up (dynamic response)
    assistant_response = ask_gpt(conversation_history)
    simulate_response(f"Interviewer: {assistant_response}", 4)
    conversation_history.append({"role": "assistant", "content": assistant_response})

    simulate_response("Interviewer: Congratulations on solving the problem! You did a great job thinking through the approach and implementing the solution.", 3)

    # 7. Final Q&A
    simulate_response("Interviewer: Now that we're done with the technical part, you have 5 minutes to ask me any questions you may have about the company, the role, or the hiring process.", 4)
    final_questions = input("You: ")
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
