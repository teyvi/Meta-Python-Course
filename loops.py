#looping is a way to iterete over an sequence and access items in the sequence. There to constructs for loop and while loop

#for loops
#variable item is the placeholder for the current item in the sequence and favorites is the name of the sequence

favorites = ['chocolate', 'ice cream', 'cake', 'cookies', 'candy']

for item in favorites:
    print('I love ', item)


#while loop#a counter is declared to end the loop, the counter increment is also added

cars = ['porsche', 'tata', 'tesla','toyota']

count = 0
while count < len(cars):
    print('I like',cars[count])
    count += 1
