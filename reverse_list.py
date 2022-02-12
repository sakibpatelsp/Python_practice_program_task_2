"""Write a program to reverse a list without using reverse function"""

def rev_lst(lst):
    i = []
    for j in lst:
        i.insert(0, j)
    print(i)

if __name__ == '__main__':
    l = [1, 2, 3, 4, 5, 6]
    rev_lst(l)