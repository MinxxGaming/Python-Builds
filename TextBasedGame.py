# print introduction and game instructions
def show_instructions():
    print('Welcome to Talanthea Manor!')
    print('Your comrades have gone missing. Collect each of their weapons, or be destroyed by Lady Talanthea herself')
    print('move options: North, South, East, West')
    print('Add to Inventory: get item name')


# empty inventory list
inventory = []

# dictionary for rooms and items
rooms = {
    'Foyer': {'South': 'Ivy Hall'},  # starting room
    'Ivy Hall': {'North': 'Foyer', 'South': 'Cellar', 'West': 'Red Hall', 'East': 'Yellow Hall',
                 'item': 'Bloody Grimoire'},
    'Red Hall': {'East': 'Ivy Hall', 'item': 'Bloody Axe'},
    'Yellow Hall': {'West': 'Ivy Hall', 'item': 'Bloody Cane'},
    'Cellar': {'North': 'Ivy Hall', 'West': 'White Hall', 'East': 'Black Hall', 'South': 'Throne Room',
               'item': 'Bloody Sword'},
    'White Hall': {'East': 'Cellar', 'item': 'Bloody Gun'},
    'Black Hall': {'West': 'Cellar', 'item': 'Bloody Rod'},
    'Throne Room': {'North': 'Cellar', 'item': 'Lady Talanthea'}  # villain room

}

start = 'Foyer'  # starting room
show_instructions()  # calling function
currentRoom = start  # currentRoom will be 'Foyer'

# gameplay loop
while True:
    print('You are in the ', currentRoom)
    print('You have the following items in your bag: ', inventory)
    print('Enter direction you would like to go or "Exit" to leave the game')
    print('**********')
    move = input('Enter direction: ').capitalize()
    if move == 'Exit':
        print('Thank you for playing!')
        break

    if move in rooms[currentRoom]:
        currentRoom = rooms[currentRoom][move]

    else:
        print('You cannot go that way. Please choose another direction')
        continue

    if "item" in rooms[currentRoom]:
        if rooms[currentRoom]['item'] == 'Lady Talanthea' and len(inventory) == 6:  # win condition
            print('Your comrades souls have been freed. Lady Talanthea has been defeated!')
            print('You win!')
            break

    if "item" in rooms[currentRoom]:
        if rooms[currentRoom]['item'] == 'Lady Talanthea': # lose condition
            print('Lady Talanthea has stolen your soul.')
            print('You lose. Try again next time!')
            break


        if ('item' in rooms[currentRoom]) and (rooms[currentRoom]['item'] not in inventory):
            current_item = rooms[currentRoom]['item']
            print('You currently have a ', current_item)
            x = input('Would you like to pick it up? Y/N').capitalize()
            if x == 'Y':
                inventory.append(current_item)  # add items to inventory