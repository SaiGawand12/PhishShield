# PhishShield: AI-Powered Website Safety Checker

## Overview
PhishShield is an AI-driven web application that helps users determine whether a website is safe or a phishing attempt. It leverages machine learning models to analyze various website attributes and provide a security assessment.

## Features
- 🔍 **Website URL Analysis**
- 🔐 **AI-powered phishing detection**
- 🛡 **Domain and SSL validation**
- 🕵 **Whois Lookup & VirusTotal Integration**
- 📊 **Machine Learning-based threat detection**
- 📡 **Real-time URL scanning**
- 📜 **Detailed risk reports**

## Dataset Used
PhishShield is trained using the following datasets:
- **majestic_million.csv** → Contains trusted/safe website data from [majestic.com](https://majestic.com/)
- **verified_online.csv** → Contains phishing website data from [phishtank.org](https://phishtank.org/)
- **Additional URL threat intelligence sources**

## Installation
Clone the repository and install dependencies:
```bash
git clone https://github.com/SaiGawand12/PhishShield.git
```
```bash
cd PhishShield
```
## Install Requirenments
```bash
pip install -r requirements.txt
```

## Usage
Run the Flask application:
```bash
python app.py
```
Visit `http://127.0.0.1:5000/` in your browser and enter a website URL to analyze its safety.

## Requirements
Install the necessary Python packages:
```bash
Flask
requests
scikit-learn
pandas
numpy
tensorflow
torch
transformers
whois
tldextract
joblib
flask-wtf
```

## 🛠 Technologies Used
- Python (Flask)
- HTML, CSS, JavaScript
- Machine Learning (Scikit-Learn, Pandas, NumPy)
- WHOIS & VirusTotal API integration

## Deployment
PhishShield can be deployed using Docker:
```bash
docker build -t phishshield .
docker run -p 5000:5000 phishshield
```
Or deploy on cloud platforms like AWS, Heroku, or Azure.


## 📜 License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 👨‍💻 Author
**Your Name**  
© 2025 SAI GAWAND. All rights reserved.

## 🤝 Contributing
Contributions are welcome! Feel free to open an issue or submit a pull request.

## ⭐ Acknowledgments
- PhishTank and  Majestic's Phishing Dataset
- Flask & Machine Learning Community

---
📢 Don't forget to ⭐ the repository if you find it useful!
