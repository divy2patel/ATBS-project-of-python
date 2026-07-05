'''
You have an inventory as a dictionary. Write:

1. `displayInventory(inventory)` — prints each item and count, plus total
2. `addToInventory(inventory, addedItems)` — takes a list of items and adds them to the dict
'''

def displayInventory(inventory):
    totalitem=0
    for k,v in inventory.items():
        print(f'item={k},value={v}')
        totalitem+=1
    print(f'Total number of item:{totalitem}')

def addToInventory(inventory,addeditems):
    for item in addeditems:
        inventory.setdefault(item,0)
        inventory[item]+=1
    return inventory

inv={'gold':42,'rope':1}
dragon_loot=['gold','degger','gold','gold','ruby']
inv= addToInventory(inv,dragon_loot)
displayInventory(inv)