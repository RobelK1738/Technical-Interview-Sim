import os

api_key = os.environ.get("OPENAI_API_KEY")
if api_key:
    print("API Key:", api_key)
else:
    print("API Key not found")
