import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
import joblib

# 1. Load Data (Locally now!)
try:
    df = pd.read_csv('sustainability_dataset.csv')
    print("✅ Dataset found!")
except FileNotFoundError:
    print("❌ ERROR: 'sustainability_dataset.csv' not found in this folder.")
    exit()

# 2. Setup
X = df[['Material']]
y = df[['CO2_per_kg', 'Recyclability_Score', 'Total_Sustainability_Score']]

# 3. Build Pipeline
preprocessor = ColumnTransformer(
    transformers=[('cat', OneHotEncoder(handle_unknown='ignore'), ['Material'])])
model_pipeline = Pipeline(steps=[
    ('preprocessor', preprocessor),
    ('regressor', RandomForestRegressor(n_estimators=50, random_state=42))
])

# 4. Train & Save
print("🤖 Training local model...")
model_pipeline.fit(X, y)
joblib.dump(model_pipeline, 'eco_snap_model.pkl')
print("✅ SUCCESS! New 'eco_snap_model.pkl' created locally.")