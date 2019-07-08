'''
a)
You're to write a function called saffirSimpson().
This takes in 2 args, i.e. speed and units.
saffirSimpson(speed, units).
Use case:
saffirSimpson(25, 'miles')
saffirSimpson(25, 'kilometers')
Now a user may enter something invalid like:
saffirSimpson('bob', 'centimeter')
This will cause an error if you don't handle this kind of exception.
(Note: Exception handling(try/catch block) is not allowed,
If statements are not allowed,.. read the top of the picture to see more of things not allowed)
Now how you handle the "exception" or error if a user enters the wrong argument is up to you,
However, your function must respond to both good arguments(correct inputs) and bad arguments(incorrect inputs).
The response must take form like this:
-if user enters both arguments correctly:
function returns ["Inputs are all valid", type of hurricane]
-if user enters one argument incorrectly, say the speed argument,
function returns ["Speed not a positive whole number", ' ']
Yeah- second element of the list must be an empty string, whenever the user enters bad input or incorrect argument.
Tip:- store all the response for user inputs (I.e. "Inputs are all valid", "Speed not a positive whole number"...) In a list and access them by using list indexing.
What happens when the user enters good arguments?
say user enters speed as 75, and "miles" as units..
In that case you have to check the range of values for miles,
That's why I sent a picture showing the range of values in an if statement.
in miles:
If speed is less than 74,
Then the result is 'Not a hurricane'
If speed is less than or equal to 95,
Then the result is 'Category 1- very dangerous...'
And like that..
say user enters speed as 75, and "kilometers" as units..
Your function must evaluate like the above, but this time using kilometers'  range, (it's also in the picture i sent)
Now when all is said and done, and the user inputs good arguments,
E.g saffirSimpson(73, 'miles'),
Your function should return a list like this:
['Inputs are all valid', 'Not a hurricane']
Tip:- store the values 'Not a hurricane', 'Category 1-very dangerous...'... In a list and use list indexing to access each of them.
-use while loops to test a condition
-use while loops to return a a value(you must include 'break' after the return statement')
(b)
main()
main() simply prompts the user to enter a value for speed and units and calls the saffirSimpson() function to handle the inputs.
You can use if statements in main.
Also, in main()
Whenever there's bad input, instead of returning a list like:
['Speed not a whole number', ' ']
Return only the error message,
And when inputs are good,
Instead of returning a list like:
['Inputs are all valid", "Not a hurricane"]
Return only the result  "Not a hurricane".
'''


def saffirSimpson(speed, units):
    cond_list= ['Inputs are all valid', 'Speed not a positive number', 'The unit must either be miles or kilometers', 'Both inputs are not valid',
                'Not a hurricane', 'Category 1- Very dangerous wind will produce some damage.', 'Category 2- Extremely dangerous wind will cause extensive damage.',
                'Category 3- Devastating damage will occur.', 'Category 4- Catastrophic damage will occur.', 'Category 5- Catastrophic damage will occur.']
    speed = 0

    while units == 'miles' and speed < 74 and sped.isdigit() == 1:
        print(cond_list[0], cond_list[4])

    while units == 'miles' and speed <= 95 and sped.isdigit() == 1:
        print(cond_list[0], cond_list[5])

    while speed <= 110 and units == 'miles' and sped.isdigit() == 1:
        print(cond_list[0], cond_list[6])

    while speed <= 129 and units == 'miles' and sped.isdigit() == 1:
        print(cond_list[0], cond_list[7])

    while speed <= 156 and units == 'miles' and sped.isdigit() == 1:
        print(cond_list[0], cond_list[8])

    while units != miles and sped.isdigit() == 0:
        print(cond_list[3])

sped = input('Enter the speed of the hurricane: ')
speed = int(sped)
units = input('Enter the units in miles or kilometres: ')
saffirSimpson(speed, units)
