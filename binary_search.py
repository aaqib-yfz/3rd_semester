def binary_search(alist,item):
    first=0
    last = len(alist)-1
    found = False
    while first <= last and not found:
        mid = (first + last )//2
        if alist[mid] == item:
            found = True
        elif alist[mid] > item:
            last = mid - 1
        else:
            first = mid + 1
    return found

a = [1 , 2 , 4 ,6 ,7 ,8,9,10]
print(binary_search(a,6))