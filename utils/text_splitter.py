 # חלוקת טקסט ל-chunks
# utils/text_splitter.py

def split_text_into_chunks(text, chunk_size=500, overlap=50):
    """
    מחלק טקסט גדול ל-chunks.
    chunk_size: כמה תווים בכל חלק
    overlap: כמה תווים חופפים בין חלק לחלק
    """

    chunks = []
    start = 0
    text_length = len(text)

    while start < text_length:
        end = start + chunk_size
        chunk = text[start:end]
        chunks.append(chunk)
        start = end - overlap  # overlap קטן כדי שהקשר לא יתפסק

    return chunks