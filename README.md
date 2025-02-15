# GenAI-App---AI-Code-Reviewer  
## 📌 Project Overview  
AI Code Reviewer is a Python-based web application that analyzes Python code and provides AI-generated feedback on:  
- **Bug detection**  
- **Performance optimizations**  
- **Code improvement suggestions**  
- **Fixed code snippets**  

The app is built using **Streamlit** for UI and **Google Gemini AI** for code analysis.  

## 🛠️ Tech Stack  
- **Frontend & Backend:** Streamlit  
- **AI Model:** Google Gemini AI  
- **Programming Language:** Python  

---

## 📂 Project Structure  
```
📁 AI-Code-Reviewer
│── app.py                 # Main application file
│── README.md               # Project documentation
│── requirements.txt        # requirements 
```

---

## ⚙️ Installation & Setup  

### 1️⃣ Clone the Repository  
```bash
git clone https://github.com/your-username/AI-Code-Reviewer.git
cd AI-Code-Reviewer
```

### 2️⃣ Install Dependencies  
```bash
pip install -r requirements.txt
```

### 3️⃣ Set Up Google AI API  
1. Obtain an API key from **Google AI Console**.  
2. Enable **Generative Language API**.  
3. Add your API key in `app.py`.  

### 4️⃣ Run the Application  
```bash
streamlit run app.py
```
This will launch the app in your browser at **http://localhost:8501/**.  

---

## 🚀 Features  
- **User-friendly Interface** – Simple and intuitive UI using Streamlit.  
- **AI-Powered Code Review** – Uses Google Gemini AI to analyze Python code.  
- **Bug Detection & Fixes** – Identifies issues and suggests improvements.  

---

## 🖥️ Usage Instructions  
1. Enter Python code in the provided text box.  
2. Click "Generate Review".  
3. The AI will analyze the code and provide:  
   - **Bug reports**  
   - **Code efficiency improvements**  
   - **Suggested fixes**  

---

## 🛠️ Troubleshooting  
**API Key Not Valid Error**  
- Ensure the API key is correctly set in `app.py`.  
- Enable **Generative Language API** in Google Cloud Console.  

**ModuleNotFoundError: No module named 'streamlit'**  
- Run:  
  ```bash
  pip install streamlit
  ```

**Streamlit Not Launching?**  
- Use the command:  
  ```bash
  streamlit run app.py
  ```

---

## 🤝 Contributing  
Feel free to contribute by opening a **Pull Request** or reporting issues.  

---

### ⭐ Star this repository if you found it useful!  

---
