import os
from autogen import AssistantAgent, UserProxyAgent
import time

# Configuration for AssistantAgent using GPT-4
config_list = [{"model": "gpt-4", "api_key": os.environ["OPENAI_API_KEY"]}]

# Initialize the AssistantAgent (Interviewer) and UserProxyAgent (Interviewee)
assistant = AssistantAgent(name="assistant", llm_config={"config_list": config_list})

# Disable Docker execution
user_proxy = UserProxyAgent(name="user_proxy", code_execution_config={"use_docker": False})

# Helper function to simulate conversation with pauses
def simulate_response(text, pause=2):
    print(text)
    time.sleep(pause)

# Function to safely execute user code
def execute_user_code(code):
    local_vars = {}
    try:
        exec(code, {}, local_vars)
        return local_vars
    except Exception as e:
        return str(e)

def main():
    # 1. Greetings
    simulate_response("Interviewer: Hi, welcome to the interview! How are you doing today?", 3)
    interviewee_response = input("You: ")

    # 2. Ice Breaker
    simulate_response("Interviewer: That's great to hear! Let's start with something light. What's your favorite programming language and why?", 3)
    interviewee_response = input("You: ")

    # 3. Interviewer introduces himself
    simulate_response("Interviewer: Thanks for sharing! I'm Alex, a software engineer here at TechCorp. I've been with the company for about 5 years now, focusing mainly on backend systems and performance optimization. How about you?", 4)

    # 4. Interviewee introduces themselves
    simulate_response("Interviewer: Could you please introduce yourself and tell me a little about your background?", 3)
    interviewee_response = input("You: ")

    # 5. Interviewer gives the DSA question
    dsa_prompt = (
        "Interviewer: Great, thanks for the intro! Let's move on to the technical part of the interview. "
        "Here is your DSA problem: \n"
        "You are given an array of integers. Write a Python function to find the length of the longest subarray with a sum equal to 0. "
        "You can take some time to think about the problem before starting. Let me know if you need any clarifications."
    )
    simulate_response(dsa_prompt, 6)
    
    # 6. Interviewee can ask clarifying questions
    simulate_response("Interviewer: Do you have any questions about the problem?", 2)
    clarifying_question = input("You: ")
    simulate_response("Interviewer: Good question! For this problem, assume the array can contain both positive and negative integers, and the length of the array can vary. Does that help?", 4)

    # 7. Interviewee attempts the question
    simulate_response("Interviewer: Alright, go ahead and give it a try. Let me know if you get stuck.", 3)
    interviewee_attempt = input("You (describe your approach): ")

    if "stuck" in interviewee_attempt.lower():
        # 8. If the interviewee gets stuck, the interviewer will give hints
        hint = assistant.run(
            {
                "messages": [
                    {
                        "role": "assistant",
                        "content": "It sounds like you're a bit stuck. Here's a hint: Try using a hashmap to store the cumulative sum at each index. This will allow you to quickly find subarrays that sum to zero."
                    }
                ]
            }
        )
        simulate_response(f"Interviewer: {hint['content']}", 5)
    
    # Simulating the user writing the code and executing it
    code_attempt = input("You (write your code): ")

    # Execute the user's code
    result = execute_user_code(code_attempt)

    # Displaying the result of the code execution
    if isinstance(result, str):
        # If there's an error
        simulate_response(f"Interviewer: Hmm, it seems there's an error in your code: \n{result}", 4)
    else:
        # If the code runs successfully
        simulate_response("Interviewer: Let's see how your code performs... \nThe code ran successfully!", 4)
    
    # Simulating success
    simulate_response("Interviewer: Excellent! It looks like you’ve implemented the solution correctly. Well done!", 4)

    # 9. Congratulation
    simulate_response("Interviewer: Congratulations on solving the problem! You did a great job thinking through the approach and implementing the solution.", 3)

    # 10. Final Q&A
    simulate_response("Interviewer: Now that we're done with the technical part, you have 5 minutes to ask me any questions you may have about the company, the role, or the hiring process.", 4)
    final_questions = input("You: ")

    simulate_response("Interviewer: Those are great questions! At TechCorp, we really value continuous learning and growth. Our team is always here to support each other, and we have regular training sessions to help our engineers stay on top of the latest technologies. The hiring process typically involves a few rounds, including a system design interview and a cultural fit interview. Anything else you'd like to know?", 8)

    # Final goodbyes
    simulate_response("Interviewer: It was great talking to you today. Best of luck with the rest of the interview process!", 3)
    simulate_response("You: Thank you! It was great talking to you too!", 2)

if __name__ == "__main__":
    main()
