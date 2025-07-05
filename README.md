# 🧠 Resume & Cover Letter Writer

An AI-powered resume and cover letter builder with a beautiful, human-like design. Built using Flask, HTML/CSS/JavaScript, and OpenAI's GPT API.

## 🚀 Features

- ✨ **AI-Powered Content Generation**: Uses GPT-3.5/4 for personalized, professional writing.
- 💡 **Real-Time Preview**: See your resume and cover letter while building.
- 🧾 **PDF Export**: Download high-quality PDFs with one click.
- 🎨 **Modern UI**: Clean, ATS-friendly and responsive design.
- 📱 **Responsive**: Works perfectly across desktop, tablet, and mobile.
- 🧰 **No API Key Required in Demo Mode**: Test all features without OpenAI key.

---

## 🛠️ Tech Stack

**Frontend**  
- HTML5, CSS3, JavaScript  
- Font Awesome for icons  
- jsPDF for PDF generation

**Backend**  
- Python Flask  
- OpenAI API (GPT-3.5/4)  
- Gunicorn for deployment  

---

## 📂 File Structure
resume-cover-letter-writer/
├── app.py # Flask backend
├── index.html # Main HTML
├── requirements.txt # Python dependencies
├── package.json # Project metadata
├── Procfile # Deployment setup (Heroku/Gunicorn)
├── static/
│ ├── css/style.css # Styles
│ └── js/script.js # Frontend logic
└── README.md # This file


---

## ⚙️ Setup Instructions

### 1. Prerequisites
- Python 3.8 or higher
- (Optional) OpenAI API key

### 2. Installation

```bash
git clone https://github.com/KavyaPatel83/Resume-Cover-Letter-Writer.git
cd Resume-Cover-Letter-Writer
pip install -r requirements.txt

export OPENAI_API_KEY="your-api-key-here"  # Or use .env file
python app.py
python -m venv venv
source venv/bin/activate       # Windows: venv\Scripts\activate
pip install -r requirements.txt



