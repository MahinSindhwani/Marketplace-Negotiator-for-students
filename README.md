# 🏠 Marketplace Negotiator for Students

This project helps students and individuals who need assistance writing housing inquiry messages. It uses generative AI (via the OpenAI API) to craft friendly and professional messages, reducing the stress of finding accommodations. It combines **Selenium** for scraping Facebook Marketplace listings with **ChatGPT** for message generation — using both prompt engineering and API integration.

---

## 📚 Required Libraries

Make sure you have **Python 3.10+** installed. Then, install the necessary libraries:

- `selenium` — for web automation  
  → `pip install selenium`

- `undetected-chromedriver` — bypasses bot detection on Facebook  
  → `pip install undetected-chromedriver`

- `openai` — interacts with the ChatGPT API  
  → `pip install openai`

---

## 🚀 How to Use

1. **Clone or download this repository.**

2. **Set up your OpenAI API key**  
   - You must have a valid OpenAI API key.
   - Store it securely in your environment variables (recommended) or directly in the script for testing.

3. **Run `main.py`**  
   The script will:
   - Ask you for a Facebook Marketplace listing URL.
   - Launch Chrome and allow you to manually log in to Facebook.
   - Scrape the listing's description and price.
   - Use ChatGPT to generate a polite, student-friendly message for the seller.

4. **Use the AI-generated message**  
   - The message will be printed in your terminal.
   - You can copy it and paste it into Facebook Messenger.

---

## ⚠️ Notes

- Facebook login must be completed manually.
- Make sure your installed Chrome version is compatible with `undetected-chromedriver`.
- This tool is intended for **educational and personal use only**.
- I am working on making this into a chrome extension for easy usage

---

## 🔧 Tech Stack

![Python](https://img.shields.io/badge/-Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Selenium](https://img.shields.io/badge/-Selenium-43B02A?style=for-the-badge&logo=selenium&logoColor=white)
![OpenAI](https://img.shields.io/badge/-OpenAI-412991?style=for-the-badge&logo=openai&logoColor=white)
