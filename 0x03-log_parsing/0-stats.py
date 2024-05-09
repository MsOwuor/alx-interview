#!/usr/bin/python3
"""
Log parsing script
"""

import sys
import re


def output(log: dict) -> None:
    """
    Helper function to display stats
    :param log: Dictionary containing the log statistics
    """
    print("File size: {}".format(log["file_size"]))
    for code in sorted(log["code_frequency"]):
        if log["code_frequency"][code]:
            print("{}: {}".format(code, log["code_frequency"][code]))


if __name__ == "__main__":
    # Regular expression to match the log line format
    regex = re.compile(
        r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3} - '
        r'\[\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}.\d+\] '
        r'"GET /projects/260 HTTP/1.1" (.{3}) (\d+)')

    line_count = 0
    log = {}
    log["file_size"] = 0
    log["code_frequency"] = {
        str(code): 0 for code in [200, 301, 400, 401, 403, 404, 405, 500]}

    try:
        for line in sys.stdin:
            line = line.strip()
            match = regex.fullmatch(line)
            if match:
                line_count += 1
                code = match.group(1)
                file_size = int(match.group(2))

                # Update file size
                log["file_size"] += file_size

                # Update status code frequency
                if code.isdecimal():
                    log["code_frequency"][code] += 1

                # Print stats every 10 lines
                if line_count % 10 == 0:
                    output(log)
    finally:
        # Print final stats
        output(log)
