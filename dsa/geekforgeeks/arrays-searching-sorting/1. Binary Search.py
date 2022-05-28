from typing import List

def binarySearchRecursive(arr: List[int], ele: int, left: int, right: int) -> int:
    
    if right < left:
        return -1
    
    mid = left + (right-left)//2

    if arr[mid] == ele:
        return mid
    
    if (arr[mid] > ele):
        return binarySearchRecursive(arr, ele, left, mid-1)
    else:
        return binarySearchRecursive(arr, ele, mid+1, right)



def binarySearchIterative(arr: List[int], ele: int, left: int, right: int) -> int:
    while (left <= right):

        mid = left + (right-left)//2
        if arr[mid] == ele:
            return mid

        if (arr[mid] > ele):
            right = mid - 1
        
        if (arr[mid] < ele):
            left = mid+1

    return -1


def binarySearch(arr: List[int], n: int, interative: bool) -> int:
    if interative:
        return binarySearchIterative(arr, n, 0, len(arr)-1)
    
    return binarySearchRecursive(arr, n, 0, len(arr)-1)



if __name__ == "__main__":
    arr = [2, 5, 8, 10, 12]
    search_ele = 5
    searchinterative = False

    result = "Not Found" if binarySearch(arr, search_ele, searchinterative) == -1 else "Found"

    print (f"Result is result {result}")