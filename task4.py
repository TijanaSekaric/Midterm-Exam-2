"""
===================   TASK 4  ====================
* Name: Merge Sort
*
* Write a function that will implement merge sort
* algorithm. Generate list of 1000 random integer
* numbers and sort the list using your function.
*
* Note: Please describe in details possible cases
* in which your solution might not work.
*
* Use main() function to test your solution.
===================================================
"""

# Write your function here



def main():
    # Test your function here
    pass

if __name__ == "__main__":
    main()


from random import randint

def merge_sort(niz):

    duzina = len(niz)

    for pozicija in range(duzina-1):
        minimum = pozicija

        for i in range(minimum+1, duzina):

            if niz[i] < niz[minimum]:
                minimum = i

        niz[pozicija], niz[minimum]= niz[minimum], niz[pozicija]

    return niz


if __name__== "__main__":
    niz=[]

    for i in range(1000):
        niz.append(randint(0,1000))

    merge_niz=merge_sort(niz)
    print(merge_niz)