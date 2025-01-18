#adding an input function to display 
input('Please enter a number')

num = input('Please enter a number: ')

#using print to output input
print(num)

#taking multiple inputs
home_phone = input('Please enter your home phone number: ')

cell_phone = input('Enter your cell phone number: ')
print(home_phone, cell_phone)

#concatenate inputs
date_of_birth = input('enter your year of birth: ')

present_year = input('enter your present year: ')

print("Your age is" , int( present_year )- int(date_of_birth))