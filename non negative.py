def max_area(arr):
    left = 0
    right = len(arr) - 1
    max_area = 0
    while left < right:
        area = min(arr[left], arr[right]) * (right - left)
        max_area = max(max_area, area)
        if arr[left] < arr[right]:
            left += 1
        else:
            right -= 1
    return max_area
print(max_area([1, 5, 4, 3]))
print(max_area([3, 1, 2, 4, 5]))
print(max_area([1,8,6,2,5,4,8,3,7])) 
print(max_area([1,1]))
print(max_area([7,3]))
