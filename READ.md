# Simulated Device Monitoring and Alert System

**Student Name:** Abegail T. Bueno
**Student Number:** 2600401
**Section:** 1- CPE A

## Project Description

This program analyzes simulated data transfer rate readings. It calculates the total number of measurements, sum, average, minimum, and maximum values. It also counts readings below 75 Mbps and identifies the first reading above 90 Mbps.

## Features

Analyze stored data transfer rate readings
Calculate the total number of measurements
Compute the sum and average of readings
Identify the minimum and maximum readings
Count readings below 75 Mbps
Find the first reading above 90 Mbps

## Requirements

- Python 3 (no external packages)

## How to Run

1. Open a terminal inside the Week17 folder.
2. Type: python device_monitor.py
   (On macOS or Linux, type: python3 device_monitor.py)

## Sample Output

## Data Transfer Rate Analyzer

Measurement: 8
Total: 647
Average: 80.875
Minimum: 65
Maximum: 102
The numbers of reading below 75 mbps: 3
First reading of above 90 mbps: 94

## Test Cases

I performed 10 tests. ** passed and ** failed.
Full details are in test_cases.md.

## Known Limitations

The program uses predefined data transfer rate readings.
New readings cannot be entered by the user.
The program does not save results to a file.
The program only identifies the first reading above 90 Mbps.

## Reflection

The hardest part of this project was calculating and analyzing the data transfer rate readings correctly. I learned how to use Python functions such as len(), sum(), min(), and max() to summarize data. I also used loops and conditional statements to count readings below 75 Mbps and find the first reading above 90 Mbps. Next, I would improve the program by allowing users to enter new readings and validating their inputs.
