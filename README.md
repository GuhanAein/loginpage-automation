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


If there are any issues please let me know and contributions are welcome


To have your Python code run automatically on startup, you can create a script that runs your Python code and then set up a system-specific method for running that script at startup. The method for setting up a startup script can vary depending on your operating system. Below are instructions for Windows, macOS, and Linux.

**Windows:**
1. Create a batch script (a file with a .bat extension) to run your Python code. Open a text editor and save the following lines as `startup_script.bat`:

```batch
@echo off
pythonw.exe "C:\path\to\your\python_script.py"
```

Replace `"C:\path\to\your\python_script.py"` with the actual path to your Python script.

2. Press `Win + R`, type `shell:startup`, and click "OK". This will open the Startup folder.

3. Move the `startup_script.bat` file into the Startup folder.

**macOS:**
1. Create a shell script to run your Python code. Open a text editor and save the following lines as `startup_script.sh`:

```bash
#!/bin/bash
python3 /path/to/your/python_script.py
```

Replace `/path/to/your/python_script.py` with the actual path to your Python script.

2. Open Terminal and navigate to the location where you saved `startup_script.sh`.

3. Make the script executable by running:

```bash
chmod +x startup_script.sh
```

4. Move the script to the user's home directory:

```bash
mv startup_script.sh ~/
```

5. Open System Preferences > Users & Groups > Login Items. Click the "+" button and add the `startup_script.sh` from your home directory.

**Linux (Ubuntu and similar):**
1. Create a shell script to run your Python code. Open a text editor and save the following lines as `startup_script.sh`:

```bash
#!/bin/bash
python3 /path/to/your/python_script.py
```

Replace `/path/to/your/python_script.py` with the actual path to your Python script.

2. Open a terminal and navigate to the location where you saved `startup_script.sh`.

3. Make the script executable by running:

```bash
chmod +x startup_script.sh
```

4. Move the script to the `~/.config/autostart/` directory:

```bash
mv startup_script.sh ~/.config/autostart/
```

5. The script will run on startup for the current user.

Remember to replace `/path/to/your/python_script.py` with the actual path to your Python script, and make sure you have Python installed and the necessary dependencies are available when the script runs at startup.



## License

This project is licensed under the [MIT License](LICENSE).
