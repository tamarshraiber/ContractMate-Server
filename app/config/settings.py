import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

TEMP_DIR = os.path.join(BASE_DIR,"temp")

VECTOR_DIR = os.path.join(BASE_DIR,"vector_db")

CHUNK_SIZE = 500

SESSION_TIMEOUT = 60 * 30

LLM_MODEL = "llama-3b"

