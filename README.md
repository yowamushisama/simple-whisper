# FastAPI Transcription Service

This project provides a FastAPI-based service to transcribe audio or video files using the Whisper model.

## Installation

1. Clone the repository:
2. 
    git clone https://github.com/yowamushisama/simple-whispere.git
    cd fastapi-transcription-service


3. Install the required packages:
 
    pip install -r requirements.txt
 
## Running the Application

Start the FastAPI server:

uvicorn app:app --reload

Using the API
Uploading a File for Transcription
You can upload an audio or video file to the /transcribe/ endpoint.

Using Swagger UI
Open http://127.0.0.1:8000/docs in your web browser.
Find the /transcribe/ endpoint.
Click "Try it out".
Select your audio or video file.
Click "Execute".
