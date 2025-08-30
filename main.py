from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from fastapi.staticfiles import StaticFiles
import cv2
import re
import requests
import textretriever
import logoretriever
from foodscraper import my_dict
from fastapi.responses import HTMLResponse
import numpy as np


app = FastAPI()
app.mount("/images", StaticFiles(directory="images"), name="images")
# ✅ Allow frontend to talk to backend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

base_url = "https://world.openfoodfacts.net"
url = f"{base_url}/cgi/search.pl"


def clean_and_split(s: str):
    """Remove periods, strip 'Contains:', and split extra ingredients."""
    if not isinstance(s, str):
        return []
    s = s.replace('.', '')
    if "Contains:" in s:
        main, contains = s.split("Contains:", 1)
        parts = [main.strip()] + [c.strip() for c in contains.split(',')]
    else:
        parts = [s.strip()]
    cleaned = []
    for p in parts:
        if p:
            p = p.strip()
            p = p[0].lower().title() + p[1:] if len(p) > 1 else p.lower().title()
            cleaned.append(p)
    return cleaned

@app.get("/", response_class=HTMLResponse)
async def home():
    return """
    
    
    
    <!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>✅ Ingredient Scanner</title>

  <!-- Google Fonts: Poppins -->
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Poppins:wght@400;600;700&display=swap" rel="stylesheet">

  <style>
    :root {
      --primary-color: #34D399; /* Emerald 400 */
      --secondary-color: #10B981; /* Emerald 500 */
      --background-color: #F3F4F6; /* Gray 100 */
      --text-color: #1F2937; /* Gray 800 */
      --white-color: #FFFFFF;
      --success-color: #22C55E; /* Green 500 */
      --danger-color: #EF4444; /* Red 500 */
      --shadow-color: rgba(0, 0, 0, 0.1);
    }

    body {
      font-family: 'Poppins', sans-serif;
      margin: 0;
      padding: 24px;
      background: linear-gradient(135deg, var(--primary-color), var(--secondary-color));
      color: var(--text-color);
      display: flex;
      flex-direction: column;
      align-items: center;
      min-height: 100vh;
    }

    .container {
      width: 100%;
      max-width: 800px;
      background: var(--white-color);
      border-radius: 24px;
      padding: 24px;
      box-shadow: 0 10px 30px var(--shadow-color);
      text-align: center;
    }

    header {
      font-size: 2rem;
      font-weight: 700;
      color: var(--white-color);
      margin-bottom: 24px;
      text-shadow: 0 2px 4px var(--shadow-color);
    }

    .display-area {
        display: flex;
        gap: 16px;
        justify-content: center;
        margin-bottom: 24px;
    }

    .scanner-interface, .preview-container {
        flex: 1;
        min-width: 0;
        border: 2px dashed #D1D5DB;
        border-radius: 16px;
        padding: 12px;
        /* background-color: #000; */
        position: relative; /* Crucial for label positioning */
        aspect-ratio: 4 / 3;
        display: flex;
        align-items: center;
        justify-content: center;
    }

    .preview-container {
        background-color: var(--background-color);
        display: none;
    }

    .preview-container .placeholder {
        color: #9CA3AF;
        font-weight: 600;
    }
    
    video, img#preview {
      width: 100%;
      height: 100%;
      object-fit: cover;
      border-radius: 12px;
      display: block;
    }

    @media (max-width: 768px) {
        .display-area {
            flex-direction: column;
        }
    }

    /* --- NEW: Label Styles --- */
    .view-label {
        position: absolute;
        top: 8px;
        left: 8px;
        background-color: rgba(20, 20, 20, 0.6);
        color: white;
        padding: 4px 10px;
        border-radius: 20px;
        font-size: 0.8rem;
        font-weight: 600;
        z-index: 10;
        backdrop-filter: blur(4px); /* Frosted glass effect */
        display: flex;
        align-items: center;
        gap: 6px;
    }

    .live-indicator {
        width: 8px;
        height: 8px;
        background-color: var(--danger-color);
        border-radius: 50%;
    }
    /* -------------------------- */

    .button-group {
      display: flex;
      gap: 12px;
      justify-content: center;
      flex-wrap: wrap;
    }

    button, .file-upload-label {
      background: var(--primary-color);
      color: var(--white-color);
      padding: 12px 24px;
      border: none;
      border-radius: 12px;
      font-size: 1rem;
      font-weight: 600;
      cursor: pointer;
      transition: all 0.2s ease-in-out;
      display: inline-flex;
      align-items: center;
      gap: 8px;
    }

    button:hover, .file-upload-label:hover {
      background: var(--secondary-color);
      transform: translateY(-2px);
      box-shadow: 0 4px 10px var(--shadow-color);
    }
    
    button:disabled {
        background-color: #9CA3AF;
        cursor: not-allowed;
        transform: none;
        box-shadow: none;
    }

    input[type="file"] {
      display: none;
    }

    #spinner {
      display: none;
      border: 5px solid #E5E7EB;
      border-top: 5px solid var(--primary-color);
      border-radius: 50%;
      width: 40px;
      height: 40px;
      animation: spin 1s linear infinite;
      margin: 24px auto;
    }

    @keyframes spin {
      0% { transform: rotate(0deg); }
      100% { transform: rotate(360deg); }
    }

    #results {
      text-align: left;
      margin-top: 24px;
    }

    .results-card {
      background: var(--background-color);
      border-radius: 16px;
      padding: 20px;
      margin-top: 16px;
    }

    .results-card h3 {
      margin-top: 0;
      border-bottom: 2px solid #E5E7EB;
      padding-bottom: 8px;
      margin-bottom: 16px;
      display: flex;
      align-items: center;
      gap: 8px;
    }

    .tag-container {
      display: flex;
      flex-wrap: wrap;
      gap: 8px;
    }

    .tag {
      padding: 6px 14px;
      border-radius: 20px;
      font-size: 0.9rem;
      font-weight: 600;
      color: var(--white-color);
      box-shadow: 0 2px 5px var(--shadow-color);
    }

    .tag-safe { background: var(--success-color); }
    .tag-flagged { background: var(--danger-color); display: block; }

    .flagged-item {
        font-weight: 700;
        display: block;
    }

    .flagged-reason {
        font-size: 0.85rem;
        font-weight: 400;
        opacity: 0.9;
        display: block;
        margin-top: 2px;
    }
    
    .error-message {
        background-color: #FECACA;
        color: #991B1B;
        padding: 16px;
        border-radius: 12px;
        margin-top: 20px;
        font-weight: 600;
    }

    .capture-flash {
      position: absolute;
      inset: 8px;
      background: rgba(255,255,255,0.6);
      opacity: 0;
      pointer-events: none;
      transition: opacity 160ms ease;
      border-radius: 12px;
    }
    .capture-flash.visible {
      opacity: 1;
      transition: opacity 120ms linear;
    }

    footer {
      margin-top: 32px;
      font-size: 0.9rem;
      color: var(--white-color);
      opacity: 0.8;
    }

    .test-section {
  background: #E0F2F1; /* A light teal/green to complement the theme */
  border: 2px dashed var(--primary-color);
  border-radius: 16px;
  padding: 20px;
  # margin-top: 24px;
  margin-bottom: 24px;
  text-align: center;
}

.test-section h3 {
  margin-top: 0;
  margin-bottom: 12px;
  color: var(--text-color);
}

.test-section p {
    margin-top: 0;
    margin-bottom: 16px;
    color: #4B5563; /* Gray-600 */
    line-height: 1.5;
}

/* Style for the download button */
.download-button {
  background: var(--secondary-color);
  color: var(--white-color);
  padding: 12px 24px;
  border-radius: 12px;
  font-size: 1rem;
  font-weight: 600;
  cursor: pointer;
  transition: all 0.2s ease-in-out;
  display: inline-flex;
  align-items: center;
  gap: 8px;
  text-decoration: none; /* Remove underline from the link */
}

.download-button:hover {
  background: var(--primary-color);
  transform: translateY(-2px);
  box-shadow: 0 4px 10px var(--shadow-color);
}
/* -------------------------- */
  </style>
</head>
<body>

  <header>🍏 Ingredient Scanner</header>

  <div class="container">
  <!-- New Test Section -->
<div class="test-section">
  <h3>🧪 Test the App</h3>
  <p>
    Don't have a product handy? Download our sample image, then use the 
    "Upload Image" button above to see the scanner in action.
  </p>
  
  <!-- IMPORTANT: Update this href path to match your file's location -->
  <a href="images/doritos.jpg" download="doritos.jpg" class="download-button">
    ⬇️ Download Sample Image
  </a>
</div>
    <div class="display-area">
      <!-- Live Camera View -->
      <div class="scanner-interface">
        <!-- NEW: Live Camera Label -->
        <div class="view-label"><span class="live-indicator"></span>Live Camera</div>
        <video id="video" autoplay playsinline muted></video>
        <div class="capture-flash" id="captureFlash" aria-hidden="true"></div>
      </div>
      <!-- Last Scanned Image Preview -->
      <div class="preview-container" id="previewContainer">
         <!-- NEW: Your Scan Label -->
        <div class="view-label">Your Scan</div>
        <img id="preview" alt="Last capture preview" style="display: none;" />
        <div class="placeholder" id="previewPlaceholder">Your scan will appear here</div>
      </div>
    </div>

    <div class="button-group">
      <button id="snapBtn">📸 Capture Photo</button>
      <label for="file-upload" class="file-upload-label">📂 Upload Image</label>
      <input id="file-upload" type="file" accept="image/*">
    </div>

    <div id="spinner"></div>
    <div id="results" role="alert" aria-live="polite"></div>
  </div>

  <footer>Built with 💚 for healthier choices</footer>

  <script>
    document.addEventListener("DOMContentLoaded", () => {
      const video = document.getElementById('video');
      const preview = document.getElementById('preview');
      const previewContainer = document.getElementById('previewContainer');
      const previewPlaceholder = document.getElementById('previewPlaceholder');
      const snapBtn = document.getElementById('snapBtn');
      const fileInput = document.getElementById('file-upload');
      const spinner = document.getElementById('spinner');
      const resultsDiv = document.getElementById('results');
      const captureFlash = document.getElementById('captureFlash');
      
      # const API_URL = "http://127.0.0.1:8000/analyze";
      const API_URL = "/analyze";


      async function setupCamera() {
        try {
          const stream = await navigator.mediaDevices.getUserMedia({
            video: { facingMode: "environment" }
          });
          video.srcObject = stream;
        } catch (err) {
          console.error("Camera access denied:", err);
          snapBtn.disabled = true;
        }
      }

      setupCamera();

      snapBtn.addEventListener('click', async () => {
        const imageBlob = await captureImageFromVideo();
        if (imageBlob) {
          showPreviewImage(imageBlob);
          triggerFlash();
          analyzeImage(imageBlob, "capture.png");
        }
      });

      fileInput.addEventListener('change', (event) => {
        const file = event.target.files[0];
        if (file) {
          showPreviewImage(file);
          analyzeImage(file, file.name);
        }
      });

      function captureImageFromVideo() {
        const canvas = document.createElement('canvas');
        canvas.width = video.videoWidth || 640;
        canvas.height = video.videoHeight || 480;
        const context = canvas.getContext('2d');
        context.drawImage(video, 0, 0, canvas.width, canvas.height);
        return new Promise(resolve => {
            canvas.toBlob(blob => resolve(blob), 'image/png');
        });
      }

      async function analyzeImage(imageFile, filename) {
        const formData = new FormData();
        formData.append("file", imageFile, filename);

        toggleSpinner(true);
        resultsDiv.innerHTML = '';

        try {
          const response = await fetch(API_URL, {
              method: "POST",
              body: formData
          });

          if (!response.ok) {
              throw new Error("Server response was not OK.");
          }
          
          const data = await response.json();

          if (data.error) {
              throw new Error(data.error);
          }
          
          renderResults(data);

        } catch (err) {
          console.error("Analysis failed:", err);
          resultsDiv.innerHTML = `<div class="error-message">⚠️ Scan Failed. Please re-take the photo, ensuring the image is clear and there is no glare.</div>`;
        } finally {
          toggleSpinner(false);
        }
      }

      function showPreviewImage(imageSource) {
        const imageURL = URL.createObjectURL(imageSource);
        previewContainer.style.display = 'flex';
        previewPlaceholder.style.display = 'none';
        preview.src = imageURL;
        preview.style.display = 'block';
        
        setTimeout(() => URL.revokeObjectURL(imageURL), 30000);
      }

      function triggerFlash() {
        captureFlash.classList.add('visible');
        setTimeout(() => captureFlash.classList.remove('visible'), 120);
      }

      function toggleSpinner(show) {
        spinner.style.display = show ? 'block' : 'none';
      }

      function renderResults(data) {
        const safeIngredients = data.ingredients
            .filter(ing => !data.flagged.some(f => f.ingredient.toLowerCase() === ing.toLowerCase()));

        const safeIngredientsHTML = safeIngredients.length > 0
            ? safeIngredients.map(i => `<span class="tag tag-safe">${i}</span>`).join("")
            : `<p>No other ingredients were identified.</p>`;

        const flaggedIngredientsHTML = data.flagged && data.flagged.length > 0
          ? data.flagged.map(f =>
              `<div class="tag tag-flagged">
                 <span class="flagged-item">${f.ingredient}</span>
                 <span class="flagged-reason"><strong>${f.status}:</strong> ${f.effect}</span>
               </div>`
            ).join("")
          : `<p>No harmful ingredients found. ✅</p>`;

        resultsDiv.innerHTML = `
          <div class="results-card">
            <h3>⚠️ Flagged for Review</h3>
            <div class="tag-container">${flaggedIngredientsHTML}</div>
          </div>
          <div class="results-card">
            <h3>✅ Other Ingredients</h3>
            <div class="tag-container">${safeIngredientsHTML}</div>
          </div>
        `;
      }
    });
  </script>
</body>
</html>




    """

@app.post("/analyze")
async def analyze(file: UploadFile = File(...)):
    print('function ran')
    contents = await file.read()

    # 🔹 Detect brand and product text
    brand = logoretriever.detect_logo(contents)
    frame = cv2.imdecode(
        np.frombuffer(contents, np.uint8), cv2.IMREAD_COLOR
    )
    logo, product = textretriever.extract_text(frame, brand)
    
    print(f"logo: {logo}, product: {product}")

    term = f"{logo} {product}"
    params = {"search_terms": term, "json": 1, "page_size": 10, "cc": "us", "lc": "en"}
    headers = {"User-Agent": "Carscanogen/1.0 (email@example.com)"}
    auth = ("off", "off")

    response = requests.get(url, headers=headers, params=params, auth=auth, timeout=10)
    data = response.json()
    results = data.get("products", [])

    if not results:
        return JSONResponse({"error": "No products found"})

    ingredients = results[0].get("ingredients_text_en", "")

    # 🔹 Parse ingredients
    parts = re.split(r',\s*(?![^()]*\))', ingredients)
    final_list = []
    for item in parts:
        item = item.lower()
        item = item.strip()
        if '(' in item and ')' in item:
            main, inside = re.match(r'^(.*?)\s*\((.*?)\)$', item).groups()
            final_list.extend(clean_and_split(main.strip()))
            subs = [s.strip() for s in inside.split(',')]
            for s in subs:
                if "and/or" in s:
                    final_list.extend([p.strip() for p in re.split(r"\s*and/or\s*", s)])
                else:
                    final_list.extend(clean_and_split(s))
        else:
            if "and/or" in item:
                final_list.extend([p.strip() for p in re.split(r"\s*and/or\s*", item)])
            else:
                final_list.extend(clean_and_split(item))
    final_list = list(set(final_list))
    print(final_list)
    # 🔹 Match against harmful additives
    flagged = []
    for i in final_list:
        i = i.capitalize()
        if i in my_dict:
            flagged.append({
                "ingredient": i,
                "status": my_dict[i]['status'],
                "type": my_dict[i].get('type', ''),
                "effect": my_dict[i]['effect']
            })
    print(flagged)

    return {
        "product": {"logo": logo, "name": product},
        "ingredients": final_list,
        "flagged": flagged or ["No carcinogenic ingredients found"]
    }
