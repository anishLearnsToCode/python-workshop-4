# Python 🐍 Basics Workshop - What After College

![Hits](https://hits.seeyoufarm.com/api/count/incr/badge.svg?url=https://github.com/anishLearnsToCode/python-workshop-4)
[![license](https://img.shields.io/badge/LICENSE-MIT-<COLOR>.svg)](LICENSE)
![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg)
[![hackerrank-python](https://img.shields.io/badge/hackerrank-python-1f72ff.svg)](https://github.com/anishLearnsToCode/hackerrank-python)
[![hackerrank-ds](https://img.shields.io/badge/hackerrank-Data%20Structures-1f72ff.svg)](https://github.com/anishLearnsToCode/hackerrank-data-structures)
[![hackerrank-algo](https://img.shields.io/badge/hackerrank-algorithms-1f72ff.svg)](https://github.com/anishLearnsToCode/hackerrank-algorithms)
[![hackerrank-interview-prep](https://img.shields.io/badge/hackerrank-Interview%20Preparation%20Kit-1f72ff.svg)](https://github.com/anishLearnsToCode/hackerrank-interview-preparation-kit)

<details>
    <summary><b>Workshop Timings</b></summary>
    Workshop Dates: 18th - 19th July 2020 <br>
    Workshop Timings: 9:00 AM - 2:00 PM (9 - 14) <br>
    Break Timings: 11:00 AM - 12:00 AM (11 - 12)
</details>

[Workshop Link (Zoom) 📺](https://us02web.zoom.us/w/86471020059?tk=bpzoH4bzk1J5FYIMQCImiZBFF4q27nnhiNrJS9tgBvQ.DQIAAAAUIhMOGxZlMEZqVFJleVJNR2tvcXhOOXY4X1NRAAAAAAAAAAAAAAAAAAAAAAAAAAAA&pwd=Q1BlYWFiTXkxQ3BKaGxIOHJ2YU9XZz09)
[Class Recordings 📽](https://onedrive.live.com/?authkey=%21AFWm1hA93ZAnykE&id=BD99C9D5BDB4DD2E%2192230&cid=BD99C9D5BDB4DD2E)

## Index
- [Introduction](#introduction)
- [Getting Started with Python](#getting-started-with-python)
- [Day 1](#day-1)
- [Day 2](#day-2)
- [Capstone Project](#hangman-game-capstone-project)
- [Further Reading](#further-reading)
- [Python Books](#python-books-)
- [Future Path??](#future-scope-and-path)

## Introduction
Solutions to all sample problems on HackerRank under the 
[Python domain](https://www.hackerrank.com/domains/python) can be 
looked up [here](https://github.com/anishLearnsToCode/hackerrank-python).

Programming is a very hands process and is both an art as well as a science. We are
engineers and are required to create efficient solutions but at the same time our programs should be 
highly readable and flexible and all the other snappy terms which makes it an art as well.

To become proficient in this art, there are many resources, and books and tutorials. Each has it's merit
and making the first step in any direction is commendable, but the cardinal factor at the end of the day
will be you sitting down (or standing) and writing code. No book or resource can substitute that.

So, what are you waiting for 😀😉 - try as many questions (below or otherwise) as you can.... 🐱‍👤    
Happy Coding :octocat: 🐱‍💻 

You can stalk your instructor on [LinkedIn](https://www.linkedin.com/in/anishsachdeva1998/) &
[GitHub](https://github.com/anishLearnsToCode).

## Getting Started With Python
We need to install and configure a few things before we can write and run any Python code. To write Python code we 
need the Python interpreter on our machine.

### 1. Install the Python 3 Interpreter
To write python programs on your machine we need the Python interpreter. There are 2 popular versions of Python 
out there right now Python 2 and Python 3. There are breaking changes between these versions and this course will be 
taught in Version 3. So as long as you have python version 3.{something}.{something} you're good to go 🙂

Download python from [this website](https://www.python.org/downloads/) 🌐. 

To check that python has been correctly installed on your machine run the following command on your terminal:
```shell script
python --version
```

It should have an output akin to:
```shell script
Python 3.8.3 
```

Once that Python has been successfully installed, we need to install a code editor or IDE so that we can write 
programs and run them. I suggest using __VS Code__ if you prefer a Code editor over an IDE (or if you don't know the
difference between Code editor and IDE 😉). using a code editor will aso be less intensive on computing resources.

I personally prefer the __JetBrains PyCharm__, but warning ⚠ it is a heavy software and might not run properly on 
all machines (especially laptops that are constrained for resources).

### 2. Installing VS Code (or go to step 3 - Installing PyChamr)
1. Download the setup from [here](https://code.visualstudio.com/).
2. Run the setup which is pretty straight forward. Just click next like 10 times and voila!

### 3. Installing JetBrains PyCharm
1. You can either install the educational edition (free) from [here](https://www.jetbrains.com/pycharm-edu/).
2. Or you can create an account on JetBrains if you have a university email address and then install the 
    [JetBrains Toolbox](https://www.jetbrains.com/toolbox-app/).
3. You can easily manage JetBrains IDE's and projects using the ToolBox app. From the ToolBox app you can now install
    either IntelliJ PyCharm Edu Edition or Ultimate Edition.    

### 4. Installing git (Optional - Only required for Windows users)
This is an optional step of your getting started guide and can be skipped. Although installing git and using it
in your projects is highly recommended. For a learning path to learn git have a look at the 
[Future Path + Scope](#future-scope-and-path) section.

Install git from the [git-scm](https://git-scm.com/downloads) website. Run the setup and click next like 10 times
and use the recommended settings for installation. 

There will be a section when it will ask the standard text editor and gie you an option between _Vim_ and _nano_. 
If you are not familiar with _Vim_ then opt for _nano_.

__IMPORTANT__ Opt for _nano_ if not familiar with _Vim_.

To check your installation of git check that git bash has been intalled and run the following command on your 
terminal.
```shell script
git --version
```

The output should be akin to 
```shell script
git version 2.24.1.windows.2
```

### 5. Writing your first Python Program
Open your text editor/IDE and create a new file `hello_world.py` and in that file copy paste the following code 
snippet.
```python
print('hello world !')
```

To run the code navigate to file in terminal and run the following commands.

```shell script
python hello_world.py
>>> hello world !
```

## [Day 1](https://github.com/anishLearnsToCode/python-workshop-4/tree/master/day1)
### Topics Covered
- [Hello World](day1/hello_world.py)
- [Comments](day1/comments.py)
- [Strings](day1/strings.py)
- [Variables](day1/variables.py)
- [User Input](day1/user_input.py)
- [Taking Integer Input](day1/int-input.py)
- [Arithmetic Operations](day1/arithmetic_operators.py)
- [Arithmetic Operator short Hand](day1/operator_short_hand.py)
- [logical Operators](day1/logical_operations.py)
- [If Else Statements](day1/if_else_statements.py)
- [Ternary Operator](day1/ternary_operator.py)
- [Finding if Number is even or odd](day1/even_odd.py)
- [Hackerrank If Else Question](day1/python_if_else.py)
- [While Loop](day1/while.py)
- [Range Object](day1/range_object.py)
- [For Loop](day1/for_loop.py)
- [Sum N Natural Numbers](day1/sum_n_natural_numbers.py)
- [Factorial](day1/factorial.py)
- [Loop Control Statements](day1/loop_control_statements.py)
- [Functions](day1/functions.py)
- [Factorial Function](day1/factorial_function.py)
- [Lists](day1/lists.py)

### Sample Questions
| Question | Solution Link |
|:---------|:--------:|
| [Say "Hello World" With Python](https://www.hackerrank.com/challenges/py-hello-world)| [Solution](https://github.com/anishLearnsToCode/hackerrank-python/blob/master/introduction/SayHelloWorldWithPython.py) |
| [Python If-Else](https://www.hackerrank.com/challenges/py-if-else) | [Solution](https://github.com/anishLearnsToCode/hackerrank-python/blob/master/introduction/PythonIfElse.py) |
| [Arithmetic Operators](https://www.hackerrank.com/challenges/python-arithmetic-operators) | [Solution](https://github.com/anishLearnsToCode/hackerrank-python/blob/master/introduction/ArithmeticOperator.py) |
| [Python Division](https://www.hackerrank.com/challenges/python-division) | [Solution](https://github.com/anishLearnsToCode/hackerrank-python/blob/master/introduction/Division.py) |
| [Loops](https://www.hackerrank.com/challenges/python-loops) | [Solution](https://github.com/anishLearnsToCode/hackerrank-python/blob/master/introduction/Loops.py)|
| [List Comprehensions](https://www.hackerrank.com/challenges/list-comprehensions) | [Solution](https://github.com/anishLearnsToCode/hackerrank-python/blob/master/basic-data-types/ListComprehension.py) |
| [Find the Runner-Up Score](https://www.hackerrank.com/challenges/find-second-maximum-number-in-a-list) | [Solution](https://github.com/anishLearnsToCode/hackerrank-python/blob/master/basic-data-types/FindTheRunnerUpScore.py) |
| [Nested Lists](https://www.hackerrank.com/challenges/nested-list) | [Solution](https://github.com/anishLearnsToCode/hackerrank-python/blob/master/basic-data-types/nested-lists.py) |
| [Finding The Percentage](https://www.hackerrank.com/challenges/finding-the-percentage) | [Solution](https://github.com/anishLearnsToCode/hackerrank-python/blob/master/basic-data-types/finding-the-percentage.py) |
| [Lists](https://www.hackerrank.com/challenges/python-lists) | [Solution](https://github.com/anishLearnsToCode/hackerrank-python/blob/master/basic-data-types/Lists.py) |
| [Tuples](https://www.hackerrank.com/challenges/python-tuples) | [Solution](https://github.com/anishLearnsToCode/hackerrank-python/blob/master/basic-data-types/tuples.py) |
| [sWAP cASE](https://www.hackerrank.com/challenges/swap-case) | [Solution](https://github.com/anishLearnsToCode/hackerrank-python/blob/master/strings/swap-case.py) |
| [String Split and Join](https://www.hackerrank.com/challenges/python-string-split-and-join) | [Solution](https://github.com/anishLearnsToCode/hackerrank-python/blob/master/strings/string-split-and-join.py) |
| [What's Your Name](https://www.hackerrank.com/challenges/whats-your-name) | [Solution](https://github.com/anishLearnsToCode/hackerrank-python/blob/master/strings/whats-your-name.py) |

## [Day 2](https://github.com/anishLearnsToCode/python-workshop-4/tree/master/day2)

### Topics Covered
- [Truthy Falsy Values](day2/truthy_falsy_values.py)
- [List Comprehension](day2/list_comprehension.py)
- [Odd elements sum](day2/odd_elements_sum.py)
- [For Loops on Lists](day2/list_for.py)
- [Taking user input as list](day2/list_input.py)
- [Map Operator](day2/list_input_map.py)
- [Capitalize Hackerrank Question](day2/capitalize.py)
- [Tuples](day2/tuples.py)
- [Dictionary](day2/dictionary.py)
- [Finding Percentage Hackerrank Question](day2/finding_percentage.py)
- [Complex Dictionary Structure](day2/complex_dict.py)
- [Inbuilt Functions](day2/inbuilt_functions.py)
- [MiniMax Sum](day2/mini_max_sum.py)
- [Strings](day2/strings.py)
- [sWAP cASE](day2/swap_case.py)
- [Inbuilt Packages](day2/inbuilt_packages.py)
- [Stock Custom Package](day2/stock.py)

### Sample Questions
| Question | Solution Link |
|:---------|:--------:|
| [Write a Function](https://www.hackerrank.com/challenges/write-a-function) | [Solution](https://github.com/anishLearnsToCode/hackerrank-python/blob/master/introduction/WriteAFunction.py) |
| [Print Function](https://www.hackerrank.com/challenges/python-print) | [Solution](https://github.com/anishLearnsToCode/hackerrank-python/blob/master/introduction/PrintFunction.py) |
| [collections.Counter()](https://www.hackerrank.com/challenges/collections-counter) | [Solution](https://github.com/anishLearnsToCode/hackerrank-python/blob/master/collections/collections-counter.py) |
| [DefaultDict Tutorial](https://www.hackerrank.com/challenges/defaultdict-tutorial) | [Solution](https://github.com/anishLearnsToCode/hackerrank-python/blob/master/collections/default-dict-tutorial.py) |
| [Collections.namedTuple()](https://www.hackerrank.com/challenges/py-collections-namedtuple) | [Solution](https://github.com/anishLearnsToCode/hackerrank-python/blob/master/collections/collections-named-tuple.py) |
| [Collections.orderedDict()](https://www.hackerrank.com/challenges/py-collections-ordereddict) | [Solution](https://github.com/anishLearnsToCode/hackerrank-python/blob/master/collections/collections-ordered-dict.py) |

## Hangman Game (Capstone Project)
The code can be viewed [here](https://github.com/anishLearnsToCode/hangman-cli-game).
Another game 👾 built on Python (this one with actual GUI) can be viewed 
[here](https://github.com/anishLearnsToCode/alien-invasion) 🎮🕹. 

## Further Reading
- [w3 School Python](https://www.w3schools.com/python/)
- [HackerRank python Domain](https://www.hackerrank.com/domains/python)
- [Why is it called Python?](http://www.python.org/doc/faq/general/#why-is-it-called-python)
- [Projects Created on Python](http://www.python.org/about/success)
- [C++ vs. Java vs. Python Language Speed Test (Informal)](https://www.youtube.com/watch?v=C8jeRug6agk)
- [Math Module](https://docs.python.org/3/library/math.html)
- [Stack Overflow Survey 2020](https://insights.stackoverflow.com/survey/2020)
- [Python Example Projects and Project Based Tutorials](https://realpython.com/tutorials/projects/)
- [Django: Web Development on Python](https://www.djangoproject.com/)
- [Falcon: Minimalist Web Framework](https://falcon.readthedocs.io/en/stable/)

## Python Books 📕
- [Python Crash Course](https://github.com/anishLearnsToCode/books/blob/master/python/python-crash-course.pdf)
- [Python in a Nutshell](https://github.com/anishLearnsToCode/books/blob/master/python/python-in-a-nutshell-3e.pdf)
- [Programming Python](https://github.com/anishLearnsToCode/books/blob/master/python/programming-python-4e.pdf)
- [Python For Data Analysis](https://github.com/anishLearnsToCode/books/blob/master/python/python-for-data-analysis-2e.pdf)

## Future Scope and Path
Now that you have learnt the basics of Python and also built an amazing project that showcases
your skills, how to move ahead and learn more? What else could you work on? Here are a 
few suggestions:

### Data Structures and Algorithms
Data Structures and Algorithms is an immensely important topic required for Software development and
is used by organizations for all sizes as a tool for employee hiring and recruitment. To get better
at this I recommend that you practice questions in the 
[Data Structures](https://www.hackerrank.com/domains/data-structures) and 
[Algorithms](https://www.hackerrank.com/domains/algorithms) 
domain on HackerRank and you can have a look at solutions to many of those problems in the 
solution repositories given below.

| Problem Domain | Solution Repository |
|----------------|---------------------|
| [Data Structures](https://www.hackerrank.com/domains/data-structures) | [Solutions](https://github.com/anishLearnsToCode/hackerrank-data-structures) |
| [Algorithms](https://www.hackerrank.com/domains/algorithms) | [Solutions](https://github.com/anishLearnsToCode/hackerrank-algorithms) |

You can views solutions to problems in Python (or any of your preferred programming language)
and you are most welcome to contribute to the repository solutions to unsolved problems 
or solutions in more languages (aka Python). 

You can also try questions on [Leet Code](https://leetcode.com/) and have a look at the 
[solutions repository](https://github.com/anishLearnsToCode/leetcode-algorithms)
and are most welcome to contribute just as above 😀

### Core Python
Before starting of your journey in Data Structures or 
[web development](#web-development) or even 
[machine learning](#machine-learning-)
another good first step can be just developing your core Python skills further so that you are 
familiar with all the different constructs that the language has to offer. That can be done on 
HackerRank in the 
[Python Domain](https://www.hackerrank.com/domains/python) 
and you can have a look at solutions to all the problems
[here](https://github.com/anishLearnsToCode/hackerrank-python).

### Web Development
Python is a very versatile programming language and is being used for all things from biology
to robotics, computer vision and even serve side rendered web applications and api's.
As you are now proficient with the programming language you can start learning a web 
development framework like 
[Django](https://www.djangoproject.com/) or
[Falcon](https://falcon.readthedocs.io/en/stable/).

Django is a have all web development framework and you can even build very large, highly modern
cluster based web sites that can be deployed to scale. You can use it just to create a server-side
API with a separate client facing application or a MVC (Model view controller) based application
that has server side rendering.

Falcon is a relatively light weight web development platform but it is blazing fast ⚡ and that serves
it's own purpose. It can be used to create a super fast very minimalistic server side API's 
and can aso be used to create server side job runners like mail sending and background processing.

You could always use multiple server side frameworks which will give you the perfect opportunity
to use buzz words like docker, kubernetes 🛳, clusters, swarms and add all these buzz words to
your resume 😉. 

### Machine Learning 🔥
Speaking of buzz words... Machine Learning has enjoyed fame of meteoric proportions and there are
plenty of resources to get started with ML and Python has somehow become the defacto language
used in Machine Learning / Deep Learning applications and is being sed by Engineers & 
scientists of many different domains that have written numerous libraries serving various purposes
all around the globe 🌎 which is good for us ☺.

Some popular libraries are:
- [numpy](https://numpy.org/)
- [scikit-learn](https://scikit-learn.org/stable/)
- [tensorflow](https://www.tensorflow.org/)
- [open-cv](https://opencv.org/)
- [pyTorch](https://pytorch.org/)

To get started with Machine Learning I recommend the ubiquitous 
[Machine Learning by Stanford](https://www.coursera.org/learn/machine-learning)
course on [Coursera](https://www.coursera.org) by Andrew Ng.

This may be old but it's essence and relevance haven't dwindled at all. Solutions to all problems
with well written code can be found [here](https://github.com/anishLearnsToCode/ml-stanford).

### Learning Git ![git-scm](https://img.icons8.com/color/25/000000/git.png)
This is not very correlated to Java, but Git is a technology being used by all organizations big and small 
that wish to maintain their code over teams of varied sizes and manage projects. Even this repository which you 
are currently reading in is being maintained by [git]() &
has been deployed on [github]().

Being proficeint with git and version control will help you manage all your projects, be in any language Java,
Python, C++ and even non-programming projects very efficiently and you will be able to easily maintain project 
state over all your devices.

There is an excellent [Version Control with Git](https://www.coursera.org/learn/version-control-with-git) 
course on Coursera by Atlassian or you can even try this 
[Git Introductory 30min Video](https://www.youtube.com/watch?v=SWYqp7iY_Tc)
on YouTube to learn the basics of git.

So, what are you waiting for git started 😁 (bad pun!)
