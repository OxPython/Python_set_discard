'''
Created on Jul 9, 2014

@author: viejoemer

HowTo remove a element from a set if this is present?

¿Cómo eliminar un elemento de un set si este está presente?

discard(elem)
Remove element elem from the set if it is present.
'''

#Create a set with values.
s_1 = set([1,2,3])
print("set one", s_1)

#Removing a element if this is present
s_1.discard(1)
print("Element removed",s_1)

#if the element is not present, don't worry
#This is the different with remove()
s_1.discard(555)
print("Nothing happen",s_1)

