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

# My plan for the College Board Create Task

### Program Overview
In our program, we plan on taking an **INPUT** from the **USER**. It will ask for 5 numbers, and then once the numbers are given, we will display **(MIN) (MAX) (AVG)**. The numbers will be put into a list, and once the user selects a button, the procedure will be called and run through the numbers. Then it will display the function result, minimum will display lowest to highest, maximum will display highest to lowest, and average will average the numbers in the list.

### Inputs 
Inputs will be given as prompts for numbers by the users. Should a number not be given, a proper response will be displayed.
int(input("Numbers...etc"))

### Lists 
Lists will be exhibited inside of our code, as the numbers given by the user input will be stored inside a list.
numbers = []

### Procedure 
Procedure for us will be limited by the inputs the user gives, as well as a 5 number limit, and it will be named 'numinput()' which will be called on later.
if number > 100 or number < 0

### Sequencing
Sequencing will be shown in the 'for' loops that will be inside our functions, having 'if' and 'else' statements in proper ordering to determine things like the highest number in a list, the lowest number, and when to add to i to go through the list.

### Selection 
Selection will be shown in our 'if ' and 'else' statements, to select if a certain variable will be chosen to go in the front of a list (min/max).

### Iteration
Iteration will be shown by going through each element inside of our lists using the 'for i in range'

Inputs from our users will be run through our procedure, which's output will be called to finally print it to the user. This output will be determined by the user input, and will vary depending on what numbers are put in. This will be put into our games page as a PBL project.

### Commits so far

### Reem Written Response
Our plans for the written responses are encapsulated by our Initial create task project overview, and explaining how the program implements into our project's games page, the procedures the user input goes through to return the output, and explains how the numbers they give play a role in the output.
## 3a
- In our program, we plan on taking an **INPUT** from the **USER**. It will ask for 5 numbers, and then once the numbers are given, we will display **(MIN) (MAX) (AVG)**. For the video, we will do 1 run for each output of the program after a user input. This will be showing the inputs going into a list, then showing iteration for going through the lists, selection to display if a number is the lowest or highest then sequencing to check each number. The input is the user giving numbers, and the output will essentially show which number was the highest number, which one was the lowest number, and what the average for all of those numbers were.
## 3b
- `
let list = document.getElementById("list");
var li = document.createElement("li");
            li.textContent = input.value;
list.appendChild(li);
`
The name of the list is list

The data in the list shows the numbers that the user inputs and is used to find values

Without the list the code wouldn't display any of the numbers the user input, as well as not be as user friendly.
## 3c
- `
add.addEventListener("click", function()

if(min > input.value) { //compare input to min
                    min = input.value;
                }
                if(max < input.value) { //compare input to max
                    max = input.value; //enteredNumber;
                }
`
The main function that does the the algorithms is named function(). Sequencing is shown by every input is gone through to check if it's lower or greater than the previous number. Selection is then performed if it is less or greater than to make it the bigger/smaller number. Then finally, the iteration is performed with every single "click" event. With every click of submitting a number the process is repeated again showing iteration.

`
<input type='number' id='input'>
<input type='button' value='add to list' id='add' disabled="disabled">
`
This is the HTML where the javascript functions are "called". It is called whenever the input is put in and the submit button is pressed. Once this happens the javascript function is run. Essentially, our algorithm takes each input from a user and adds it to a variable called count and sum. Count is the total numbers in the list and Sum is the sum of the numbers in the list. It also then makes the min and max temporarily the first input number. After more numbers are added, the each get compared to the first number, and if they the highest or lowest value out of the previous numbers, they are set to min or max. After all that happens, finally average is calculated by taking sum/count.
## 3d
- 
`
function minvar() {
     alert("Min:" + min);
        }
function maxvar() {
     alert("Max:" + max);
        }
function avevar() {
     alert("Avg:" + avg);
        }
`
`
function enableDisable() {
            if(this.value === ""){
                add.disabled = "disabled";
            } else {
                add.removeAttribute("disabled");
            }
        }
`
In the first call, the functions are calling for the outputs from function() and displaying it on the screen with alert. This is testing for the "min max avg" values that were calculated in function(). This will then display them once the button is pressed and called from the HTML buttons.

In the second call, the function is getting the output from function() to say that the function has stopped running. This call is testing to make sure the function has stopped running, then it will reset the function so it can be run multiple times.
