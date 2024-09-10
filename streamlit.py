import openai
import os
import streamlit as st

# Initialize the OpenAI client with the API key
client = openai.OpenAI(
    api_key=os.getenv("OPENAI_API_KEY"),
)

# Function to interact with GPT model using client.chat.completions.create
def ask_gpt(messages):
    completion = client.chat.completions.create(
        model="gpt-4o",  # Use your specific model
        messages=messages,
    )
    return completion.choices[0].message.content

def main():
    st.title("Technical Interview Simulator")

    if 'conversation_history' not in st.session_state:
        st.session_state.conversation_history = [
            {
                "role": "system", 
                "content": (
                    "You are a helpful and professional interviewer conducting a technical interview. "
                    "The interview has 9 distinct steps that should be followed in order: "
                    "1. Greet the interviewee and ask how they are feeling today. "
                    "2. Ask a fun, non-technical icebreaker question (such as 'If you could have any superpower, what would it be and why?'). "
                    "3. Transition into the technical part of the interview by introducing the DSA (Data Structures & Algorithms) problem. "
                    "4. Allow the interviewee to ask any clarifying questions about the problem. "
                    "5. Ask the interviewee to provide the code for their solution and help them run it. "
                    "6. Congratulate the interviewee on their effort and wrap up the technical part. "
                    "7. End the interview by allowing the interviewee to ask any final questions about the role or company. "
                    "Proceed step-by-step, making sure to be professional and encouraging."
                )
            }
        ]

    conversation_history = st.session_state.conversation_history

    if 'step' not in st.session_state:
        st.session_state.step = 1

    if st.session_state.step == 1:
        # 1. Greetings
        st.write("Interviewer: Hi, welcome to the interview! How are you doing today?")
        interviewee_response = st.text_input("You: ", key="step_1_input")

        if interviewee_response:
            conversation_history.append({"role": "user", "content": interviewee_response})
            assistant_response = ask_gpt(conversation_history)
            st.write(f"Interviewer: {assistant_response}")
            conversation_history.append({"role": "assistant", "content": assistant_response})
            if st.button("Move to next portion", key="move_step_2"):
                st.session_state.step = 2
                st.empty()

    if st.session_state.step == 2:
        # 2. Ice Breaker (dynamic response)
        st.write("Interviewer: Let's start with something fun. If you could have any superpower, what would it be and why?")
        interviewee_response = st.text_input("You: ", key="step_2_input")

        if interviewee_response:
            conversation_history.append({"role": "user", "content": interviewee_response})
            assistant_response = ask_gpt(conversation_history)
            st.write(f"Interviewer: {assistant_response}")
            conversation_history.append({"role": "assistant", "content": assistant_response})
            if st.button("Move to next portion", key="move_step_3"):
                st.session_state.step = 3
                st.empty()


    if st.session_state.step == 3:
        # 4. Introduce DSA question (dynamic response)
        dsa_prompt = (
            "Let's move on to the technical part of the interview. "
            "You are given an array of integers. Write a Python function to find the length of the longest subarray with a sum equal to 0."
        )
        interviewee_response = st.text_input("You (continue): ", key="step_4_input")
        if interviewee_response: 
            conversation_history.append({"role": "assistant", "content": dsa_prompt})
            assistant_response = ask_gpt(conversation_history)
            st.write(f"Interviewer: {assistant_response}")
            if st.button("Move to next portion", key="move_step_5"):
                st.session_state.step = 4
                st.empty()

    if st.session_state.step == 4:
        # 5. Allow clarifying questions
        interviewee_response = st.text_input("You (ask any questions): ", key="step_5_input")

        if interviewee_response:
            conversation_history.append({"role": "user", "content": interviewee_response})
            assistant_response = ask_gpt(conversation_history)
            st.write(f"Interviewer: {assistant_response}")
            conversation_history.append({"role": "assistant", "content": assistant_response})
            if st.button("Move to next portion", key="move_step_6"):
                st.session_state.step = 5
                st.empty()


    if st.session_state.step == 5:
        # 7. Execute the user's code
        code_attempt = st.text_area("You (write your code): ", key="step_7_input", height=300)
        
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
            # st.write(f"Interviewer: {success_response}")

            assistant_response = ask_gpt(conversation_history)
            st.write(f"Interviewer: {assistant_response}")
            conversation_history.append({"role": "assistant", "content": assistant_response})
            if st.button("Move to next portion", key="move_step_8"):
                st.session_state.step = 6
                st.empty()

    if st.session_state.step == 6:
        # 8. Congratulation and wrap-up (dynamic response)
        assistant_response = ask_gpt(conversation_history)
        st.write(f"Interviewer: {assistant_response}")
        conversation_history.append({"role": "assistant", "content": assistant_response})
        if st.button("Move to next portion", key="move_step_9"):
            st.session_state.step = 7
            st.empty()

    if st.session_state.step == 7:
        # 9. Final Q&A
        st.write("Interviewer: Now that we're done with the technical part, you have 5 minutes to ask me any questions you may have about the company, the role, or the hiring process.")
        final_questions = st.text_input("You (ask your final questions): ", key="step_9_input")

        if final_questions:
            conversation_history.append({"role": "user", "content": final_questions})
            assistant_response = ask_gpt(conversation_history)
            st.write(f"Interviewer: {assistant_response}")
            conversation_history.append({"role": "assistant", "content": assistant_response})

        # Final goodbyes
        assistant_response = ask_gpt(conversation_history)
        st.write(f"Interviewer: {assistant_response}")
        st.write("You: Thank you! It was great talking to you too!")

if __name__ == "__main__":
    main()
