import time
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

# Start Edge browser
driver = webdriver.Edge()

# Set up a wait time to find elements
wait = WebDriverWait(driver, 10)

# Open the website
driver.get("https://www.mfcentral.com/")

# Make the browser window full size
driver.maximize_window()

# Path to save the screenshot
screenshot_path = r'B:\python_sel\portfolio_screenshot.png'

# Click on the signin button
signin = wait.until(EC.presence_of_element_located((By.XPATH, '//a[@class="btn login-btn aos-init aos-animate"]')))
signin.click()

# Enter PAN number into the input field
pan = wait.until(EC.presence_of_element_located((By.XPATH, '//input[@id="textinput"]')))
pan.send_keys("PAN number")

# Enter the password
password1 = wait.until(EC.presence_of_element_located((By.XPATH, '//input[@name="password"]')))
password1.send_keys("PASSWORD")

# Ask the user to solve CAPTCHA
print("Please solve the CAPTCHA manually and press Enter once you have completed it.")
input("Press Enter to continue...")

# Click on the submit button
submit = wait.until(EC.element_to_be_clickable((By.XPATH, '//button[@id="submit-id"]')))
submit.click()

# Wait for the page to load
time.sleep(3)

# List of security questions and answers
questions = [
    {
        'question_text': "What was the first company that you worked for?",
        'answer_text': "CAMS"},
    {
        'question_text': "What is your first mobile brand?",
        'answer_text': "ASUS"},
    {
        'question_text': "What is the name of your pet?",
        'answer_text': "JUDA"},
    {
        'question_text': "What is your first Car/Bike?",
        'answer_text': "HORNET"},
    {
        'question_text': "Which city you were born in?",
        'answer_text': "TRICHY"}
]

try:
    # Go through each question
    for question in questions:
        try:
            # Wait for the question to appear
            ques_element = wait.until(EC.presence_of_element_located((By.XPATH, '//textarea[@name="question"]')))

            # Get the text of the question
            actual_question_text = ques_element.get_attribute("value").strip()

            # If it matches, answer the question
            if actual_question_text == question['question_text']:
                ans_element = wait.until(EC.presence_of_element_located((By.XPATH, '//input[@name="answer"]')))
                ans_element.send_keys(question['answer_text'])
                break  # Stop looking once the answer is entered
            else:
                print("checking....")

        except TimeoutException:
            print(f"Question not found: {question['question_text']}")

except TimeoutException:
    print("Couldn't find one of the question elements in time.")

# Click the final submit button
submit2 = wait.until(EC.element_to_be_clickable((By.XPATH, '//button[@id="submit-id"]')))
submit2.click()

# Scroll to the bottom of the page
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

# Click the "Ok" button
ok = wait.until(EC.element_to_be_clickable((By.XPATH, '//span[text()="Ok"]/..')))
ok.click()

# Click the "OK" button
ok1 = wait.until(EC.element_to_be_clickable((By.XPATH, '//span[text()="OK"]/..')))
ok1.click()

# Wait a bit
time.sleep(2)

expected_text = "Welcome, RAMKUMAR"

# Locate the element
welcome = wait.until(EC.presence_of_element_located((By.XPATH, '//div[@class="db-cards db-banner db-welcome"]/h3')))

# Get the entire text from the  element
actual_text = welcome.text

# Print the extracted text
print("Actual text:", actual_text)

# Compare the expected text with the actual text
if actual_text.strip() == expected_text:
    print("Login successful:", actual_text)
else:
    print("Login unsuccessful")

# Wait for a bit
time.sleep(2)

# Click on the portfolio section
portfolio = wait.until(EC.element_to_be_clickable((By.XPATH, '//div[@class="db-cards db-grid-portfolio"]')))
portfolio.click()

# Wait for the page to update
time.sleep(2)

# Take a screenshot and save it
driver.get_screenshot_as_file(screenshot_path)
print(f'Screenshot saved to {screenshot_path}')

# Click on the profile button
profile = wait.until(EC.element_to_be_clickable((By.XPATH, '//span[text()="RAMKUMAR"]/ancestor::button')))
profile.click()

# Click on the logout link
logout = wait.until(EC.element_to_be_clickable((By.XPATH, '//a[text()="Logout"]/..')))
logout.click()

time.sleep(2)

# Expected URL after logout the page
expected_url = "https://app.mfcentral.com/investor/signin"

# Get the current URL of the page
current_url = driver.current_url

# Check if the current URL is the same as the expected URL
if current_url == expected_url:
    print("Page successfully logged out")
    # Close the browser if the URL matches
    driver.quit()
else:
    print("Failed to log out : {current_url}")
    # Failed to log out
