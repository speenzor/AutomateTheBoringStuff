stuff = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}

#This fuction takes a dictionary like 'stuff' and outputs a nice list
def displayinventory(inventory):
    print('Inventory:')
    item_total=0
    for k,v in inventory.items():
        print (v,k)
        item_total= item_total + v
    print('Total number of items: ' + str(item_total))


inv = {'gold coin': 42, 'rope': 1}
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']

#This fuction takes a dictionary and a list and updates the dictionary with the new item count
def addToInventory(inventory, addedItems):
	for i in addedItems:
		inventory.setdefault(i,0)
	for k,v in inventory.items():
		inventory[k]= v+(int(addedItems.count(k)))

displayinventory(inv)
