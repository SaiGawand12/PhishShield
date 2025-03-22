import pandas as pd
import tldextract
import re

def extract_features(url):
    """Extracts various features from the given URL."""
    extracted = tldextract.extract(url)
    domain = extracted.domain
    subdomain = extracted.subdomain

    return {
        "URL_Length": len(url),
        "Num_Dots": url.count('.'),
        "Num_Slashes": url.count('/'),
        "Num_Hyphens": url.count('-'),
        "Num_At": url.count('@'),
        "Num_Question": url.count('?'),
        "Num_Equals": url.count('='),
        "Num_Percent": url.count('%'),
        "Has_IP": 1 if re.match(r'(\d{1,3}\.){3}\d{1,3}', url) else 0,
        "Has_Https": 1 if url.startswith("https") else 0,
        "Domain_Length": len(domain),
        "Subdomain_Length": len(subdomain),
        "Num_Subdomains": subdomain.count('.'),
        "Is_Trusted": 0 if domain in ["google", "amazon", "paypal", "facebook", "twitter", "microsoft", "apple"] else 1
    }

def preprocess_data():
    """Processes phishing and legitimate datasets, extracts features, and saves them."""
    phishing_df = pd.read_csv("data/verified_online.csv", usecols=["url"])
    phishing_df["Is_Phishing"] = 1  

    legit_df = pd.read_csv("data/majestic_million.csv", usecols=["Domain"])
    legit_df.rename(columns={"Domain": "url"}, inplace=True)
    legit_df["Is_Phishing"] = 0  

    df = pd.concat([phishing_df, legit_df], ignore_index=True).dropna(subset=["url"]).drop_duplicates()

    feature_data = df["url"].apply(extract_features)
    feature_df = pd.DataFrame(feature_data.tolist())
    feature_df["Is_Phishing"] = df["Is_Phishing"].values

    feature_df.to_csv("data/processed_data.csv", index=False)
    print("✅ Preprocessed data saved to: data/processed_data.csv")

if __name__ == "__main__":
    preprocess_data()
