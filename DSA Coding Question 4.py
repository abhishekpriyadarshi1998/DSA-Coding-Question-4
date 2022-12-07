def peak_element(arr, n): 
    # Find index of maximum element 
    # on left side of array 
    max_index = 0
    for i in range(n): 
        if arr[i] > arr[max_index]: 
            max_index = i 
  
    # Return maximum element 
    return arr[max_index] 
  
# Driver program 
arr = [10, 20, 15, 2, 23, 90, 67] 
n = len(arr) 
print(peak_element(arr, n))