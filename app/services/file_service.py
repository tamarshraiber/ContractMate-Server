import os
import shutil
import uuid
from app.config.settings import TEMP_DIR

def save_temp_file(file) -> str:
    session_id = str(uuid.uuid4())
    session_path = os.path.join(TEMP_DIR, session_id)
    os.makedirs(session_path, exist_ok=True)
    file_path = os.path.join(session_path, file.filename)
    
    with open(file_path, "wb") as f:
        f.write(file.file.read())
    
    return session_id, file_path

def cleanup_session(session_id: str):
    session_path = os.path.join(TEMP_DIR, session_id)
    if os.path.exists(session_path):
        shutil.rmtree(session_path)
        
