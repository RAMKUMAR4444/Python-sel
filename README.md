# MF Central Automation Script 🌐

## About This Project

This project automates the process of logging into MF Central, searching for mutual funds, and completing a purchase. It uses Python with Selenium to interact with the website and handle navigation, form submissions, and UPI payments.

---

## What I Did

- Automated the login process, including handling CAPTCHA manually.
- Dynamically matched and answered security questions.
- Navigated the mutual fund selection process.
- Integrated UPI payment through Google Pay.
- Captured a screenshot of the success page after purchase.
- Logged out securely from the account.

---

## Challenges and Solutions

### CAPTCHA Handling
- **Issue**: CAPTCHA can't be automated ethically.
- **Solution**: Added a manual prompt to solve CAPTCHA before proceeding.

### Dynamic Security Questions
- **Issue**: Security questions vary each time.
- **Solution**: Used dynamic text matching to identify the question and provide the correct answer.

### Website Layout Changes
- **Issue**: Changing website structure could break automation.
- **Solution**: Used robust XPath locators and error handling to adjust if elements are not found.

### Disclaimer
- This script is intended for personal and educational use only.
---

Happy Automating! 🎉
