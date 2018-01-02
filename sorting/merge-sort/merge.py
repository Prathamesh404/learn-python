
# Here we will deal with code to create a merge subroutine.
def merge:
    """
    This function deals with merging of two arrays.
    """
    c = []
    while len(a) != 0 and len(b) != 0:
        if a[0] < b[0]:
            c.append(a[0])
            a.remove(a[0])
        else:
            c.append(b[0])
            b.remove(b[0])
    if len(a) == 0:
        c += b

    else:
        c += a

    return c

#this code is for merge sort

def mergesort(x):
    """
    function to sort an array using merge sort algorithm
    """
    if len(x) == 0 or len(x) == 1:
         return x

    else:
        middle = len(x)/2
        a = mergesort(x[:middle])
        b = mergesort(x[middle:])

        return merge(a,b)

                                    
