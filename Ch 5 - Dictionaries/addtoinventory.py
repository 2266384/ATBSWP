inv = {'gold coin': 42, 'rope': 1}
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']

def addToInventory(inventory, addedItems):
    mySet = set(addedItems)
    for items in mySet:
        if items in inventory.keys():
            inventory[items] += addedItems.count(items)
        else:
            inventory[items] = addedItems.count(items)

    return inventory

def displayInventory(inventory):
    print('Inventory:')
    items_total = 0
    for k, v in inventory.items():
        print(str(v) + ' ' + k)
        items_total = items_total + v
    print('Total number of items: ' + str(items_total))

inv = addToInventory(inv, dragonLoot)
displayInventory(inv)
