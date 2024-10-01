# Question Answering Bot using Langchain and OpenAI

- [Introduction](#introduction)
- [Tools Used](#tools-used)
- [Getting Started](#getting-started)

## Introduction

This project implements a custom question-answering chatbot powered by LangChain and provides an API via FastAPI for access.

## Tools Used

- [Langchain](https://link-to-langchain): Framework for building conversational AI systems.
- [FastAPI](https://fastapi.tiangolo.com/): FastAPI is a modern, fast (high-performance), web framework for building APIs with Python

## Getting Started

To run the project locally, follow these steps:

1. Clone the repository to your local machine.
2. Install the necessary dependencies listed in the `requirements.txt` file.
3. Run the application by executing `uvicorn app.main:app --port {} --reload` in your terminal.
4. The `/qa` endpoint needs to be passed two files as an input.
    1. a JSON file containing a list of questions that needs to be answered using LLM. e.g. `{"questions": ["question1", "question2" ...]}`
    2. a JSON or PDF having the content over which questions need to be answered. In case of a JSON file, it must have a content like this `{"content": "long piece of text ..."}`
5. Use the sample input files located in the `tests` folder to test the API.