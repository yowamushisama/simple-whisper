from fastapi import FastAPI, UploadFile, File, HTTPException
import whisper
import os
import logging
import time

app = FastAPI()

model = whisper.load_model("base")

WORKING_DIR = "working_dir"
os.makedirs(WORKING_DIR, exist_ok=True)

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def process_transcription(file_path: str) -> str:
    try:
        start_time = time.time()
        logging.info(f"Starting transcription for file: {file_path}")

        result = model.transcribe(file_path, language='en')
        transcription = result["text"]

        end_time = time.time()
        processing_time = end_time - start_time
        logging.info(f"Transcription completed in {processing_time:.2f} seconds")

        return transcription, processing_time
    except Exception as e:
        logging.error(f"Error during transcription: {e}", exc_info=True)
        raise HTTPException(status_code=500, detail=f"Error during transcription: {str(e)}")
    finally:
        if os.path.exists(file_path):
            os.remove(file_path)

@app.post("/transcribe/")
async def transcribe(file: UploadFile = File(...)):
    file_path = os.path.join(WORKING_DIR, file.filename)

    try:
        with open(file_path, "wb") as buffer:
            buffer.write(await file.read())

        transcription, transcription_time = process_transcription(file_path)

        return {
            "message": "Transcription completed",
            "transcription": transcription,
            "transcription_time": transcription_time
        }

    except Exception as e:
        logging.error(f"Error during file processing: {str(e)}", exc_info=True)
        if os.path.exists(file_path):
            os.remove(file_path)
        raise HTTPException(status_code=500, detail=f"Error during file processing: {str(e)}")
