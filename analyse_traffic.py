"""
Network Traffic Summary - Educational Simulation
Counts sample connections and highlights repeated destinations.
No live network scanning or external connections are performed.
"""

import csv
from collections import Counter
from pathlib import Path

LOG_FILE = Path(__file__).resolve().parent.parent / "data" / "sample_network_logs.csv"


def main():
    with LOG_FILE.open(newline="", encoding="utf-8") as file:
        rows = list(csv.DictReader(file))

    destinations = Counter(row["destination_ip"] for row in rows)
    total = len(rows)

    print("Network Traffic Summary - Simulated Data")
    print("-" * 45)
    print(f"Total connections: {total}")
    print(f"Unique destinations: {len(destinations)}")
    print("\nConnections by destination:")

    for destination, count in destinations.most_common():
        label = "Repeated destination - investigate" if count >= 3 else "No repeated pattern in this sample"
        print(f"{destination}: {count} connection(s) | {label}")

    print("\nReminder: Repeated connections can be legitimate. Correlate with endpoint and DNS logs.")


if __name__ == "__main__":
    main()
