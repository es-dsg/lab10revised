[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/Ny6nTrGM)
[![Open in Codespaces](https://classroom.github.com/assets/launch-codespace-2972f46106e565e64193e422d61a12cf1da4916b45550586e14ef0a7c637dd04.svg)](https://classroom.github.com/open-in-codespaces?assignment_repo_id=16784750)
# Lab 10 Lottery Number Generator

  _Learning Objectives: Demonstrate understanding of lists and using imported modules (random)_

Many states, like California, use lotteries to raise money for things like public schools and infastructure. 

In this lab you will create a program that generates lottery tickets, either randomly or by allowing the user to enter their own numbers.

## Step 1: Create a function that generates a random lottery ticket
Write a function that takes no parameter and returns a list.

- Use _random_ and _sample_ to generate a list of five unique (meaning no repeats) integers between 1 and 49 inclusive. 
- Append to your list a sixth integer, for the mega number, between 1 and 19 inclusive. This number can be the same as any of the original 5 lottery numbers.
- Return the list.

## Step 2: Create a function that creates a custom lottery ticket
Write a function that takes no parameters and returns a list.

- Get console input from the user for five unique (meaning no repeats) integers between 1 and 49 inclusive.
- Append to your list a sixth integer from the user, for the mega number, between 1 and 19 inclusive. This number can be the same as any of the original 5 lottery numbers.
- Return the list.

Note: if the user enters the same number more than once your program should catch the error and ask for the number again. For example:
```
    Enter your lottery number between 1 and 49: 17
    Enter your lottery number between 1 and 49: 17
    Invalid entry. Number must be between 1 and 49. Numbers cannot be repeated.
    Enter your lottery number between 1 and 49: 29
```

## Step 3: Create the main function
Write the main function. 

Welcome the user and prompt them to select a custom lottery ticket or a random ticket.

```
    Welcome to Python Lotto!
    You have the option to choose your own lottery numbers or have them randomly selected for you.
    Please enter C for custom or R for random: 
```
Depending on their selection your program should then call the appropriate function and output the final results.
```
    Your lottery ticket is: 08 13 37 09 22 (mega 16).
```
## Output Example
Run your program and try out the different options. 
Here is an example for the user choosing a random lottery ticket:
```
    Welcome to Python Lotto!
    You have the option to choose your own lottery numbers or have them randomly selected for you.
    Please enter C for custom or R for random: R
    Your lottery ticket is: 37 24 40 21 03 (mega 19).
```
Here is an example for the user choosing to create a custom lottery ticket:
```
    Welcome to Python Lotto!
    You have the option to choose your own lottery numbers or have them randomly selected for you.
    Please enter C for custom or R for random: C
    Enter your lottery number between 1 and 49: 15
    Enter your lottery number between 1 and 49: 7
    Enter your lottery number between 1 and 49: 42
    Enter your lottery number between 1 and 49: 33
    Enter your lottery number between 1 and 49: 25
    Enter your mega number between 1 and 19: 12
    Your lottery ticket is: 15 07 42 33 25 (mega 12).
```
## Test and Submit 
There are no automated tests for this lab, so throughly test you program with differnt inputs before submitting.  
As always, stop by student hours, send an email, check in with a peer, or stop by the STEM Center if you need any assistance.


