# FastAPI app, endpoints

# main.py
from fastapi import FastAPI, File, UploadFile, Body, HTTPException
from utils.file_handler import save_uploaded_file
from utils.text_extraction import extract_text_from_pdf, extract_text_from_docx
from utils.text_splitter import split_text_into_chunks
from session_manager import create_session ,get_session, cleanup_expired_sessions
from rag.rag_engine import get_answer_from_chunks
import asyncio


# כאן ניצור את האפליקציה
app = FastAPI()


# --------------------------
# Endpoint 1: Upload קובץ
# --------------------------
@app.post("/upload")
async def upload_file(file: UploadFile = File(...)):

    file_path = save_uploaded_file(file)

    # חילוץ טקסט
    if file.filename.endswith(".pdf"):
        text = extract_text_from_pdf(file_path)
    elif file.filename.endswith(".docx"):
        text = extract_text_from_docx(file_path)
    else:
        text = ""

    # חלוקה ל-chunks
    chunks = split_text_into_chunks(text)

    # create session
    session_id = create_session(chunks, file.filename)

    return {
        "message": "File uploaded successfully",
        "session_id": session_id,
        "chunks_count": len(chunks)
    }

# --------------------------
# Endpoint 2: Query / שאילתה על החוזה
# --------------------------
@app.post("/query")
async def query_contract(
    session_id: str =Body(...),
    query: str = Body(...)
):
    session = get_session(session_id)
    if not session:
        raise HTTPException(status_code=404, detail="Session expired or file not uploaded")

    answer = get_answer_from_chunks(query,session["chunks"], session["history"])
    session["history"].append({"query":query, "answer":answer})


    return {"answer": answer}


@app.on_event("startup")
async def start_cleanup_task():
    async def cleanup_loop():
        import time
        while True:
            cleanup_expired_sessions()
        await asyncio.sleep(600) #every 10 minutes 
    asyncio.create_task(cleanup_loop)       

# --------------------------
# להרצה מקומית:
# uvicorn main:app --reload
# --------------------------