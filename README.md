# SAT solver for Sudoku - Project 1 (SAT)

## Usage
The following script will run a Dockerized instance of the SAT solver:
`./SAT -SN INPUT_FILE`

If this does not work, go into the `./src` folder and run `./SAT -SN INPUT_FILE` to directly call the Python (3.6) sript.

Or e.g. for Strategy 2:
`./src/SAT -S2 'sudoku.cnf'`

## Strategies
The following strategies are implemented (with their corresponding -S flags):
- Random (1)
- Grab First (2)
- DLIS (3)
- RDLIS (4)
- One-Sided Jeroslow-Wang (5)
- Two-Sided Jeroslow-Wang (6)


The deadline for the SAT project will be 1st of March (= the end of week 4 in the course). Details of how to hand in your results will follow. 

### Part I: building a SAT solver

Your challenge is to write a SAT solver, and then use it to solve Sudoku problems. If you are unfamiliar with the rules of a Sudoku puzzle, read up on them here,  (Links to an external site.)Links to an external site.or many other places on the Web.

Writing a SAT solver for Sudoku's requires that you
1. write a SAT solver that can read DIMACS input. See the slides from the first lecture on propositional logic, or here (Links to an external site.)Links to an external site.; feel free to ignore the "c" and "p" lines. 
2. encode the Sudoku rules as clauses in DIMACS format. You get these for free here. (Links to an external site.)Links to an external site. Suggestion: make sure you understand what the different lines of this file mean. You will need this later. 
3. encode a given puzzle in DIMACS format. One example of a puzzle is here.  (Links to an external site.)Links to an external site. (again, make sure you understand what the different lines mean).
4. give (2)+(3) as input to (1) and return the solution to the given puzzle. This output should again be a DIMACS file, but containing only all 81 unit clauses.

Your SAT solver should implement at least three different strategies: the DP algorithm without any further heuristics, plus two different heuristics of your choice. These can be some of the heuristics discussed in the lectures, or any other heuristic you can find in the literature (or that you make up yourself, for that matter). Points will be awarded for how sophisticated the strategies are that you choose to implement, but you must implement two different strategies as well as the basic DP algorithm itself.

Of course, your SAT solver must be fully general, in the sense that it is an algorithm to solve not only Sudoku's formulated in SAT, but any SAT problem (at least in principle, given enough time and memory).

We give you a collection of 22000 Sudoku's (Links to an external site.)Links to an external site. to test your SAT solver on. These are all in an obvious notation: each line of 81 characters is one puzzle, with a '.' representing an empty square. Obviously, you will need a trivial script to turn such a line into a DIMACS file. 

You are free to choose any programming language you fancy, but we must be able to run your SAT solver with the command SAT -Sn inputfile , for example: SAT -S2 sudoku_nr_10 , where SAT is the (compulsory) name of your program, n=1 for the basic DP and n=2 or 3 for your two other strategies, and the input file is the concatenation of all required input clauses (in your case: sudoku rules + given puzzle). 


### Part II: experiment

After you've implemented your SAT solver, we want you to formulate some hypothesis about its behaviour, and then design and execute an experiment to test this hypothesis. 

Examples of possible hypotheses would be:
1. our strategy 3 outperforms strategy 2, which outperforms basic DP
2. Sudoku's with fewer givens are harder, with a linear correspondence between number of givens and runtime
3. Sudoku's which are hard for people are also hard for our SAT solver (see here (Links to an external site.)Links to an external site. for an example set, also in other places on the Web)
4. We've encoded the rules of a hypersudoku in DIMACS format, and our hypothesis is that solving the same puzzle under hypersudoku rules will be harder than solving it under the normal sudoku rules
5. We've encoded the rules of 2x2, 4x4 and 9x9 sudokuo's in DIMACS format, and our hypothesis is that difficulty increases quadratically with the size of the Sudoku. (there is a rich set of Sudoku variations, see eg here (Links to an external site.)Links to an external site., and many other places on the Web)

(to avoid confusion: the above hypotheses are not necessarily true, they are just examples of the kind of hypotheses we expect).

Clearly, testing these and other hypotheses require that you can somehow measure the performance of your SAT solver. Runtime is of course one measure, but it's also rather uninformative. More informative is to instrument your SAT solver with metrics on the search space it traverses, on the number of backtracks it has to do, on the number of conflicts it encounters, on the number of unit-clauses and pure-literals it resolves, etc. It's up to you to decide which metrics are informative and relevant for your particular hypothesis and experiment. 
A note on runtime: we don't care about the actual runtime, which will depend on how clever you are as a programmer, which programming language you use, and how much money you spend on a machine. Instead, we only care about the relative runtimes of your SAT solver under different experimental conditions. 

Points are awarded for the originality of your hypothesis and for the thoroughness of the design and execution of your experiment. 

### Part III: report

Write a report of max 5 pages where you describe
1. the important design decisions for your SAT solver (both how and why)
2. which heuristics you implemented (and how and why)
3. your hypothesis (plus motivation why it is interesting and plausible)
4. your experimental design (which experimental conditions do you test, which test set do you use, which metrics are you measuring, and why)
5. your experimental results (consider including plots or graphs or bar charts, and to test for statistical significance of your results)
6. the conclusion about your hypothesis that you draw from your results (and why) 

Points are awarded for clarity of your argumentation, and quality of the writing and presentation. 

### What to hand in

You hand in a single zip-file with 
- all your source code, plus a compiled and executable version of your 'SAT' program (as per the specs above)
- your report as a PDF file. 

Use your student numbers to name the zip file, as follows: 371630_973934.zip
