#!/usr/bin/python3
"""
Function to find a peak element in a list of unsorted integers
"""

def find_peak(list_of_integers):
    """
    Find a peak in a list of unsorted integers.

    Args:
    list_of_integers (list): List of unsorted integers.

    Returns:
    int: A peak element.
    """
    if not list_of_integers:
        return None

    def find_peak_util(nums, low, high, n):
        mid = low + (high - low) // 2

        # Check if mid is a peak
        if (mid == 0 or nums[mid] >= nums[mid - 1]) and (mid == n - 1 or nums[mid] >= nums[mid + 1]):
            return nums[mid]

        # If the left neighbor is greater, the peak is in the left half
        if mid > 0 and nums[mid - 1] > nums[mid]:
            return find_peak_util(nums, low, mid - 1, n)

        # If the right neighbor is greater, the peak is in the right half
        return find_peak_util(nums, mid + 1, high, n)

    n = len(list_of_integers)
    return find_peak_util(list_of_integers, 0, n - 1, n)
