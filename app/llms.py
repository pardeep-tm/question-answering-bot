"""Module to hold functionality related to Langchain methods"""

import logging
from typing import List

from langchain.chains import AnalyzeDocumentChain
from langchain_openai import ChatOpenAI
from langchain.chains.question_answering import load_qa_chain

from app.config_settings import settings

logger = logging.getLogger(__name__)


def generate_answers(document_text: str, questions: List[str]) -> dict:
    """
    Generate answers based on the given text using Langchain

    Args:
        document_text (str): The document over which questions need to be answered.
        questions (List[str]): The list of questions need to be answered using LLM.

    Returns:
        dict: Questions and their answers
    """
    try:
        llm = ChatOpenAI(model=settings.LLM_MODEL or "gpt-4o-mini", temperature=0, api_key=settings.OPENAI_API_KEY)
        qa_chain = load_qa_chain(llm, chain_type="map_reduce")
        qa_document_chain = AnalyzeDocumentChain(combine_docs_chain=qa_chain)
    except Exception as exc:
        logger.error(f"Error in chain initiation in Langchain: {exc}")
        return {}
    
    # Iterate through each question and get an answer
    answers = {}
    for question in questions:
        try:
            answer = qa_document_chain.run(
                input_document=document_text,
                question=question
            )
            answers[question] = answer.strip()
        except Exception as exc:
            logger.error(f"Error in running qa chain for question: {question}, error: {exc}")
            answers[question] = ""
    
    return answers