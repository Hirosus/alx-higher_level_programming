#!/usr/bin/python3
"""
Script to compute metrics from stdin input.
"""

import sys

def print_metrics(total_size, status_counts):
    """
    Print computed metrics.

    :param total_size: The total file size.
    :type total_size: int
    :param status_counts: Dictionary containing counts of status codes.
    :type status_counts: dict
    """
    print("File size: {}".format(total_size))
    for status_code in sorted(status_counts):
        print("{}: {}".format(status_code, status_counts[status_code]))

def compute_metrics(lines):
    """
    Compute metrics from a list of input lines.

    :param lines: List of input lines.
    :type lines: list of str
    :return: Total file size and counts of status codes.
    :rtype: tuple
    """
    total_size = 0
    status_counts = {}

    for line in lines:
        elements = line.split()
        if len(elements) >= 7:
            status_code = elements[-2]
            file_size = elements[-1]

            total_size += int(file_size)

            if status_code in status_counts:
                status_counts[status_code] += 1
            else:
                status_counts[status_code] = 1

    return total_size, status_counts

def main():
    """
    Main function to read stdin and compute metrics.
    """
    lines = []
    try:
        for line in sys.stdin:
            lines.append(line.strip())
            if len(lines) == 10:
                total_size, status_counts = compute_metrics(lines)
                print_metrics(total_size, status_counts)
                lines = []

    except KeyboardInterrupt:
        total_size, status_counts = compute_metrics(lines)
        print_metrics(total_size, status_counts)

if __name__ == "__main__":
    main()

