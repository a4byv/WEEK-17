def get_initial_readings():
    return [28, 31, 35, 37, 29]


def add_reading(readings):
    text = input("Enter new reading: ")

    try:
        reading = int(text)

        if reading < 0 or reading > 100:
            print("Invalid reading. Enter a value from 0 to 100.")
        else:
            readings.append(reading)
            print("Reading added successfully.")

    except ValueError:
        print("Invalid input. Enter a whole number only.")


def classify_reading(reading, warning_limit, critical_limit):
    if reading < warning_limit:
        return "NORMAL"
    elif reading <= critical_limit:
        return "WARNING"
    else:
        return "CRITICAL"


def compute_total(readings):
    total = 0
    for reading in readings:
        total += reading
    return total


def compute_average(readings):
    return compute_total(readings) / len(readings)


def find_minimum(readings):
    minimum = readings[0]
    for reading in readings:
        if reading < minimum:
            minimum = reading
    return minimum


def find_maximum(readings):
    maximum = readings[0]
    for reading in readings:
        if reading > maximum:
            maximum = reading
    return maximum


def count_category(readings, warning_limit, critical_limit, category):
    count = 0

    for reading in readings:
        result = classify_reading(
            reading, warning_limit, critical_limit
        )

        if result == category:
            count += 1

    return count


def determine_overall_status(warning_count, critical_count):
    if critical_count > 0:
        return "ATTENTION REQUIRED"
    elif warning_count > 0:
        return "MONITOR"
    else:
        return "NORMAL"


def display_summary(readings):
    if len(readings) == 0:
        print("No readings available.")
        return

    warning_limit = 30
    critical_limit = 35

    total = compute_total(readings)
    average = compute_average(readings)
    minimum = find_minimum(readings)
    maximum = find_maximum(readings)

    normal_count = count_category(
        readings, warning_limit, critical_limit, "NORMAL"
    )
    warning_count = count_category(
        readings, warning_limit, critical_limit, "WARNING"
    )
    critical_count = count_category(
        readings, warning_limit, critical_limit, "CRITICAL"
    )

    status = determine_overall_status(
        warning_count, critical_count
    )

    print("\nMONITORING SUMMARY")
    print("------------------")
    print("Number of readings  :", len(readings))
    print("Total of readings   :", total)
    print(f"Average temperature : {average:.2f} °C")
    print(f"Minimum temperature : {minimum} °C")
    print(f"Maximum temperature : {maximum} °C")
    print()
    print(f"NORMAL   : {normal_count} ({normal_count / len(readings) * 100:.2f}%)")
    print(f"WARNING  : {warning_count} ({warning_count / len(readings) * 100:.2f}%)")
    print(f"CRITICAL : {critical_count} ({critical_count / len(readings) * 100:.2f}%)")
    print()
    print("Overall Status:", status)


def main():
    readings = get_initial_readings()
    warning_limit = 30
    critical_limit = 35

    while True:
        print("\nSIMULATED DEVICE MONITORING SYSTEM")
        print("----------------------------------")
        print("[1] View Readings")
        print("[2] Add Reading")
        print("[3] Classify Readings")
        print("[4] Generate Summary")
        print("[5] Exit")

        choice = input("Enter choice: ").strip()

        if choice == "1":
            print("\nCURRENT READINGS")
            print("----------------")
            for index, reading in enumerate(readings, start=1):
                print(f"Reading {index}: {reading} °C")

        elif choice == "2":
            add_reading(readings)

        elif choice == "3":
            print("\nREADING CLASSIFICATION")
            print("----------------------")
            for reading in readings:
                category = classify_reading(
                    reading, warning_limit, critical_limit
                )
                print(f"{reading} °C -> {category}")

        elif choice == "4":
            display_summary(readings)

        elif choice == "5":
            print("Thank you for using the Device Monitoring System.")
            break

        else:
            print("Invalid choice. Please enter a number from 1 to 5.")


main()
