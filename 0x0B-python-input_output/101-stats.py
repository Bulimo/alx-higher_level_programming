#!/usr/bin/python3
"""
Module 101-stats

Functions:
    print_metrics()
"""


def print_metrics(size, status_codes):
    print("File size: {:d}".format(size))
    for k, v in sorted(status_codes.items()):
        if v:
            print("{:s}: {:d}".format(k, v))


if __name__ == "__main__":
    """
    reads file input and extracts line for extraction of metrics
    """
    import sys

    size = 0
    line_count = 0
    status_codes = {"200": 0, "301": 0, "400": 0, "401": 0,
                    "403": 0, "404": 0, "405": 0, "500": 0}
    try:
        for line in sys.stdin:
            log = [str(word) for word in line.strip().split(" ")]
            size += int(log[-1])

            if log[-2] in status_codes:
                status_codes[log[-2]] += 1

            line_count += 1

            if line_count % 10 == 0:
                print_metrics(size, status_codes)

    except KeyboardInterrupt:
        print_metrics(size, status_codes)
