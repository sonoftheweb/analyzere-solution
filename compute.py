#!/usr/bin/env python

import sys

MAX_INPUT = 100

def parse_arguments():
    if len(sys.argv) != 3:
        print("Usage: compute.py <threshold> <limit>")
        return None, None

    try: 
        threshold = float(sys.argv[1])
        limit = float(sys.argv[2])
    except ValueError:
        print("both arguments must be numeric")
        return None, None

    return threshold, limit

def compute_adjusted_value(input_value, threshold, limit, cumulative_sum):
    if input_value > threshold:
        adjusted_value = input_value - threshold
    else: 
        adjusted_value = 0.0

    if cumulative_sum + adjusted_value > limit:
        adjusted_value = max(0.0, limit - cumulative_sum)

    return adjusted_value

def main():
    threshold, limit = parse_arguments()
    if threshold is None or limit is None:
        return

    cumulative_sum = 0.0
    results = []
    line_count = 0

    for l in sys.stdin:
        line_count += 1
        if line_count > MAX_INPUT:
            print(f"Input exceeds {MAX_INPUT} lines, stopping...")
            break

        try:
            input_value = float(l.strip())
        except ValueError: 
            print("all input must be numeric")
            continue

        adjusted_value = compute_adjusted_value(input_value, threshold, limit, cumulative_sum)
        cumulative_sum += adjusted_value
        results.append(adjusted_value)

    for result in results:
        print(f"{result:.1f}")

    print(f"{cumulative_sum:.1f}")

if __name__ == "__main__":
    main()
