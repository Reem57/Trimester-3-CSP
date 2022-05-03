{% include nav.html %}

Create Task
Requirements:
Input and an Output
At least one list
At least one procedure
At least one algorithm
Idea:
Video
We will submit a video that is:
Less than 1 minute
With no collaboration
No voice, only text captions
Less than 30 MB in file size
.mp4, .wmv, .avi, or .mov format
Video here:
Written Response
Response to prompts 3a-3d
Responses here:

# 3. WRITTEN RESPONSES
## 3.a.i.
 - There is a math problem that mathematicians can't solve called the Collatz Conjecture. The purpose of my program is to
use computer science to try find patterns in the problem and help the mathematicians.
## 3.a.ii.
 - The video demonstrates the math problem being used with different numbers and then outputting the list or the length of
the list just like mathematicians would use the could to decode the problem.
## 3.a.iii.
 - The first input is choosing “Print List” by inputting 1, then I entered the number 19. The output was a list of values “58 29
88 44 22 11 34 17 52 26 13 40 20 10 5 16 8 4 2 1”. The second input is choosing “Input Number to repeat” by inputting 2,
then I entered the number 14. The output was a list of values “0 1 7 2 5 8 16 3 19 6 14 9 9 17 “. The last input is choosing
“Generate a random number to repeat” by inputting 3, then the program displayed “The function is going to run 16 times”
(generates the random number of 16) and outputs the following list of values “0 1 7 2 5 8 16 3 19 6 14 9 9 17 17 4.”
## 3.b.i.
## 3.b.ii.
3.b.iii.
 - The name of the list is myList
## 3.b.iv.
 - The list stores the values of the number after its being multiplied and divided. For example, if my number is 5, the
program will multiply five by three then add one and store the output (“the odd/even program”). 3 * 5 + 1 = 16 so sixteen is
the number that will be stored. This process will repeat (differently for even and odd numbers) until it reaches a value of
one.
## 3 c.
## 3.b.v.
 -Using a list in my code has two major benefits to manage the complexity of the code. One is having the length of the list
“handy” and could be used whenever is needed. The second benefit is that specific values from the list could be identified
easily and used later. If a list wasn’t used, to print the values you would have to have
print(i) instead of myList.append(int(i)). And to have the length of the list you would have to have a separate variable which can be called count.
This variable would have to increase by one each time the loop repeats. So above the while loop, you will have to include
count = 0 and right after the while loop starts you will have to include count = count +1.
## 3.c.i.
## 3.c.ii.
## 3 d.
## 3.c.iii.
 - The function above, logic,is where the main procedure runs. It runs the number of times the user wants it to run using the parameter a
. The function goes through every single integer from two to the selected value a
and runs the “odd/even program.” Then the function outputs the number of times the odd/even program had to be run in
order to get to a value of one. This procedure is used in my program to run the basic logic of the odd/even program while
changing the parameter
a without having to retype the entire program thus I can call it when needed later on.
## 3.c.iv.
 - The algorithm is repeating from 1 to a
(the parameter) + 1 using a for loop since the value 0 can’t be run in the function. Then each time the program runs, it
creates a new list called
myList
to store the outputs generated from the next loop. The next loop is a while loop that basically is the “odd/even program.”
First, it checks if the value is 1 and if it's not then it runs the loop. The procedure then checks if the value is even by
checking if the remainder when the value of
i is divided by two is equal to zero. If it’s even, it divides the value by two and the output is added to myList
using the line myList.append(int(i)). If it’s odd, the procedure multiples the value by three, adds 1, and adds it to the list.
Lastly, it prints the total length of the list using the line print(len(myList), end=” “) and adds a space after.
## 3.d.i.
 - First call:
def test1():
logic(7)
 - Second call:
def test2():
logic(20)
## 3 d.ii.
 - Condition(s) tested by first call:
In this call, the parameter a
is given a value of 7. Meaning that the logic function will repeat 7 times which will display the length of the list 7 times
from the number 1 to 8. The while checks if the value
i is not equal to one. The if statement checks if the value of i
is even or odd and proceeds with the function accordingly. This is repeated 7 times according to the parameter
Condition(s) tested by second call:
In this call, the parameter a
is given a value of 20. Meaning that the logic function will repeat 20 times which will display the length of the list 20 times
from the number 1 to 21. The while checks if the value
i is not equal to one. The if statement checks if the value of i
is even or odd and proceeds with the function accordingly. This is repeated 20 times according to the parameter.
## 3.d.iii.
 - Results of the first call:
0,1,7,2,5,8,16
 - Results of the second call:
0,1,7,2,5,8,16,3,19,6,14,9,9,17,17,4,12,20,20,7
