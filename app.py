import joblib
import pandas as pd
import tldextract
import re
from flask import Flask, render_template, request

app = Flask(__name__)

# Load trained model
model = joblib.load("models/phishing_model.pkl")

def extract_features(url):
    """
    Extracts features from the given URL.
    """
    extracted = tldextract.extract(url)
    domain = extracted.domain
    subdomain = extracted.subdomain

    features = {
        "URL_Length": len(url),
        "Num_Dots": url.count('.'),
        "Num_Slashes": url.count('/'),
        "Num_Hyphens": url.count('-'),
        "Num_At": url.count('@'),
        "Num_Question": url.count('?'),
        "Num_Equals": url.count('='),
        "Num_Percent": url.count('%'),
        "Has_IP": 1 if re.match(r'(\d{1,3}\.){3}\d{1,3}', url) else 0,
        "Has_Https": 1 if "https" in url else 0,
        "Domain_Length": len(domain),
        "Subdomain_Length": len(subdomain),
        "Num_Subdomains": subdomain.count('.'),
        "Is_Trusted": 1 if domain in ["google", "amazon", "paypal", "facebook", "twitter", "microsoft", "apple"] else 0
    }
    
    return features

@app.route("/", methods=["GET", "POST"])
def index():
    result = None
    confidence = 0
    whois_link = ""
    technical_details_link = ""
    if request.method == "POST":
        url = request.form.get("url")
        
        if url:
            features = extract_features(url)
            feature_df = pd.DataFrame([features])
            prediction = model.predict(feature_df)[0]
            result = "Safe" if prediction == 0 else "Phishing"
        

        # Generate links dynamically
        whois_link = f"https://who.is/whois/{url}"
        technical_details_link = f"https://www.virustotal.com/gui/domain/{url}"
            

    return render_template("index.html", result=result, whois_link=whois_link, technical_details_link=technical_details_link)

if __name__ == "__main__":
    app.run(debug=True)
