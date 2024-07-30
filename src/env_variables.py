import os

PROJECT_NAME = os.environ["PROJECT_NAME"]
PROJECT_VERSION = os.environ["PROJECT_VERSION"]

PYTHON_VERSION = os.environ["PYTHON_VERSION"]

# GOOGLE_API_KEY = os.environ["GOOGLE_API_KEY"]

LLM_MODEL_CONFIG = {
  "temperature": 0.4,
  "top_p": 0.95,
  "max_output_tokens": 2800,
  "response_mime_type": "text/plain",
}