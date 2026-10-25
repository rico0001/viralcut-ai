from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

def test_user_flow():
    # Initialize the WebDriver
    driver = webdriver.Chrome()  # Ensure you have the ChromeDriver installed and in your PATH
    driver.get("http://localhost:3000")  # Adjust the URL as necessary for your local setup

    # Test user registration
    driver.find_element(By.LINK_TEXT, "Register").click()
    time.sleep(1)  # Wait for the page to load

    driver.find_element(By.NAME, "username").send_keys("testuser")
    driver.find_element(By.NAME, "email").send_keys("testuser@example.com")
    driver.find_element(By.NAME, "password").send_keys("password123")
    driver.find_element(By.NAME, "confirm_password").send_keys("password123")
    driver.find_element(By.XPATH, "//button[text()='Register']").click()
    time.sleep(2)  # Wait for registration to complete

    # Test user login
    driver.find_element(By.LINK_TEXT, "Login").click()
    time.sleep(1)

    driver.find_element(By.NAME, "email").send_keys("testuser@example.com")
    driver.find_element(By.NAME, "password").send_keys("password123")
    driver.find_element(By.XPATH, "//button[text()='Login']").click()
    time.sleep(2)

    # Test creating a new project
    driver.find_element(By.LINK_TEXT, "New Project").click()
    time.sleep(1)

    driver.find_element(By.NAME, "project_name").send_keys("Test Project")
    driver.find_element(By.XPATH, "//button[text()='Create Project']").click()
    time.sleep(2)

    # Verify project creation
    assert "Test Project" in driver.page_source

    # Clean up and close the browser
    driver.quit()

if __name__ == "__main__":
    test_user_flow()