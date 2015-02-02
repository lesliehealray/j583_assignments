# #!usr/bin/env python
import random

# Function will print slug like an actual slug
def print_treasure(symbol):
    treasure = []
    #Generate rows with length of 3
    for row in range(3):
      # Append a blank list to each row cell
      treasure.append([])
      for column in range(3):
        # Assign x to each row for 3 x's in each list
        treasure[row].append(symbol)    
    for row in treasure:
        print " ".join(row)

def treasure_amount():
    loot_bag = random.randrange(1, 3)
    if loot_bag % 2:
       print_treasure('$')
       print "Congratulations! You've found treasure!!!"
       new_balance = treasure * total
       print 'Your loot has increased %d times for a grand total of %d' % (treasure, new_balance)
    else:
        print_treasure('X')
        new_balance = total - 10
        print "So sorry. You've found a money sucker. Your loot is now %d" % new_balance

print "Welcome to Pirate's Booty! The game that can make you rich!"

name = raw_input('What is your Pirate Name?>>')
print "Your name is Pirate %s" % name
beginning_loot = len(name) * 3.14 
print "Congratulations! Your name has granted you %s of pirate loot" % beginning_loot
print "Pick your next step from the choices below"
choices = [
    "Grab your loot and spend it on hookers and cheap booze.",
    "Hop on the boat and sail to Treasure Island",
    "Give your loot to some poor lonely soul",
]

for i, choice in enumerate(choices, start=1):
    print '%d . %s' % (i, choice)

journey_pick = raw_input("NOW PICK A NUMBER BETWEEN 1 AND %s? >>" % len(choices))

valid = False
while not valid:
    try: 
        journey_pick = int(journey_pick)
        if journey_pick <= len(choices):
            valid = True 
    except ValueError: 
        valid = False
    
    finally:
        if not valid:
            print 'Read the instructions and try again matey!' 
            journey_pick = raw_input('NOW PICK A NUMBER BETWEEN 1 AND %s? >>' % len(choices))

if journey_pick == 1:
    print "Game Over! You've spent your money and now have a strange itch."
elif journey_pick == 3:
    beginning_loot = 0
    print "You've been robbed and feel like a loser."
else:
    money_bag = random.randrange(0, 9)
    treasure = random.randrange(1,9)
    total = beginning_loot * money_bag
    difference = (beginning_loot * money_bag) - beginning_loot
    print 'As you climb into the boat, you find a bag of money.'
    if total > beginning_loot:
        print 'Your loot has increased by %d for a grand total of %d' % (difference, total)
    elif total < beginning_loot:
        print 'You found one hungry money bag.'
    else:
        print 'No money, just sand. What sour luck you have matey!'
    
    print 'However, while you were admiring the ocean view, you discover another bag floating.' 
        #print 'You pick the bag and open it up to discover {0:,} of bonus coins'.format(bonus_coins)
    print 'You open the bag up'
    print treasure_amount()    
    print "So you carry onward and after several hours, you finally reach the edge of Treasure Island." 
    print "You're thristy and tired and enter a nearby shack where you enjoy a frosty cold one."
    print "After you finish the very last drop, you start to feel sleepy. Little faires begin to fly around your head."
    print "he bartender tells you that only the lucky mateys react this way when they drink the cold frosty ones."
    print "He begins to lead you to the back room to rest. You trip on a floor board. "
    print "You pull the wooden slat up and discover a box."
    answer = raw_input('Do you open the box? Type yes or no  >>').lower()
    if answer == 'yes':
        print treasure_amount()
    else:
        print "Hastily you leave the shack." 
        print "You come upon a basket of food. You are very hungry."
    foods = ['apple', 'pizza', 'hogie sandwich']
    print "Do you choose "
    for i, food in enumerate(foods, start=1):
        print '%d . %s' % (i, food)

    print "The Universe has frozen. You are suspended in time. More adventure awaits when this has been resolved."

#food_choice = raw_input("Which food do you choose to eat %s? >>" % len(foods))



