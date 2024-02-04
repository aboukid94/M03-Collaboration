OOP_programming.py

class Solution:
    def sort012(self,arr,n):
    
        low = 0
        mid = 0
        high = n - 1
        
        while mid <= high:
            if arr[mid] == 0:
                arr[low],arr[mid] = arr[mid], arr[low]
                mid += 1
                low += 1
                    
            elif arr[mid] == 1:
                mid += 1
                
            else:
                arr[mid], arr[high] = arr[high], arr[mid]
                high -=1
                    
        return arr