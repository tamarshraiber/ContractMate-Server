import uuid
import time
from typing import Dict

#temporary store
session_store: Dict[str,dict]={}  # session_id -> {"chunks": [...], "file_name": str, "history": [] , "timestamp": float}

SESSION_TIMEOUT =3600 # 1 HOUR

def create_session(chunks: list,file_name: str)->str:
    session_id = str(uuid.uuid4())
    session_store[session_id] = {
        "chunks" :chunks,
        "file_name":file_name,
        "history":[],
        "timestamp":time.time()
    }

    return session_id

def get_session(session_id: str)->dict:
    session =session_store.get(session_id)
    if not session:
        return None
    session["timestamp"] = time.time()
    return session

def delete_session(session_id: str):
    session_store.pop(session_id, None)

def cleanup_expired_sessions():
    now = time.time()
    expired= [
        sid for sid, data in session_store.items()
        if now -data.get("timestamp",now)>SESSION_TIMEOUT
    ]    
    for sid in expired:
        delete_session(sid)