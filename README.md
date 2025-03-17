# screen-nolock
Python script to prevent session locking when the script is active. Also, casually prevents state change in teams

It uses the `pyautogui` library to send key events.

## How It Works

The script alternates between pressing the `volumedown` and `volumeup` keys every 100 seconds to keep the system active. You can modify the keys or the time interval as needed.

## Requirements

To run this script, you need to install the following Python library:

- `pyautogui`

### Installation

You can install the required library using pip:
pip install pyautogui
