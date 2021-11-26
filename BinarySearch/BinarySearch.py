def binary_search(a,b,c,d):
    if c >= b:
        mid = (c + b) // 2
        if a[mid] == d:
            return mid
        elif a[mid] > d:
            return binary_search(a,b, mid - 1,d)
        else:
            return binary_search(a, mid + 1, c, d)
    else:
        return -1

my_list = [41,44,49,52,55,60,67,68,90,100]
result = binary_search(my_list,0,10,67) # 0 = Start of list 10 = End of list and 67 = What we are searching for
result = result + 1
print(result)

#Binary search is an efficient algorithm for finding an item from a sorted list of items. 
#It works by repeatedly dividing in half the portion of the list that could contain the item, until you've narrowed down the possible locations to just one.
#Explanation given by Khan academy  https://www.khanacademy.org/computing/computer-science/algorithms/binary-search/a/binary-search#:~:text=Binary%20search%20is%20an%20efficient,possible%20locations%20to%20just%20one.