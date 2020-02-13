#!/usr/bin/env python3
def find_averages_of_subarrays(K, arr):
    result = []
    windowSum, windowStart = 0.0, 0
    # windowEnd is our pointer that goes through all the numbers!
    for windowEnd in range(len(arr)):
        windowSum +=arr[windowEnd] # Add the next element
        # slide the window, we don't need to slide if we've not hit the required window size of 'k'
        if windowEnd >= K - 1: # it's K-1 because our window is size 5, but that'll be 0-4 in python
            result.append(windowSum / K)  # calculate the average
            windowSum -= arr[windowStart]  # subtract element going out
            windowStart += 1  # slide the window ahead
        print(f"WindowSum: {windowSum}, WindowStart: {windowStart}, WindowEnd: {windowEnd}")
    return result


def main():
  result = find_averages_of_subarrays(5, [1, 3, 2, 6, -1, 4, 1, 8, 2])
  print("Averages of subarrays of size K: " + str(result))

main()