"""
===================   TASK 3  ====================
* Name: Recursive Sum
*
* Write a recursive function that will sum given
* list of integer numbers.
*
* Note: Please describe in details possible cases
* in which your solution might not work.
*
* Use main() function to test your solution.
===================================================
"""

# Write your function here
def sabiranjedo(n):

    if n==0:
        return 0
    return + sabiranjedo(n-1)
zb = sabiranjedo(100)
print(zb)





def main():
    # Test your function here
    pass

if __name__ == "__main__":
    main()