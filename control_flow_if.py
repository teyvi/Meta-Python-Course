#control flow talks about the order inwhich the program runs e.g of flows conditional (if, else, if else) loop(for , while)

#conditional statement
total_bill = 145
discount1 = 10
discount2 = 20

if total_bill > 100 and total_bill < 200:
    print("Bill is greater that 100!")
    total_bill = total_bill - discount1
elif total_bill > 200:
    print('Bill is greater than 200')
    total_bill = total_bill - discount2

else:
    print("Bill is less than 100")

print("Total bill: " + str(total_bill))

#switch statement helps create readable codes unlike if elif that get complex with many conditions

http_status = 401
match http_status:
    case 200 | 201:
        print('Success')
    case 400 | 401:
        print('Bad Request')
    case 500 | 501 :
        print('Server Error')
    case _:
        print('Unknown')


#using loops to iterate in a sequence and access each item in the sequence
