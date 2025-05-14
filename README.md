# Marketplace-Negotiator-for-Students

This project supports students by using generative AI to draft housing inquiry messages, reducing the stress of finding accommodations. It combines Selenium for web scraping Facebook Marketplace listings with ChatGPT for message generation, involving both prompt engineering and API integration.

---

## 📚 Libraries to Download

Make sure you have Python 3.10+ installed. Then, install the required libraries:

- `selenium` (for web automation)  
  → `pip install selenium`

- `undetected-chromedriver` (to bypass bot detection on Facebook)  
  → `pip install undetected-chromedriver`

- `openai` (to interact with the ChatGPT API)  
  → `pip install openai`

---

## 🚀 How to Use This

1. **Clone or download this repository.**

2. **Set up your OpenAI API key.**  
   - You must have an API key from OpenAI.
   - Save it in your environment or directly in your code (not recommended for public use).

3. **Run `main.py`.**  
   This script will:
   - Ask you to paste a Facebook Marketplace listing URL.
   - Open Chrome in a controlled window and allow you to log in to Facebook.
   - Scrape the listing description and price.
   - Use ChatGPT to generate a friendly message to the seller asking for a student-friendly price.

4. **Read the AI-generated message in the terminal.**  
   You can then copy and paste it into Facebook Messenger to contact the seller.

---

### 💡 Note:
- Facebook login is **manual** and required.
- Make sure Chrome is installed and compatible with `undetected-chromedriver`.
- This tool is for educational and personal use only.

