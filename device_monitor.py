rates = [72, 88, 65, 94, 81, 76, 102, 69]

measurement = len(rates)
total = sum(rates)
avge = total / measurement
minim = min(rates)
maxim = max(rates)

below75 = 0

for rate in rates:
    if rate < 75:
        below75 += 1
    
first_above_90 = None
 
for rate in rates:
    if rate > 90:
        first_above_90 = rate
        break

print("Data Transfer Rate Analyzer")
print("---------------------------")
print("Measurement: ", measurement)
print("Total: ", total)
print("Average: ", avge)
print("Minimum: ", minim)
print("Maximum: ", maxim)
print("The numbers of reading below 75 mbps: ", below75)
print("First reading of above 90 mbps: ", first_above_90)
