# Random Generator Checker

from random import randrange

def dice_roll_probability(faces, count):
    ''' Rolls a dice with given number of faces given number of times.
        Then will divide total count to show % of each faces thrown.

        >>> dice_roll_probability(6,10)
	      [0.1, 0.1, 0.2, 0.1, 0.1, 0.4]
	      >>> dice_roll_probability(6,100)
	      [0.16, 0.21, 0.16, 0.1, 0.2, 0.17]
	      >>> dice_roll_probability(6,1000)
	      [0.177, 0.166, 0.197, 0.149, 0.149, 0.162]
	      >>> dice_roll_probability(6,10000)
  	    [0.1631, 0.1714, 0.1637, 0.1705, 0.1651, 0.1662]
  	    >>> dice_roll_probability(6,100000)
	      [0.16703, 0.16702, 0.16746, 0.1674, 0.16324, 0.16785]
  	    >>> dice_roll_probability(6,1000000)
  	    [0.167088, 0.165978, 0.166467, 0.166525, 0.167106, 0.166836]
  	    >>> dice_roll_probability(6,10000000)
	      [0.1667358, 0.166748, 0.1665631, 0.1665952, 0.1667036, 0.1666543]

      	As you can see, actual run probability nears theoretical percentage
        as number of rolls increase
    '''
    rolls = [randrange(1, faces+1) for i in range(count)]
    return [rolls.count(i) / float(count) for i in range(faces+1)][1:]
