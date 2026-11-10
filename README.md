# Asistente Contingencia - Clinical Workflow Assistant

A production-ready assistive web platform designed to streamline clinical note recording, transcription, and structured document formatting during operational contingencies in primary healthcare environments.

## Architecture & Tech Stack
- Language: Python 3.10+
- Framework: Streamlit Community Framework
- Core Processing: Audio-to-text processing pipeline, asynchronous I/O handling, and LLM text formatting APIs.
- Output Generation: Structured document compilation (python-docx).
- Deployment: Streamlit Cloud / Docker containerization.

## Key Features
- Voice Transcription Integration: Real-time audio recording interface for medical and administrative staff.
- Automated Field Structuring: Converts unorganized clinical audio inputs into normalized health record contingency forms.
- Validation Pipeline: Data integrity checks prior to rendering exportable outputs.

## Local Development Setup

1. Clone the repository:
   git clone https://github.com/patricio2306/asistente-contingencia.git
   cd asistente-contingencia

2. Create and activate a virtual environment:
   python -m venv venv
   source venv/bin/activate

3. Install dependencies:
   pip install -r requirements.txt

4. Run application:
   streamlit run app.py

## Roadmap & Current Work in Progress
- Migrate local transcription buffers to asynchronous streaming workers.
- Implement end-to-end unit tests using pytest for output parsers.
- Containerize application via multi-stage Dockerfile for decoupled microservice deployment.
