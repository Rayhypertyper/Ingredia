Check out the configuration reference at https://huggingface.co/docs/hub/spaces-config-reference
# Ingredient Scanner (Food-app)

Small FastAPI backend + browser frontend to capture or upload product images,
extract text with OCR, optionally detect brand logos, lookup ingredients on
OpenFoodFacts, and flag additives of concern.

Features
- Capture from camera or upload image
- OCR-based ingredient extraction (PaddleOCR)
- Optional logo detection via Google Vision
- Lookup product ingredients on OpenFoodFacts
- Flag known additives from local dataset

Quick start
Prerequisites: Python 3.11+, pip

Clone and enter project
git clone <repo-url>
cd Food-app

Create virtualenv and install
python -m venv .venv
.venv\Scripts\Activate.ps1  # PowerShell
pip install -r requirements.txt

Run server (development)
uvicorn main:app --reload --host 0.0.0.0 --port 8000
Open http://127.0.0.1:8000/ or open test.html locally

Configuration
- If using Google Vision set GOOGLE_APPLICATION_CREDENTIALS
- For local frontend opened via file:// set API_URL to http://127.0.0.1:8000/analyze
- If served by FastAPI use relative API URL "/analyze"

API
POST /analyze accepts multipart/form-data with field "file"
Response includes product, ingredients, and flagged arrays

Debugging tips
- Check browser DevTools → Console/Network for permission or fetch errors
- Watch uvicorn logs for exceptions from OCR or network calls
- Test with curl: curl -F "file=@images/doritos.jpg" http://127.0.0.1:8000/analyze

Deployment
- A Dockerfile is provided for containerized hosting (adjust PORT env)
- For Hugging Face Spaces use the provided Hugging Face readme front-matter

Contributing
- Open issues or PRs; add tests for new parsing logic
- License: MIT (add LICENSE file)

Check out the configuration reference at https://huggingface.co/docs/hub/spaces-config-reference
