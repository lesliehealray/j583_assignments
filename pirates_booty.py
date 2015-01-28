#!usr/bin/env python
import random


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
	total = beginning_loot * money_bag
	difference = (beginning_loot * money_bag) - beginning_loot
	print 'As you climb into the boat, you find a bag of money.'
	if total > beginning_loot:
		print 'Your loot has increased by %d for a grand total of %d' % (difference, total)
	elif total < beginning_loot:
		print 'You found one hungry money bag.'
	else:
		bonus_coins = 18 ** 5
		print 'No money, just sand. What sour luck you have matey!'
		print 'However, while you were admiring the ocean view, you discover another bag floating.' 
		print 'You pick the bag and open it up to discover {0:,} of bonus coins'.format(bonus_coins)
		#string formatting
