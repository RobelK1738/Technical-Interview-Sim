#!/bin/bash
# conda activate autogenstudio

# Check if OPENAI_API_KEY is set
if [ -z "$OPENAI_API_KEY" ]; then
    # If OPENAI_API_KEY is not set, export the value
    export OPENAI_API_KEY="API_KEY"
    echo "OPENAI_API_KEY was not set, exporting a new key."
fi


autogenstudio ui