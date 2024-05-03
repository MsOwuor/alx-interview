#!/usr/bin/env python3

import sys
import re

# Regular expression pattern to match the input format
pattern = re.compile(r'^(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}) - \[.*\] "GET \/projects\/260 HTTP\/1\.1" (\d{3}) (\d+)$')

# Initialize variables to store metrics
total_size = 0
status_counts = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}
lines_processed = 0

try:
    for line in sys.stdin:
        # Check if the line matches the expected format
        match = pattern.match(line)
        if match:
            # Extract relevant information from the line
            ip_address = match.group(1)
            status_code = int(match.group(2))
            file_size = int(match.group(3))

            # Update metrics
            total_size += file_size
            status_counts[status_code] += 1
            lines_processed += 1

            # Print statistics after every 10 lines
            if lines_processed % 10 == 0:
                print(f"File size: {total_size}")
                for code in sorted(status_counts.keys()):
                    if status_counts[code] > 0:
                        print(f"{code}: {status_counts[code]}")
                print()

except KeyboardInterrupt:
    pass  # Handle keyboard interrupt gracefully

# Print final statistics
print(f"File size: {total_size}")
for code in sorted(status_counts.keys()):
    if status_counts[code] > 0:
        print(f"{code}: {status_counts[code]}")

