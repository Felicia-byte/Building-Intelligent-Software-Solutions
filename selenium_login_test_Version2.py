#!/usr/bin/env python3
"""
Task 2: Automated Testing with AI (Selenium example)

- Automates login test for a sample site (replace sample URLs with the target).
- Executes two test cases: valid and invalid credentials.
- Prints results and saves a screenshot for evidence.

Setup:
- Install Chrome and ChromeDriver (matching versions). Put chromedriver in PATH.
- Alternatively, modify to use Firefox/geckodriver.
- This script uses Selenium WebDriver directly. AI-enabled tools like Testim.io can augment by
  auto-generating selectors and maintaining flaky tests; this script demonstrates an automated baseline.

Note:
- Replace TEST_URL, VALID_USERNAME, VALID_PASSWORD with real values or point to a local test page.
"""

import os
import time

try:
    from selenium import webdriver  # type: ignore
    from selenium.webdriver.common.by import By  # type: ignore
    from selenium.common.exceptions import NoSuchElementException, WebDriverException  # type: ignore
except ImportError:
    print("Missing dependency: 'selenium' is not installed. Install it with: pip install selenium")
    raise SystemExit(1)

# --- Configuration (update for your target app) ---
TEST_URL = "https://example.com/login"  # replace with actual login page
VALID_USERNAME = "testuser"
VALID_PASSWORD = "correct_password"
INVALID_USERNAME = "baduser"
INVALID_PASSWORD = "wrong_password"
SCREENSHOT_DIR = "assets"
os.makedirs(SCREENSHOT_DIR, exist_ok=True)

# --- Selectors (update per page) ---
# The following are example selectors. Update them to match your login page.
SELECTOR_USERNAME = (By.NAME, "username")  # or (By.ID, "username")
SELECTOR_PASSWORD = (By.NAME, "password")
SELECTOR_SUBMIT = (By.XPATH, "//button[@type='submit']")
SELECTOR_SUCCESS_INDICATOR = (By.CSS_SELECTOR, ".dashboard")  # element that appears on successful login
SELECTOR_ERROR_INDICATOR = (By.CSS_SELECTOR, ".error")        # element showing error message

def run_login_test(driver, username, password, timeout=5):
    driver.get(TEST_URL)
    time.sleep(1)  # wait for page load; replace with explicit waits for production tests

    try:
        driver.find_element(*SELECTOR_USERNAME).clear()
        driver.find_element(*SELECTOR_USERNAME).send_keys(username)
        driver.find_element(*SELECTOR_PASSWORD).clear()
        driver.find_element(*SELECTOR_PASSWORD).send_keys(password)
        driver.find_element(*SELECTOR_SUBMIT).click()
    except NoSuchElementException as e:
        return {"status": "error", "message": f"Selector not found: {e}"}

    # Wait briefly for outcome
    time.sleep(timeout)

    # Check success or error element
    try:
        if driver.find_elements(*SELECTOR_SUCCESS_INDICATOR):
            return {"status": "success", "message": "Login successful (success indicator present)"}
        if driver.find_elements(*SELECTOR_ERROR_INDICATOR):
            return {"status": "failure", "message": "Login failed (error indicator present)"}
    except Exception as e:
        return {"status": "error", "message": f"Error checking result: {e}"}

    # Fallback: based on current URL change or title
    current_url = driver.current_url
    return {"status": "unknown", "message": f"Current URL: {current_url}"}

def main():
    # Instantiate WebDriver. Ensure chromedriver is in PATH.
    try:
        driver = webdriver.Chrome()  # or webdriver.Firefox()
    except WebDriverException as e:
        print("WebDriver error:", e)
        print("Make sure the browser driver (chromedriver/geckodriver) is installed and in PATH.")
        return

    results = {}

    # Valid credentials test
    res_valid = run_login_test(driver, VALID_USERNAME, VALID_PASSWORD)
    results['valid'] = res_valid
    driver.save_screenshot(os.path.join(SCREENSHOT_DIR, "login_valid.png"))

    # Invalid credentials test
    res_invalid = run_login_test(driver, INVALID_USERNAME, INVALID_PASSWORD)
    results['invalid'] = res_invalid
    driver.save_screenshot(os.path.join(SCREENSHOT_DIR, "login_invalid.png"))

    driver.quit()

    print("=== Selenium login test results ===")
    for k, v in results.items():
        print(f"{k}: {v}")

    # 150-word summary
    summary = (
        "Selenium automates repetitive UI test cases like login flows, enabling systematic execution "
        "of both valid and invalid credential scenarios. AI-enhanced testing platforms (e.g., Testim.io) "
        "improve this baseline by automatically detecting stable selectors, suggesting resilience strategies "
        "for flaky elements, and maintaining tests when UI changes occur. Running automated tests frequently "
        "in CI increases coverage across browsers and reduces manual effort. In our run, screenshots for both "
        "cases were saved to 'assets/'. Compared to manual testing, automated tests execute faster, are "
        "repeatable, and can run at scale, while AI tools further reduce maintenance overhead by adapting to "
        "DOM changes and providing failure triage."
    )
    print("\nSummary (≈150 words):\n")
    print(summary)

if __name__ == "__main__":
    main()