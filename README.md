# 🌿 EcoSnap Insight

**AI-Powered Waste Impact Analytics for Conscious Consumers**

Transform waste management decisions with instant, data-driven environmental insights. EcoSnap Insight uses machine learning to predict CO₂ emissions and recyclability scores for any material, helping you understand the true cost of what you discard.

---

## ✨ Features

- **AI-Powered Predictions** – Machine learning model instantly analyzes waste materials
- **CO₂ Footprint Analysis** – Get accurate carbon emission estimates (kg CO₂ per unit)
- **Recyclability Intelligence** – Understand how recyclable each material truly is
- **Impact Scoring** – Automatic environmental impact rating (High/Low/Moderate)
- **Minimal & Fast** – Zero external dependencies, pure vanilla JavaScript frontend
- **Real-Time Results** – Sub-second response times with FastAPI backend
- **Dark Mode UI** – Modern, eco-themed interface designed for usability

---

## 🏗️ Architecture

```
┌─────────────────────────────────────────────────────────┐
│                    Frontend (Client)                     │
│         HTML5 + CSS3 + Vanilla JavaScript                │
│          (No frameworks, no build steps)                 │
└──────────────────────┬──────────────────────────────────┘
                       │ FETCH requests
                       ▼
┌─────────────────────────────────────────────────────────┐
│                   FastAPI Backend                        │
│          Python 3.9+ | Scikit-learn | Pandas            │
└──────────────────────┬──────────────────────────────────┘
                       │ Model Inference
                       ▼
┌─────────────────────────────────────────────────────────┐
│           Machine Learning Model                         │
│      RandomForestRegressor (50 estimators)              │
│   Trained on Sustainability Dataset                     │
└─────────────────────────────────────────────────────────┘
```

---

## 🚀 Quick Start

### Prerequisites
- Python 3.9 or higher
- Modern web browser (Chrome, Firefox, Edge, Safari)

### 1️⃣ Setup Backend

Clone the repository and navigate to the project directory:

```bash
git clone https://github.com/yourusername/ecosnap-insight.git
cd ecosnap-insight
```

Install dependencies:

```bash
pip install fastapi uvicorn pandas scikit-learn joblib
```

Start the FastAPI server:

```bash
uvicorn main:app --reload
```

**Windows users with PATH issues?** Use:
```bash
python -m uvicorn main:app --reload
```

You'll see: `INFO: Uvicorn running on http://127.0.0.1:8000` ✅

### 2️⃣ Launch Frontend

Simply open `index.html` in your browser. That's it!

The app will automatically connect to your local backend and you're ready to start analyzing waste materials.

---

## 📊 How It Works

1. **Enter a Material** – Type any waste material (e.g., "Plastic", "Glass", "Paper", "Metal")
2. **Model Processes Input** – Your input is one-hot encoded and fed through the Random Forest model
3. **Get Instant Results** – View CO₂ emissions, recyclability percentage, and impact rating
4. **Make Better Decisions** – Use these insights to choose sustainable disposal options

### Example Output
```
Material: Plastic

☁️ CO₂ Emissions: 15.34 kg
♻️ Recyclability: 65%
⚠️ Overall Impact: High
```

---

## 🧠 Model Details

- **Algorithm:** Random Forest Regressor (50 trees)
- **Input Feature:** Material type (categorical)
- **Output Predictions:** 
  - CO₂ emissions per kg
  - Recyclability score (0-1)
  - Total sustainability score
- **Encoding:** One-Hot Encoding for categorical material types
- **Framework:** Scikit-learn pipeline for reproducibility

---

## 🔄 Retraining the Model

Want to improve predictions with your own data? Here's how:

1. **Prepare your dataset** – Create a CSV file named `sustainability_dataset.csv` with columns:
   ```csv
   Material,CO2_per_kg,Recyclability_Score,Total_Sustainability_Score
   Plastic,15.34,0.65,0.55
   Glass,2.10,0.95,0.80
   ...
   ```

2. **Run the training script:**
   ```bash
   python train_local.py
   ```

3. **Done!** The new `eco_snap_model.pkl` will be automatically loaded by your backend on restart.

---

## 📁 Project Structure

```
ecosnap-insight/
├── index.html                      # Frontend UI
├── main.py                         # FastAPI backend
├── train_local.py                  # Model training script
├── eco_snap_model.pkl              # Pre-trained ML model
├── sustainability_dataset.csv      # Training data (optional)
└── README.md                       # This file
```

---

## 🔌 API Reference

### POST `/predict`

Predict the environmental impact of a material.

**Request:**
```json
{
  "material": "Plastic"
}
```

**Response:**
```json
{
  "input_material": "Plastic",
  "co2_emissions_kg": 15.34,
  "recyclability_score": 0.65,
  "impact_rating": "High"
}
```

### GET `/`

Health check endpoint.

**Response:**
```json
{
  "message": "EcoSnap AI is awake and ready! 🌿"
}
```

---

## 🎨 Frontend Highlights

- **Responsive Design** – Works seamlessly on desktop, tablet, and mobile
- **Accessible UI** – High contrast dark mode, clear typography
- **Real-time Feedback** – Button states, loading indicators, smooth animations
- **Error Handling** – User-friendly error messages for failed predictions
- **Keyboard Support** – Press Enter to submit queries

---

## 🛣️ Future Improvements

- [ ] **Image Recognition** – Snap photos of waste and auto-detect material type
- [ ] **Barcode Integration** – Scan UPC codes for product-specific data
- [ ] **Advanced Analytics** – Track impact trends and statistics
- [ ] **Export Reports** – Download detailed impact analyses
- [ ] **Multi-Material Analysis** – Analyze waste composition impact

---

## 📜 License

This project is licensed under the MIT License – see the [LICENSE](LICENSE) file for details.
