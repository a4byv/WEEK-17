# Test Cases – Simulated Device Monitoring and Alert System

Tested by: Abegail T. Bueno Date: October 12 2026

| Test Case | Input or Action   | Expected Result                         | Actual Result  | Pass/Fail |
| --------- | ----------------- | --------------------------------------- | -------------- | --------- |
| TC01      | Run the program   | rates = 72, 88, 65, 94, 81, 76, 102, 69 | Display        | Pass      |
| TC02      | Enter Measurement | Measurement: 8                          | Measurement: 8 | Pass      |
| TC03      | Calculate Total   | Total: 647                              | Total: 647     | Pass      |
| TC04      | Calculate Average | Average: 80.875                         | Average: 80.87 | Pass      |
| TC05      | find Minimum      | Minimum: 65                             | Minimum: 65    | Pass      |
| TC06      | Find Maximum      | Maximum: 102                            | Maximum: 102   | Pass      |
| TC07      | Count readings    |                                         |                |           |
|           | below 75 Mbps     | Total: 647                              |                | Pass      |
| TC08      | First reading     |                                         |                |           |
|           | above 90 Mbps     | Total: 647                              |                | Pass      |
| TC09      | Check readings    |                                         |                |           |
|           | below 75 Mbps     | Total: 647                              |                | Pass      |
| TC010     | Check loop        |                                         |                |           |
|           | above 90 Mbps     | Total: 647                              |                | Pass      |

## Bugs Found and Fixed

- (In this program, there is no bug detected during testing. The program correctly calculated the total, average, minimum, and maximum values. The hardest test was checking the first reading above 90 Mbps. The program correctly displayed 94 Mbps instead of 102 Mbps because the break statement stopped the loop after finding the first qualifying reading.)
