# Homework 2: TF-IDF and Regular Expressions

This homework asks you to perform a TF-IDF analysis and use regular expressions to manipulate texts. 

# Goals

In this assignment you will:
* Compute TF-IDF scores for a set of documents, then find the most distinctive words.
* Write regular expressions for grouping and substitution.

# Background

## TF-IDF

We discussed TF-IDF as a metric to find the "most distinctive" words in documents. In this homework, we will compute TF-IDF scores for a set of documents and use that to determine the most distinctive word in each document. 

## NLTK

NLTK is the Natural Language Toolkit, a set of common text-processing tools for Python. You can install NLTK using:

```
> python3 -mpip install --user nltk
```

> Note: if you are using Jupyter Notebook on Scholar to do your assignments, you are going to want to run this command from a terminal window on Scholar (by SSHing to scholar, or opening a terminal window through Thinlinc). Some students have been having trouble trying to install modules using Jupyter Notebook's built-in terminal.

You may find it helpful to reference the code in the *ngram_and_nlp* notebook for examples of using NLTK.

We will use NLTK to clean and *stem* the documents before processing the documents. To clean the documents, we will:

1) Remove *stop words* from each document.
2) Remove punctuation from the document (you may use the `remove_punc` helper method in `helper.py` to help with this).
2) Make the words lower case.
4) Stem the words.

## Regular Expressions

Please refresh your memory of regular expressions using the class notes. You may also find the Python [documentation on regular expressions](https://docs.python.org/3.6/library/re.html) useful.

A few helpful reminders: 

### Testing for Patterns

When you use `re.search` to find a regular expression match, it returns a `Match` object if the pattern exists in the string (we will see more about objects later in Module 4). If *there is no match*, then `re.search` (and `re.match`, `re.findall` and `re.findall`) will return `None`,  which you can test for:

<pre>
p = re.compile('pattern')
if (p.search(s)) :
   # This branch will execute if the pattern is found
else :
   # this branch will execute if the pattern is <b><i>not</i></b> found
</pre>

### Substituting with Functions

A "normal" use of `re.sub` is to substitute one string for another (remember that you can use the *groups* that you match in a pattern as part of your string substitution):

```
s = '456loool789'
p = re.compile('l(o+)l')
print(p.sub('o', s)) #replace "loool" with "o" -> '456o789'
```

You can also call a method instead of providing a replacement string. This method will be called with the `Match` object corresponding to the matched string, and should return a string:

```
def replFun(m) :
    return 'l' + m.group(1).upper() + 'l'

s='looool'
p = re.compile('l(o+)l')
print(replFun(p.search(s))) #replace "looool" with "lOOOOl"
```

# Instructions

## 0) Set up your repository for this homework.

Use the link on Brightspace to clone Homework 2.

The repository should contain several files:

1. This README.
2. Two starter files with some function stubs called `hw2_1.py` and `hw2_2&3.py`. These files also contain test code you can use to test your solutions.
3. A helper file called `helper.py` (this contains code to remove punctuation from a string).
4. A directory, `lecs/` that contains 14 text files. These are the documents you will process for Problem 1.

## Problem 1: TF-IDF

For this problem, we will compute the tf-idf scores for all the terms in each document in the `lecs/` folder.

Fill in the missing functions in `hw2_1.py`, according to their specifications. You may find the lecture notes on *ngrams* helpful for thinking about the format of the doc-word matrix, and the notebook *ngrams_and_nlp* helpful for learning how to use nltk.

Note that even after installing nltk and importing it, you may need to add the following below your nltk import statement:
```
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')
```

While we will test you using our own tests, at the end of `hw2_1.py` are some good test cases to check your code as you go. Feel free to uncomment and recomment them where convenient for you as you write the different functions. The output to those should be:
```
*** Testing readAndCleanDoc ***
['let', "'s", 'look', 'wifi', "'s"]
*** Testing buildDocWordMatrix ***
(2, 429)
429
[2. 9. 2. 1. 1. 1. 3. 2. 1. 4.]
["'re", "'s", "'ve", '.11', '1', '1.2', '100', '11', '1997', '1999']
[ 6. 11.  0.  0.  0.  0.  0.  0.  0.  0.]
*** Testing buildTFMatrix ***
[0.00305344 0.01374046 0.00305344 0.00152672 0.00152672 0.00152672
 0.00458015 0.00305344 0.00152672 0.00610687]
[0.01438849 0.0263789  0.         0.         0.         0.
 0.         0.         0.         0.        ]
[1. 1.]
*** Testing buildIDFMatrix ***
[0.      0.      0.30103 0.30103 0.30103 0.30103 0.30103 0.30103 0.30103
 0.30103]
*** Testing buildTFIDFMatrix ***
(2, 429)
[0.         0.         0.00091918 0.00045959 0.00045959 0.00045959
 0.00137876 0.00091918 0.00045959 0.00183835]
[0. 0. 0. 0. 0. 0. 0. 0. 0. 0.]
*** Testing findDistinctiveWords ***
{'lecs/1_vidText.txt': array(['second', 'per', 'megabit'], dtype='<U12'), 'lecs/2_vidText.txt': array(['point', 'router', 'set'], dtype='<U12')}
```

Submit your filled in version of `hw2_1.py`.

## Problem 2: Regular Expression Groups

Consider a regular expression that identifies street addresses, with the format:

1. One or more digits, followed by a space.
2. One or more words, each starting with a capital letter and then followed by zero or more lowercase letters. This will be followed by a space.
3. A road type, one of "Rd.", "Dr.", "Ave." or "St."

So the following are valid street names:

`465 Northwestern Ave.`

`201 South First St.`

Assume that we will only test with valid street names. There will only be 'one valid street name' in a test case. However, there may be other words preceeding or following the valid street name.

*We consider street names to be valid if they satify the above mentioned rubric in problem 2. Hint: Grading test case alert.*

Fill in the function `problem2`. This function should search an input string for any valid street address, then return *just the street name* from that address: not the street number, and not the road type. So if you pass in:

`The EE building is at 465 Northwestern Ave.`

you should return:

`Northwestern`

If you pass in:

`Meet me at 201 South First St. at noon`

you should return:

`South First`

Also, if you pass in:

`Professor Brinton lives on 123 Have No Clue Ave.`

you should return:

`Have No Clue`

**Be careful not to return extra spaces in the return value. You may need to do a little bit of extra processing of the string captured by your group to ensure this. You will receive partial credit for having spaces. Please remove extra spaces for full credit. Hint: A good way to test if you have tailing spaces is to try printing something immediately after the output.**

## Problem 3: Regular Expression Substitution

Fill in the function `problem3`. This function should *garble* addresses by returning the original address but with the street name reversed. For the above two examples, you should return:

`The EE building is at 465 nretsewhtroN Ave.`

`Meet me at 201 tsriF htuoS St. at noon`

(Note that the entire street name is reversed, not word by word).

Two hints:

1. Think about creating three groups in your regular expression. One that captures the street number, one that captures the street name, and one that captures the road type. You can then use those three groups to assemble the appropriate.
2. If you have a string `s`, `s[::-1]` is the reversed string.

You should feel free to write helper functions in `hw2_2&3.py` to help solve this problem.

# What you need to submit

Please submit `hw2_1.py` and `hw2_2&3.py` with all the functions filled in.

# Submitting your code

Push your completed `hw2_1.py` and `hw2_2&3.py` to your repository before the deadline.

