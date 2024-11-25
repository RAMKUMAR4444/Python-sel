import time
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

# Start the Edge browser
driver = webdriver.Edge()

# Set up a wait time of 10 seconds for finding elements
wait = WebDriverWait(driver, 10)

# Open the website
driver.get("https://www.mfcentral.com/")

# Make the browser window full size
driver.maximize_window()

# Path to save the screenshot
screenshot_path = r'B:\python_sel\navimf.png'

# Click on the "Sign In" button
signin = wait.until(EC.presence_of_element_located((By.XPATH, '//a[@class="btn login-btn aos-init aos-animate"]')))
signin.click()

# Enter PAN number into the input field
pan = wait.until(EC.presence_of_element_located((By.XPATH, '//input[@id="textinput"]')))
pan.send_keys("PAN NUMBER")

# Enter the password
password1 = wait.until(EC.presence_of_element_located((By.XPATH, '//input[@name="password"]')))
password1.send_keys("PASSWORD")

# Ask the user to solve CAPTCHA manually and press Enter
print("Please solve the CAPTCHA manually and press Enter once you have completed it.")
input("Press Enter to continue...")

# Click on the submit button
submit = wait.until(EC.element_to_be_clickable((By.XPATH, '//button[@id="submit-id"]')))
submit.click()

# Wait for 3 seconds to allow the page to load
time.sleep(3)

# List of security questions and answers
questions = [
    {
        'question_text': "What was the first company that you worked for?",
        'answer_text': "ANSWER"},
    {
        'question_text': "What is your first mobile brand?",
        'answer_text': "ANSWER"},
    {
        'question_text': "What is the name of your pet?",
        'answer_text': "ANSWER"},
    {
        'question_text': "What is your first Car/Bike?",
        'answer_text': "ANSWER"},
    {
        'question_text': "Which city you were born in?",
        'answer_text': "ANSWER"},
    {
        'question_text': "Where did you go to high school/college?",
        'answer_text': "ANSWER"}
]

try:
    # Go through each security question
    for question in questions:
        try:
            # Wait for the question to appear
            ques_element = wait.until(EC.presence_of_element_located((By.XPATH, '//textarea[@name="question"]')))

            # Get the text of the question
            actual_question_text = ques_element.get_attribute("value").strip()

            # If the question matches, enter the answer
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

# Wait for 3 seconds for any further processing
time.sleep(3)

# Click the "Ok" button
ok = wait.until(EC.element_to_be_clickable((By.XPATH, '//span[text()="Ok"]/..')))

# Scroll to the bottom of the page to make the "Ok" button visible
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);", ok)

ok.click()

# Wait for 3 seconds
time.sleep(3)

# Click the "OK" button
ok1 = wait.until(EC.element_to_be_clickable((By.XPATH, '//span[text()="OK"]/..')))
ok1.click()

# Wait for 3 seconds
time.sleep(3)

# Expected welcome message
expected_text = "Welcome, RAMKUMAR"

# Locate the welcome message element
welcome = wait.until(EC.presence_of_element_located((By.XPATH, '//div[@class="db-cards db-banner db-welcome"]/h3')))

# Get the text from the welcome message element
actual_text = welcome.text

# Print the text found
print("Actual text:", actual_text)

# Check if the actual text matches the expected text
if actual_text.strip() == expected_text:
    print("Login successful:", actual_text)
else:
    print("Login unsuccessful")

# Wait for 2 seconds
time.sleep(2)

# Click on the "Transactions" section
transact = wait.until(EC.element_to_be_clickable((By.XPATH, '//div[@class="db-cards db-grid-track"]')))
transact.click()

# Wait for 2 seconds
time.sleep(2)

# Click on the "Lumpsum/SIP" option
lumpsum = wait.until(EC.element_to_be_clickable((By.XPATH, '//h4[text()="Lumpsum/SIP"]/../..')))
lumpsum.click()

# Wait for 2 seconds
time.sleep(2)

# Click on the "Equity" option
equity = wait.until(EC.element_to_be_clickable((By.XPATH, '//img[@alt="Equity"]/..')))
equity.click()

# Wait for 2 seconds
time.sleep(2)

# Enter the search term in the search box
searchbox = wait.until(EC.presence_of_element_located((By.XPATH, '//input[@id="search-mfs"]')))
searchbox.send_keys("Navi Large & Midcap Fund Direct-Growth")

# Click on the search result
navi = wait.until(EC.element_to_be_clickable((By.XPATH, '//a[@class="search-mf-links"]')))
navi.click()

# Wait for 2 seconds
time.sleep(2)

# Click on the "Start Lumpsum" button
startlumpsum = wait.until(EC.element_to_be_clickable((By.XPATH, '//a[text()="Start Lumpsum"]')))
startlumpsum.click()

# Wait for 15 seconds
time.sleep(15)

# Enter the amount to invest
amount = wait.until(EC.presence_of_element_located((By.XPATH, '//input[@inputmode="numeric"]')))
amount.send_keys("10")

# Click the checkbox to agree to terms
checkbox = wait.until(EC.presence_of_element_located((By.XPATH, '//input[@type="checkbox"]/..')))
checkbox.click()

# Wait for 2 seconds
time.sleep(2)

# Click the "Invest" button
invest = wait.until(EC.element_to_be_clickable((By.XPATH, '//span[text()="Invest"]/..')))
invest.click()

# Wait for 5 seconds
time.sleep(5)

print("please enter otp")

# Wait for user input to continue
input("ENTER to continue")

# Click the "Verify OTP" button
verifyotp = wait.until(EC.element_to_be_clickable((By.XPATH, '//span[text()="Verify OTP"]/..')))
verifyotp.click()

# Click the "UPI" payment option
upi = wait.until(EC.element_to_be_clickable((By.XPATH, '//input[@value="UPI"]/..')))
upi.click()

# Click the "Pay" button
pay = wait.until(EC.element_to_be_clickable((By.XPATH, '//span[contains(text(),"Pay v")]/..')))
pay.click()

# Wait for 5 seconds
time.sleep(5)

# Click the "Google Pay" option
gpay = wait.until(EC.element_to_be_clickable((By.XPATH,  '(//div[@class="flex card flex-full gateway_bg"])/child :: div[3]')))
gpay.click()

# Wait for 2 seconds
time.sleep(2)

# Enter Google Pay ID
gpayid = wait.until(EC.presence_of_element_located((By.XPATH, '//input[@formcontrolname="upiValue"]')))
gpayid.send_keys("UPI ID")

# Wait for 2 seconds
time.sleep(2)

# Click the dropdown button to select bank
button4 = wait.until(EC.element_to_be_clickable((By.XPATH, '//mat-select[@role="listbox"]')))
button4.click()

# Wait for 2 seconds
time.sleep(2)

# Select the bank (SBI) from the dropdown
sbi = wait.until(EC.element_to_be_clickable((By.XPATH, '//span[text()=" @oksbi "]/..')))
sbi.click()

# Wait for 2 seconds
time.sleep(2)

# Click the "Verify and Pay" button
verifypay = wait.until(EC.element_to_be_clickable((By.XPATH, '//button[text()="verify and Pay "]')))
verifypay.click()

# Wait for 2 seconds
time.sleep(2)

# Set maximum wait time for success message
max_wait_time = 300  # Maximum time to wait in seconds
check_interval = 60  # Interval between checks in seconds
start_time = time.time()

while True:
    try:
        # Wait for the success message and check its text
        h3_element = WebDriverWait(driver, check_interval).until(
            EC.presence_of_element_located((By.XPATH, '//h3[text()="Success!"]')))

        if "Success!" in h3_element.text:
            print("Successfully bought a Navi MF!")

            # Save a screenshot of the page
            driver.save_screenshot(screenshot_path)
            print(f"Screenshot saved as {screenshot_path}")
            break

    except Exception as e:
        # Handle exceptions such as timeout
        print(f"An error occurred: {e}")

    # Check if maximum wait time exceeded
    elapsed_time = time.time() - start_time
    if elapsed_time > max_wait_time:
        print("Something Went Wrong")
    break

# Click on the profile button
profile = wait.until(EC.element_to_be_clickable((By.XPATH, '//span[text()="RAMKUMAR"]/ancestor::button')))
profile.click()

# Click on the logout link
logout = wait.until(EC.element_to_be_clickable((By.XPATH, '//a[text()="Logout"]/..')))
logout.click()

# Wait for 2 seconds
time.sleep(2)

# Expected URL after logout
expected_url = "https://app.mfcentral.com/investor/signin"

# Get the current URL of the page
current_url = driver.current_url

# Check if the current URL is the same as the expected URL
if current_url == expected_url:
    print("Page successfully logged out")
    # Close the browser if the URL matches
    driver.quit()
else:
    print(f"Failed to log out : {current_url}")
