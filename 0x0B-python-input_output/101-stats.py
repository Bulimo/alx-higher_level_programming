#!/usr/bin/python3
"""
Module 101-stats

Functions:
    print_metrics()
"""

import sys


size = 0
line_count = 0
status_codes = {"200": 0, "301": 0, "400": 0, "401": 0,
                "403": 0, "404": 0, "405": 0, "500": 0}
try:
    for line in sys.stdin:
        line = line.strip()
        if not line:
            continue

        log = line.split(" ")
        try:
            size += int(log[-1])
        except Exception:
            pass
        if log[-2] in status_codes:
            status_codes[log[-2]] += 1
        line_count += 1
        if line_count % 10 == 0:
            print("File size: {:d}".format(size))
            for k, v in sorted(status_codes.items()):
                if v > 0:
                    print("{:s}: {:d}".format(k, v))

except KeyboardInterrupt:
    print("File size: {:d}".format(size))
    for k, v in sorted(status_codes.items()):
        if v > 0:
            print("{:s}: {:d}".format(k, v))
    raise

print("File size: {:d}".format(size))
for k, v in sorted(status_codes.items()):
    if v > 0:
        print("{:s}: {:d}".format(k, v))
