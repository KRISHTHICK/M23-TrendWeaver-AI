# M23-TrendWeaver-AI
GenAI

### 🧵 New Fashion AI Project: **TrendWeaver AI – Fabric Pattern Classifier & Outfit Composer**

**📌 Description:**
TrendWeaver AI is an image-based Streamlit app that:

* Detects common fabric patterns from uploaded outfit images.
* Suggests outfit items based on the predicted pattern.
* Generates downloadable PDF lookbooks.
* Tracks and visualizes the most frequent patterns seen in a session.

---

### 🧠 Features:

* Upload 1-3 fabric or outfit images.
* Predicts one of 5 popular patterns (floral, striped, solid, polka dots, checked).
* Shows style suggestions per pattern.
* PDF Lookbook download for each pattern.
* Real-time bar chart of pattern frequency.

---

### 🛠 How to Run in VS Code & GitHub:

1. **Clone or Download:**

   ```bash
   git clone https://github.com/your-username/TrendWeaver-AI.git
   cd TrendWeaver-AI
   ```

2. **Install dependencies (without virtual environment):**

   ```bash
   pip install -r requirements.txt
   ```

3. **Run the Streamlit App:**

   ```bash
   streamlit run app.py
   ```

---

### 📦 `requirements.txt`:

```txt
streamlit
Pillow
fpdf
matplotlib
```

---

### ✅ Additional Ideas:

* Add actual ML model for pattern classification.
* Store user session results in a database.
* Add seasonal recommendation engine.

Would you like a GitHub-ready README file too?
