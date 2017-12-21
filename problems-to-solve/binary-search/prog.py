# This program deals with Binary Search.

def bin_search(item_list, item):
    first = 0
    last = len(item_list) - 1
    found = False

    while(first <= last and not found):
        mid = (first + last) // 2
        if item_list[mid] == item:
            found = True
        else:
            if item < item_list[mid]:
                last = mid - 1
            else:
                first= mid + 1

        return found

print(bin_search([2,6,4,9,5,7,3,1], 6))
print(bin_search([21,62,43,96,54,23,10,13], 10))
