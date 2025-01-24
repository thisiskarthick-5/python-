

n = int(input("Enter the number of item : "))
sum = 0

item1 = "apple"
item2 = "mango"
item3 = "orange"

for i in range(n):
    name = input("Enter the name of the item : ").lower()
    count = int(input("Enter the count : "))     
    if name == item1:
        sum += count*20
    elif name == item2:
        sum += count*40
    elif name == item3:
        sum += count*50
    else:
        print("not found") 

print("bill :",sum)
print("Item\t","Count\t","Total\t")

if name == item1:
    print("Apple\t",count,"\t",count*20)
elif name == item2:
    print("mango\t",count,"\t",count*40)
elif name == item3:
    print("orange\t",count,"\t",count*50)
 












   



