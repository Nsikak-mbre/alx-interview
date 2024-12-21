#!/usr/bin/python3
"""
Script that reads stdin line by line and computes metrics.
"""

import sys


def print_stats(total_size, status_counts):
    """
    Print the accumulated metrics.
    """
    print(f"File size: {total_size}")
    for status_code in sorted(status_counts.keys()):
        if status_counts[status_code] > 0:
            print(f"{status_code}: {status_counts[status_code]}")


def main():
    """
    Main function to read stdin and compute metrics.
    """
    total_size = 0
    status_counts = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0,
                     404: 0, 405: 0, 500: 0}
    line_count = 0

    try:
        for line in sys.stdin:
            line = line.strip()
            line_count += 1
            try:
                # Split and parse the line
                parts = line.split()
                file_size = int(parts[-1])
                status_code = int(parts[-2])

                # Update metrics
                total_size += file_size
                if status_code in status_counts:
                    status_counts[status_code] += 1

            except (ValueError, IndexError):
                # Skip lines that don't match the format
                continue

            # Print statistics every 10 lines
            if line_count % 10 == 0:
                print_stats(total_size, status_counts)

    except KeyboardInterrupt:
        # Handle keyboard interruption (CTRL + C)
        print_stats(total_size, status_counts)
        raise

    # Final print after processing all lines
    print_stats(total_size, status_counts)


if __name__ == "__main__":
    main()
