# Simulated Device Monitoring and Alert System

**Student Name:** Abegail T. Bueno
**Student Number:** 2600401
**Section:** 1- CPE A

## Project Description

This program is designed to check and analyze temperature readings from a simulated device. It calculates the total, average, lowest, and highest temperatures. It also checks whether each reading is NORMAL, WARNING, or CRITICAL based on the set temperature limits. This helps users understand the device's condition and identify readings that may need attention.

## Features

- Displays the initial temperature readings.
- Allows users to add a new temperature reading.
- Checks if the entered reading is within the allowed range of 0–100 °C.
- Classifies temperatures as NORMAL, WARNING, or CRITICAL.
- Calculates the total and average of the readings.
- Finds the lowest and highest temperatures.
- Counts the readings under each category and calculates their percentages.
- Shows the overall status of the device based on the readings.

## Requirements

- Python 3 (no external packages)

## How to Run

1. Open a terminal inside the Week17 folder.
2. Type: python device_monitor.py
   (On macOS or Linux, type: python3 device_monitor.py)

## Sample Output

## Data Transfer Rate Analyzer

SIMULATED DEVICE MONITORING SYSTEM
----------------------------------
[1] View Readings
[2] Add Reading
[3] Classify Readings
[4] Generate Summary
[5] Exit
Enter choice: 

## Test Cases

I prepared 10 test cases to check if the program works properly. These tests cover the initial readings, adding new readings, handling invalid inputs, classifying temperatures, and calculating the results.
Full details are in test_cases.md.

## Known Limitations

- The program starts with a set of temperature readings.
- Users can only add readings between 0 and 100 °C.
- The program does not save the readings or results for future use.
- The temperature categories depend on the limits set in the code.
- The program uses sample data and is not connected to a real device or temperature sensor.

## Reflection

While working on this project, I learned how to use Python to check and analyze temperature readings. One of the challenging parts was making sure that the calculations and classifications were correct. I also learned how to use functions like sum(), len(), min(), and max() to get the results more easily. Using loops and conditional statements helped me count the readings and determine the device's overall status. If I were to improve this program in the future, I would add a feature that allows users to save their results and enter more readings easily.
