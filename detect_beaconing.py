"""
C2 Beaconing Detection - Educational Simulation
Analyses timestamps in a CSV file for repeated, regular connection intervals.
Uses synthetic/example logs only; it does not contact any server.
"""

import csv
import statistics
from datetime import datetime
from pathlib import Path

LOG_FILE = Path(__file__).resolve().parent.parent / "data" / "sample_network_logs.csv"
TIME_FORMAT = "%Y-%m-%d %H:%M:%S"
REGULARITY_TOLERANCE_SECONDS = 3


def parse_time(value):
    return datetime.strptime(value, TIME_FORMAT)


def main():
    grouped = {}

    with LOG_FILE.open(newline="", encoding="utf-8") as file:
        for row in csv.DictReader(file):
            key = (row["source_ip"], row["destination_ip"], row["protocol"])
            grouped.setdefault(key, []).append(parse_time(row["timestamp"]))

    print("C2 Beaconing Detection - Simulated Log Analysis")
    print("-" * 55)

    for (source, destination, protocol), timestamps in grouped.items():
        timestamps.sort()
        if len(timestamps) < 3:
            continue

        intervals = [
            (timestamps[i] - timestamps[i - 1]).total_seconds()
            for i in range(1, len(timestamps))
        ]
        average = statistics.mean(intervals)
        spread = max(abs(value - average) for value in intervals)
        possible_beacon = spread <= REGULARITY_TOLERANCE_SECONDS

        print(f"\nSource: {source}")
        print(f"Destination: {destination}")
        print(f"Protocol: {protocol}")
        print(f"Connections: {len(timestamps)}")
        print(f"Intervals (seconds): {intervals}")
        print(f"Average interval: {average:.1f} seconds")
        print("Result:", "POSSIBLE REGULAR BEACONING" if possible_beacon else "No regular pattern detected")

    print("\nNote: Regular timing is only a clue for investigation, not proof of malware.")


if __name__ == "__main__":
    main()
