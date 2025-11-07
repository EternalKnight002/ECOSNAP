from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import pandas as pd
import joblib
from fastapi.middleware.cors import CORSMiddleware

# --- 1. Initialize App & Load Model ---
app = FastAPI(title="EcoSnap AI Backend")

# Allow your React frontend to talk to this backend (CORS)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], # Allows all origins (for hackathon simplicity)
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Load the trained model
# NOTE: Ensure 'eco_snap_model.pkl' is in the SAME folder as this script.
try:
    model = joblib.load('eco_snap_model.pkl')
    print("✅ Model loaded successfully!")
except FileNotFoundError:
    print("❌ ERROR: eco_snap_model.pkl not found. Please make sure it is in this folder.")

# --- 2. Define Input Data Format ---
# This is what the frontend MUST send us
class WasteInput(BaseModel):
    material: str  # e.g., "Plastic", "Glass", "Paper"

# --- 3. API Endpoints ---
@app.get("/")
def home():
    return {"message": "EcoSnap AI is awake and ready! 🌿"}

@app.post("/predict")
def predict_impact(data: WasteInput):
    try:
        # 1. Convert incoming JSON to a pandas DataFrame (what the model expects)
        # Strips spaces and Capitalizes first letters (e.g., " plastic " -> "Plastic")
        cleaned_material = data.material.strip().title()
        input_df = pd.DataFrame({'Material': [cleaned_material]})

        # 2. Run prediction
        # Result is an array: [[co2, recyclability, total_score]]
        prediction = model.predict(input_df)

        # 3. Format the results nicely for the frontend
        return {
            "input_material": data.material,
            "co2_emissions_kg": round(prediction[0][0], 2),
            "recyclability_score": round(prediction[0][1], 2),
            # We optionally include a simple interpretation text
            "impact_rating": "High" if prediction[0][0] > 10 else "Low/Moderate"
        }

    except Exception as e:
        # If something goes wrong (e.g., material not recognized perfectly), send an error
        raise HTTPException(status_code=500, detail=str(e))