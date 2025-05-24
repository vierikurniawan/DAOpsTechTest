# BFI Finance - DA Operation - Tech Test
## 🍷 Wine Quality Prediction
### ⚙️ Setup Instructions
- With Git:
  
  1️⃣ Clone this repository
  ```bash
  git clone https://github.com/vierikurniawan/DAOpsTechTest.git
  cd DAOpsTechTest 
  ```
  2️⃣ Install dependencies
  ```bash
  pip install -r requirements.txt
  ```
- Without Git:

  1️⃣ Download this repository
  - Download the ZIP File of this Repository
  - Extract the ZIP File
  - Open the extracted folder
    
  2️⃣ Install dependencies
  ```bash
  pip install -r requirements.txt
  ```
### 🏗 How to Run the Model & API
  1️⃣ Run the API
  ```bash
  uvicorn app:app --reload
  ```
  2️⃣ Predict with the Model
  - Using Swagger UI (API testing UI):
    - Open http://127.0.0.1:8000/docs
    - Select the `/predict` endpoint
    - Click "Try it out"
    - Input the 11 wine features to predict the wine quality
    ```bash
    feature_names = [
    'fixed acidity', 'volatile acidity', 'citric acid', 'residual sugar',
    'chlorides', 'free sulfur dioxide', 'total sulfur dioxide',
    'density', 'pH', 'sulphates', 'alcohol'
    ]
    ```
    - Execute the request
      
  - Using Python:
    - Open the file `test_api.py`
    - Input the 11 wine features to predict the wine quality
    ```bash
    feature_names = [
    'fixed acidity', 'volatile acidity', 'citric acid', 'residual sugar',
    'chlorides', 'free sulfur dioxide', 'total sulfur dioxide',
    'density', 'pH', 'sulphates', 'alcohol'
    ]
    ```
    - Run the file
    ```bash
    python test_api.py
    ```
### 📊 Monitoring Dashboard
This dashboard was built with Grafana & Prometheus and consists of 2 visualizations, showing:
- Prediction count/rate
- API response time/latency
  
![Monitoring Report](https://github.com/user-attachments/assets/f813f778-d382-4b95-9de6-34ef670f7bd3)
