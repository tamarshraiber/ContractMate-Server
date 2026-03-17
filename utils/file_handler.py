# שמירה וקבלת קבצים
import os
import shutil

TEMP_DIR = "temp"

# אם התיקייה לא קיימת – ליצור אותה
os.makedirs(TEMP_DIR, exist_ok=True)

def save_uploaded_file(upload_file):
    """
    שומר קובץ שהגיע מהמשתמש
    ומחזיר את הנתיב שלו
    """

    file_path = os.path.join(TEMP_DIR, upload_file.filename)

    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(upload_file.file, buffer)

    return file_path