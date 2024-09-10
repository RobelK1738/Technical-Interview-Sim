#!/bin/bash


pip3 install requirements.txt

# Check if OPENAI_API_KEY is set
if [ -z "$OPENAI_API_KEY" ]; then
    # If OPENAI_API_KEY is not set, export the value
    export OPENAI_API_KEY="sk-IcZSPnqo7v8mbaiE5w3bg0tx1YSV_oUPIDZYrABAcMT3BlbkFJp5wYx99-JmF0CdZVdqaFKljQMlCrkSXsSNHWg3HE4A"
    echo "OPENAI_API_KEY was not set, exporting a new key."
fi

# Ensure streamlit is run if the key is set
echo "Running streamlit.py"
streamlit run streamlit.py
