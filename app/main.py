"""Entry point to the API application"""

from fastapi import FastAPI, UploadFile, File, HTTPException
from pydantic import BaseModel
from typing import List
import json

from .llms import generate_answers
from .utils import extract_text_from_json, extract_text_from_pdf

app = FastAPI()


@app.post("/qa")
async def question_answering(
    questions_file: UploadFile = File(...),
    document_file: UploadFile = File(...)
):
    """
    API to handle question answering using Langchain as the backend LLM framework.

    Args:
        questions_file: JSON file containing questions.
        document_file: JSON or PDF file having content over which questions need to be answered.
    
    Returns:
        JSONResponse: Returns a JSON data with questions and valid answers if any.
    """
    # process the questions
    if questions_file.content_type == "application/json":
        questions = json.load(questions_file.file).get("questions", [])
    else:
        raise HTTPException(status_code=400, detail="Questions file must be in JSON format.")

    if not questions:
        raise HTTPException(status_code=400, detail="No questions provided.")

    # process the document (PDF or JSON)
    if document_file.content_type == "application/pdf":
        document_text = extract_text_from_pdf(document_file)
    elif document_file.content_type == "application/json":
        document_text = extract_text_from_json(document_file)
    else:
        raise HTTPException(status_code=400, detail="Document must be either PDF or JSON format.")

    # generate answers using Langchain
    answers = generate_answers(document_text, questions)

    return answers
