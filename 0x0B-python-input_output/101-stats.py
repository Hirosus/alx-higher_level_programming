#!/usr/bin/python3

import sys

def print_metrics(total_size, status_codes):
    """Prints the computed metrics."""
    print("Total file size: {}".format(total_size))
    for code in sorted(status_codes):
        print("{}: {}".format(code, status_codes[code]))

def main():
    total_size = 0
    status_codes = {}

    try:
        for i, line in enumerate(sys.stdin, 1):
            parts = line.split()
            if len(parts) >= 9:
                status_code = parts[-2]
                file_size = parts[-1]
                
                total_size += int(file_size)

                if status_code in status_codes:
                    status_codes[status_code] += 1
                else:
                    status_codes[status_code] = 1

            if i % 10 == 0:
                print_metrics(total_size, status_codes)

    except KeyboardInterrupt:
        print_metrics(total_size, status_codes)
        sys.exit(0)

if __name__ == "__main__":
    main()

