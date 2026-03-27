num_users= int(input("Enter number of users: "))

users= {}

for i in range(num_users): 
    
    print()
    username = input("Enter username: ")
    num_items= int(input("How many items? "))
    items = []
    
    for j in range(num_items): 
        
        item =input("Item " + str(j+1)+ ": ")
        items.append(item)
        
    
    users[username] = items
    
print("\nUSER DATA: ")

for user in users:
    print(user, "->", users[user])
    
all_items= set()
dict={}

for user in users:
    user_items_set= set(users[user])
    
    for item in user_items_set:
        all_items.add(item)
        
        if item in dict:
            dict[item] += 1
        else:
            dict[item]=1
            
print("\nCOMMON ITEMS:")

found_common=False

for item in dict:
    if dict[item] >1:
        print(item)
        found_common=True
        
if found_common== False:
    print("None")
    
print("\nUNIQUE ITEMS:")

found_unique=False

for item in dict:
    if dict[item]==1:
        print(item)
        found_unique=True
        
if found_unique==False:
    print("None")
        
print("\nMOST POPULAR ITEM:")
    
num_max =0
    
for item in dict:
        if dict[item] > num_max:
            num_max = dict[item]
            
for item in dict:
        if dict[item] == num_max:
            print(item)    
