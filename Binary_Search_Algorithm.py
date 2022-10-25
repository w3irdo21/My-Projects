# {*** W wil use Recursion for easy ***}
def binary_search(start,end,li,target):

# it will break the list to half for searching easily
    if start<=end :
        mid=(start+end)//2      
        
        if(li[mid]==target) :
            return mid+1
        elif(li[mid]>target) :
            return binary_search(start,mid-1,li,target)
        elif(target>li[mid]) :
            return binary_search(mid+1,end,li,target)
    else :
        return -1

total=int(input("Enter total Elements for a List : "))
list = []

for i in range(0,total) :
    a=int(input(f"Enter Element number {i+1} : "))
    list.append(a)

print(list)

# Sorting is Important for searching
list.sort()
print(list)

search=int(input("Enter the Element You want to search :\n"))
searched= binary_search(0,total,list,search)

if searched== -1 :
    print("Element not in list")
else:
     print(f"Element is Placed at {searched} Position ")