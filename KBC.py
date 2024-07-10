questions = [
    [
        "1. Who is the father of C language?", "Steve Jobs", "James Gosling",
        "Dennis Ritchie", "Rasmus Lerdorf", 3
    ],
    [
        "2. Which of the following is not a valid C variable name?",
        "int number;", "float rate;", "int variable_count;", "int $main;", 4
    ],
    [
        "3. What is short int in C programming?", "The basic data type of C",
        "Qualifier", "Short is the qualifier and int is the basic data type",
        "All of the mentioned", 3
    ],
    [
        "4. All keywords in C are in ____________", "LowerCase letters",
        "UpperCase letters", "CamelCase letters", " None of the mentioned", 1
    ],
    [
        "5. Which is valid C expression?", "int my_num = 100,000;",
        "int my_num = 100000;", "int my num = 1000;", "int $my_num = 10000;", 2
    ],
    [
        "6. Which of the following cannot be a variable name in C?", "volatile",
        "true", "friend", "export", 1
    ],
    [
        "7. Which keyword is used to prevent any changes in the variable within a C program?",
        "immutable", "mutable", "const", "volatile", 3
    ],
    [
        "8. What is the result of logical or relational expression in C?",
        " True or False", "0 or 1",
        "0 if an expression is false and any positive number if an expression is true",
        "None of the mentioned", 2
    ],
    [
        "9. Which of the following typecasting is accepted by C language?",
        "Widening conversions", "Narrowing conversions",
        "Widening & Narrowing conversions", "None of the mentioned", 3
    ],
    [
        "10. Where in C the order of precedence of operators do not exist?",
        "Within conditional statements, if, else", "Within while, do-while",
        "Within a macro definition", "None of the mentioned", 4
    ],
]

levels = [1000, 4000, 5000, 10000, 15000, 25000, 40000, 70000, 90000, 200000]

money = 0
for i in range(0, len(questions)):
    question = questions[i]
    print(f"\n\n{question[0]}\n")
    print(f" a. {question[1]}   b. {question[2]}\n")
    print(f" c. {question[3]}   b. {question[4]}\n")

    answer = input("Enter your choice: (1-4) or q for quit")
    if (answer == "q"):
        lev=i-1
        if(lev<0):
            print(f"Game quit\nYou won Rs.0")
            break
        else:
            print(f"Game quit\nYou won Rs.{levels[lev]}")
            break
    else:
        if (int(answer) == question[5]):
            print(f"You answer is Corect\nYou won Rs. {levels[i]}")
        else:
            print("You answer is Wrong.\n")
            print(f"Correct option is: {question[5]}")
            if (i >= 3 and i < 9):
                money = 10000

            if (i == 9):
                money = 200000
            print(f"You won Rs.{money}")
            break
