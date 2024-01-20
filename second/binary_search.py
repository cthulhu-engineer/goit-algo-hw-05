def binary_search_with_upper_bound(arr, target):
    left, right = 0, len(arr) - 1
    iterations = 0
    upper_bound = None

    while left <= right:
        iterations += 1
        mid = left + (right - left) // 2

        if arr[mid] == target:
            upper_bound = arr[mid]
            break
        elif arr[mid] < target:
            left = mid + 1
            upper_bound = arr[mid] if upper_bound is None or arr[mid] > upper_bound else upper_bound
        else:
            right = mid - 1

    if upper_bound is None and left < len(arr):
        upper_bound = arr[left]

    return iterations, upper_bound
