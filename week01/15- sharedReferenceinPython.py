x=5
y=x
'''
x-->5<----y
When Python looks at the first statement,
what it does is that, first, it creates an object to represent the value 5. 
Then, it creates the variable x if it doesn't exist and made it a reference 
to this new object 5. The second line causes Python to create the variable y,
and it is not assigned with x, rather it is made to reference that object that x does.
The net effect is that the variables x and y wind up referencing the same object. 
This situation, with multiple names referencing the same object, 
is called a Shared Reference in Python. Now, if we write:
'''
x="aya"
print(y)

'''
x---->"aya"
5
y----->10
This statement makes a new object to represent 'aya' and makes x to reference
this new object.
However, y still references the original object i.e 5.
Again if we write one more statement as:
'''
y = 10
'''
This statement causes the creation of a new object and made y
to reference this new object.
The space held by the prior object is reclaimed if it is no longer referenced,
that is, the object's space is automatically thrown back into the free space pool, 
to be reused for a future object. 
This automatic reclamation of object's space is known as Garbage Collection.
'''