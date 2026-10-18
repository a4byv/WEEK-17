# Test Cases – Simulated Device Monitoring and Alert System

## Test Case Table

| Test Case | Input or Action | Expected Result | Actual Result | Pass/Fail |
|---|---|---|---|---|
| TC01 | Run the program | Displays the initial readings: 28, 31, 35, 37, 29 | Displayed all five initial readings correctly. | Pass |
| TC02 | View readings | Shows all five temperature readings in order | Displayed all five readings correctly. | Pass |
| TC03 | Add a new reading | Enter 33; reading is added successfully | Displayed "Reading added successfully." | Pass |
| TC04 | Enter an invalid reading | Enter abc; displays an error message | Displayed "Invalid input. Enter a whole number only." | Pass |
| TC05 | Enter a reading above the limit | Enter 120; reading is rejected | Displayed "Invalid reading. Enter a value from 0 to 100." | Pass |
| TC06 | Classify the readings | Displays NORMAL, WARNING, or CRITICAL for each reading | Classified 28 °C and 29 °C as NORMAL, 31 °C and 35 °C as WARNING, and 37 °C as CRITICAL. | Pass |
| TC07 | Calculate the total | Total: 160 | Total: 160 | Pass |
| TC08 | Calculate the average | Average: 32.00 °C | Average: 32.00 °C | Pass |
| TC09 | Find the minimum and maximum | Minimum: 28 °C; Maximum: 37 °C | Minimum: 28 °C; Maximum: 37 °C | Pass |
| TC10 | Count readings by category | NORMAL: 2; WARNING: 2; CRITICAL: 1 | Displayed the correct number and percentage for each category. | Pass |

## Bugs Found and Fixed

- No major bugs were found during testing. The program correctly displayed the initial readings and calculated the total, average, minimum, and maximum values.
- The program successfully rejected invalid inputs, such as letters and readings outside the allowed range.
- The reading classifications worked correctly, with 30 °C and 35 °C classified as WARNING and readings above 35 °C classified as CRITICAL.
- The summary correctly displayed the number and percentage of readings in each category, along with the overall status.
- The menu and exit option worked properly, allowing the user to choose different functions and end the program successfully.
