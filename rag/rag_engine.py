def get_answer_from_chunks(query: str, chunks: list, history: list = []):
    """
    history: רשימת QA קודמות כדי לתת זרימה הגיונית לשיחה
    chunks: הטקסטים של החוזה
    """
    # כרגע mock
    # בעתיד כאן תתחברי ל-LLM או למודל פנימי
    context_info = f"{len(chunks)} chunks, history length: {len(history)}"
    response = f"זו תשובה לדוגמה על השאלה: '{query}' ({context_info})"
    return response