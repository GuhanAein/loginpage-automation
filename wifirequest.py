import socket
from selenium import webdriver

# Set up the browser driver (e.g., Chrome)
driver = webdriver.Chrome()

# Function to check if connected to a specific Wi-Fi network
def connected_to_wifi(ssid):
    connected_ssid = (
        ":".join(["%02x" % b for b in bytes.fromhex(ssid)])
        if len(ssid) == 12
        else ssid
    )
    wifi_name = socket.gethostname()
    return connected_ssid == wifi_name

# Define the SSID of the desired Wi-Fi network
desired_ssid = "KPR Institutions"  # Replace with the desired SSID

# Check if connected to the desired Wi-Fi network
if connected_to_wifi(desired_ssid):
    # Navigate to the login page
    driver.get("http://10.10.32.1")

    # Find the input fields and enter your credentials
    username_input = driver.find_element_by_id("username")
    password_input = driver.find_element_by_id("password")
    username_input.send_keys("21ad015")  # Replace with your actual user ID
    password_input.send_keys("123456")  # Replace with your actual password

    # Find the checkbox and click it (assuming its ID is "accept-checkbox")
    accept_checkbox = driver.find_element_by_id("accept-checkbox")
    accept_checkbox.click()

    # Submit the form
    login_button = driver.find_element_by_id("login-button")
    login_button.click()

    # Close the browser
    driver.quit()
else:
    print("Not connected to the desired Wi-Fi network.")
