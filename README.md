---
title: Food Ingredient Scanner
emoji: 🍔
colorFrom: blue
colorTo: green
sdk: python
python_version: "3.11"
suggested_hardware: "t4-medium"  # GPU for PaddleOCR inference
suggested_storage: "small"     # enough for models + a few images
app_file: main.py
pinned: false
short_description: "Scan food images to detect ingredients and flag harmful additives"
tags: ["OCR", "FastAPI", "Food", "Ingredients", "Health"]
preload_from_hub:
  - paddleocr/models/ch_ppocr_server_v2.0  # Preload PaddleOCR model to speed up startup
---

Check out the configuration reference at https://huggingface.co/docs/hub/spaces-config-reference


# Food Ingredient Scanner


A web-based AI application that scans food product images, identifies ingredients using external databases, and flags potentially harmful additives to promote healthier consumer choices.



## 📋 Table of Contents

- [Food Ingredient Scanner](#food-ingredient-scanner)
  - [📋 Table of Contents](#-table-of-contents)
  - [✨ Features](#-features)
  - [⚙️ How It Works](#️-how-it-works)
  - [🛠️ Tech Stack](#️-tech-stack)
  - [🚀 Setup and Installation](#-setup-and-installation)
    - [Prerequisites](#prerequisites)
    - [1. Clone the Repository](#1-clone-the-repository)
    - [2. Set Up Google Cloud Credentials](#2-set-up-google-cloud-credentials)
    - [3. Create a `requirements.txt` File](#3-create-a-requirementstxt-file)
    - [4. Set Up a Virtual Environment \& Install Dependencies](#4-set-up-a-virtual-environment--install-dependencies)
  - [▶️ Running the Application](#️-running-the-application)
  - [📁 Project Structure](#-project-structure)
  - [🔮 Future Improvements](#-future-improvements)

---

## ✨ Features

-   **Live Camera Capture**: Scan products in real-time using your device's camera.
-   **Image Upload**: Analyze existing photos of food products.
-   **AI-Powered Recognition**:
    -   Uses **Google Cloud Vision** to accurately detect brand logos.
    -   Uses **PaddleOCR** to extract product names and other text from the image.
-   **Comprehensive Ingredient Data**: Integrates with the [Open Food Facts API](https://world.openfoodfacts.org/) to retrieve detailed ingredient lists.
-   **Harmful Ingredient Flagging**: Cross-references ingredients against a curated dictionary of additives with potential health concerns.
-   **User-Friendly Interface**: A clean, responsive, and intuitive single-page application that clearly separates safe and flagged ingredients.

---

## ⚙️ How It Works

The application follows a simple yet powerful workflow:

1.  **Image Input**: The user captures a photo with their camera or uploads an image file via the frontend.
2.  **Backend Processing**: The image is sent to the FastAPI backend.
3.  **Logo & Text Extraction**:
    -   `logoretriever.py` sends the image to the Google Cloud Vision API to identify the product's brand (e.g., "Lay's", "Coca-Cola").
    -   `textretriever.py` uses PaddleOCR to read the text on the product, identifying the product name (e.g., "Classic", "Diet Coke").
4.  **Data Retrieval**: The backend queries the Open Food Facts API with the combined brand and product name (e.g., "Lay's Classic").
5.  **Ingredient Parsing**: The application retrieves the ingredients string from the API response and intelligently parses it into a clean list.
6.  **Analysis**: Each ingredient is checked against the dictionary in `foodscraper.py`. Any matches are added to a "flagged" list.
7.  **Response**: The backend sends a JSON object to the frontend containing the product name, the full ingredient list, and the list of flagged ingredients with their associated health concerns.
8.  **Display**: The frontend dynamically renders the results in a clear, color-coded format.

---

## 🛠️ Tech Stack

-   **Backend**: Python 3.9+
    -   **Framework**: FastAPI
    -   **AI / Machine Learning**: Google Cloud Vision API, PaddleOCR
    -   **API Communication**: Requests
    -   **Image Processing**: OpenCV, NumPy
    -   **WSGI Server**: Uvicorn
-   **Frontend**:
    -   HTML5
    -   CSS3 (Modern, responsive design)
    -   Vanilla JavaScript (for camera access, API calls, and DOM manipulation)

---

## 🚀 Setup and Installation

### Prerequisites

-   Python 3.9 or higher.
-   A Google Cloud Platform (GCP) account with the **Cloud Vision API** enabled.
-   Git.

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/your-repo-name.git
cd your-repo-name
```

### 2. Set Up Google Cloud Credentials

To use the logo detection feature, you must authenticate with Google Cloud.

1.  In your GCP project, create a **Service Account**.
2.  Assign the **Cloud Vision AI User** role to the service account.
3.  Create a **JSON key** for this service account and download it to your computer.
4.  Set an environment variable that points to the path of this JSON key file.

    -   **On macOS / Linux:**
        ```bash
        export GOOGLE_APPLICATION_CREDENTIALS="/path/to/your/keyfile.json"
        ```
    -   **On Windows (Command Prompt):**
        ```bash
        set GOOGLE_APPLICATION_CREDENTIALS="C:\path\to\your\keyfile.json"
        ```
     **Important**: This variable must be set in the terminal session where you will run the application.

### 3. Create a `requirements.txt` File

Create a file named `requirements.txt` in the root directory and add the following dependencies:

```
fastapi
uvicorn[standard]
google-cloud-vision
paddleocr
paddlepaddle
requests
python-multipart
numpy
opencv-python-headless
rapidfuzz
langdetect
```

### 4. Set Up a Virtual Environment & Install Dependencies

It is highly recommended to use a virtual environment.

```bash
# Create a virtual environment
python -m venv venv

# Activate the virtual environment
# On macOS / Linux:
source venv/bin/activate
# On Windows:
venv\Scripts\activate

# Install the required packages
pip install -r requirements.txt
```

---

## ▶️ Running the Application

1.  **Start the Backend Server**:
    With your virtual environment activated, run the following command from the project's root directory:

    ```bash
    uvicorn main:app --reload
    ```
    The `--reload` flag automatically restarts the server when you make changes to the code.

2.  **Access the Frontend**:
    The application is now running. Open your web browser and navigate to:

    [http://127.0.0.1:8000](http://127.0.0.1:8000)

---

## 📁 Project Structure

```
.
├── images/
│   └── monster-ingredients.jpg  # Sample image for testing
│
├── main.py                # FastAPI server, API endpoints, and frontend HTML
├── logoretriever.py       # Handles logo detection with Google Cloud Vision
├── textretriever.py       # Handles text extraction with PaddleOCR
├── foodscraper.py         # Contains the dictionary of harmful ingredients
├── carcinogens.py         # (Optional) Additional data for harmful ingredients
├── README.md              # This file
└── requirements.txt       # Python dependencies
```

---

## 🔮 Future Improvements

-   **Database Integration**: Replace the hardcoded Python dictionary of harmful ingredients with a scalable database (e.g., PostgreSQL, MongoDB) for easier management.
-   **User Accounts**: Allow users to create accounts to save their scan history and set personal dietary restrictions or allergies for custom flagging.
-   **Barcode Scanning**: Implement barcode scanning as a faster, more reliable alternative to image recognition for identifying products.
-   **Expanded Ingredient Information**: Link flagged ingredients to external sources or provide more detailed pop-ups explaining the health concerns.
