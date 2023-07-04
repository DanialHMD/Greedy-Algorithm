# Greedy Algorithm
Greedy algorithm is one of most famous algorithms that is used to solve problems. Basically it used to make optimal choices in each stage.
### How does it work?
So for example we have multiple steps in a program which we want to reach the highest point in each step without looking back or forward. 

Thats when greedy algorithm works; in each step we look for optimal choice to get the highest point at the end of program.

![download](https://github.com/DanialHMD/Greedy-Algorithm/assets/108475573/d5069988-dcb2-4db6-b791-ffaf38998f9f)

If we want to use the greedy algorithm in the picture above, it will work like this:
* In first it will choose the "4" in top
* in next step it has 4 options, it will choose the option with highest value, which in this case will be "3"
* in next step we have subs of "3" we chose in the previous step, so the choice again will be the highest which is "3".
* and in the last step between 3 subs of the second "3" we have "2" as the highest value.

In total we will get `4+3+3+2=12`. The problem with greedy algorithm is that it doesn't return the optimal choice in the end, what I mean is that we have higher numbers and choices but we can't get them from greedy algorithm. So make sure to use this algorithm in the right place.

### Example
For the exmple of Greedy Algorithm we can bring up the money change.

Whenever you want to give change for money you can use Greedy technique. The way it works is that for example you want to give 23 bucks and the cash is available is `[1,5,10,25]`.

So what you do is that you take the cashes as a list and reverse it and you save that `23` bucks as a variable called `total`. Write a Greedy function for finding the change like this:
```
def greedy(cash, total):
    
    cash.sort(reverse=True) 

    amount = 0 
    change = [] 

    for c in cash:

        while c <= total:
            change.append(c) 
            total -= c 
            amount += 1 
        
    return amount , change
```

In this function we have some extra variable like `change` which saves the list of cash values that has been used for change. and an `amount` variable which defines the number of cash that has been used.

And the loop is the key in this function since everything happens here. for each value in reversed cash list it will keep subtracting the value from `total` and adds the information to `amount` and `cash`. when total is smaller than value it will move on to the next value in the list and does the same process until total is 0.

This was a simple exmaple for Greedy Algorithm it can be used in many problems and can be helpful.

