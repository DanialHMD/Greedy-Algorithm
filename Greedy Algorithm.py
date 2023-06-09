def greedy(cash, total):
    
    cash.sort(reverse=True) #reversing cash list

    amount = 0 #assigning a variable for getting the amount of cash is used
    change = [] #a list of type of cash is used

    for c in cash:

        while c <= total:
            change.append(c) #add change to the list
            total -= c #reducing the change from total
            amount += 1 #adding one to the amount
        
    return amount , change

cash=[1,5,10,25,50,100]
total=286

a , c = greedy(cash , total)

print("Minimum number of coins needed:", a)
print("Change:", c)
