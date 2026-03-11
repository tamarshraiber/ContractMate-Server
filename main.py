# FastAPI app, endpoints

# main.py
from fastapi import FastAPI, File, UploadFile, Body
from utils.file_handler import save_uploaded_file
from utils.text_extraction import extract_text_from_pdf, extract_text_from_docx
from utils.text_splitter import split_text_into_chunks


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

    return {
        "message": "File uploaded successfully",
        "path": file_path,
        "extracted_text": text,
        "chunks_count": len(chunks)
    }

# --------------------------
# Endpoint 2: Query / שאילתה על החוזה
# --------------------------
@app.post("/query")
async def query_contract(query: str = Body(...)):
    """
    מקבל שאילתא מהמשתמש, לדוגמה:
    "האם החוזה הזה הוגן?"
    
    בשלב זה נשתמש ב-mock response
    כדי לבדוק את ה-flow.
    """
    # TODO: כאן נתחבר ל-RAG + OLLAMA
    mock_response = f"זו תשובה לדוגמה על השאלה: '{query}'"
    
    return {"answer": mock_response}

# --------------------------
# להרצה מקומית:
# uvicorn main:app --reload
# --------------------------