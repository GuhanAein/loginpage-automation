# Wi-Fi Login Automation

This Python script automates the login process on a Wi-Fi portal. It checks if the device is connected to a specific Wi-Fi network and performs the login process using Selenium.

## Requirements

- Python 3.x
- Selenium package
- WebDriver (e.g., ChromeDriver) for the desired browser

## Installation

1. Install Python:
   - Visit the official Python website (https://www.python.org) and download the latest version suitable for your operating system.
   - Follow the installation instructions provided.

2. Install Selenium:
   - Open a command prompt or terminal.
   - Run the following command to install the Selenium package:
     ```
     pip install selenium
     ```

3. Download WebDriver:
   - Download the WebDriver for your desired browser (e.g., ChromeDriver for Google Chrome).
   - Ensure the WebDriver version matches your browser version for compatibility.

4. Set up the WebDriver:
   - Extract the WebDriver executable from the downloaded archive.
   - Place the executable in a directory included in your system's PATH environment variable.

## Usage

1. Open the Python script file `wifi_login.py` in a text editor.

2. Modify the script:
   - Replace `"KPR Institutions"` with the SSID (Wi-Fi network name) of your desired network.
   - Replace `"21ad015"` with your actual user ID.
   - Replace `"123456"` with your actual password.

3. Save the modified script.

4. Run the script:
   - Open a command prompt or terminal.
   - Navigate to the directory containing the script.
   - Run the following command:
     ```
     python wifi_login.py
     ```

   The script will check if your device is connected to the specified Wi-Fi network and perform the login process if it is. Otherwise, it will display a message indicating that it's not connected.

## License

This project is licensed under the [MIT License](LICENSE).


If there are any issues please let me know and contributions are welcome
