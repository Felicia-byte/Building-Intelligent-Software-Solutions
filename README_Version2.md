```markdown
# Week 4 Assignment: AI in Software Engineering
Theme: "Building Intelligent Software Solutions" 💻🤖

This repository scaffold contains example code, templates, and guidance to complete the Week 4 assignment. It is designed for a group of 3–5 students. Update group members and customize as needed.

Contents
- README.md (this file)
- requirements.txt
- code_completion.py            — AI vs manual sorting function + 200-word analysis
- selenium_login_test.py       — Selenium test script for login (valid/invalid)
- predictive_analytics.py      — Predictive analytics pipeline using Breast Cancer dataset (adapted)
- report_template.md           — PDF-ready report template with theoretical answers and ethical reflection
- assets/                      — place screenshots, saved models, and test outputs here

How to run
1. Create virtual environment
   python -m venv venv
   source venv/bin/activate  # Linux/Mac
   venv\Scripts\activate     # Windows

2. Install dependencies
   pip install -r requirements.txt

3. Run the code examples:
   - AI vs Manual sort function:
     python code_completion.py
   - Selenium login test (see notes below for WebDriver):
     python selenium_login_test.py
   - Predictive analytics:
     python predictive_analytics.py

Notes
- Selenium requires a browser driver (e.g., ChromeDriver) installed and accessible in PATH.
  Download ChromeDriver matching your Chrome version: https://chromedriver.chromium.org/downloads
- predictive_analytics.py uses sklearn's built-in Breast Cancer dataset to show a complete flow. Replace with a Kaggle dataset if required.
- Put screenshots (Selenium test results, model metrics, graphs) into assets/ and reference them in the final PDF report.

Submission checklist
- [ ] Code committed to GitHub
- [ ] PDF report exported from report_template.md with screenshots
- [ ] 3-minute video with all group members
- [ ] Post the PDF as an article in the Community and share the repo link

If you want, I can:
- Convert scripts into Jupyter notebooks
- Create the PDF report and fill in sample results (I can run code locally here only conceptually — please run and provide screenshots if required)
```