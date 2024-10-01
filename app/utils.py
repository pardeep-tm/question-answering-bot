"""Utility functions"""

import json
import logging

import PyPDF2
from fastapi import UploadFile, HTTPException


logger = logging.getLogger(__name__)
   
def extract_text_from_pdf(pdf_file: UploadFile) -> str:
    text = ""
    try:
        pdf_reader = PyPDF2.PdfReader(pdf_file.file)
        for page_num in range(len(pdf_reader.pages)):
            page = pdf_reader.pages[page_num]
            text += page.extract_text()
        return text
    except Exception as e:
        logger.error(f"Error processing PDF: {e}")
        raise HTTPException(status_code=500, detail=f"Error processing PDF: {str(e)}")


def extract_text_from_json(json_file: UploadFile) -> str:
    try:
        json_content = json.load(json_file.file).get("content", "")
        return json.dumps(json_content)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error processing JSON: {str(e)}")