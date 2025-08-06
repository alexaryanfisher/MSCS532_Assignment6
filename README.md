# Selection Algorithms and Data Structures
### Medians and Order Statistics & Elementary Data Structures

This repository contains my sixth assignment for MSCS532. This is an Python implementation of fundamental data structures and selection algorithms.

## Project Overview
This project aims to show a comparsion of selection algorithms such as randomized and deterministic with the use of Quickselect and Median of Medians. It also demostrates the implementation of various elementary data structures such as arrays, matrices, stacks, queues, and linked lists.

 * ### Part 1: Selection Algorithms
      This part of the implementations highlights the randomized quickselect algorithm and deterministic selection with Median of Medians. This section also includes a performance comparsion between the two based on the empirical analysis of their running times.

 * ### Part 2: Data Structures
      This part of the project implements the use of an array, matrix, stack, queue, and linked list within Python. The code for this section includes use cases to demostrate their core operations.

## Project Deliverables:
```selection.py``` : Python file containing implementation of selection algorithms such as randomized quickselect and median of medians. 

```datastructures.py``` : Python file containing implementation of elementary data structions as well as their use cases.

```ProjectReport.md```: Report containing the analysis of selection algorithms to include their performance analysis and empirical analysis comparsion. It also contains data structures design choices, use cases, and performance comparison.

## Summary of Findings
In the various parts of the project, there were key insights that outlined the practical performance of selection algorithms and elementary data structures. The project dived into the theoretical time complexities with an empirical analysis of randomized quickselect and deterministic median of medians. The randomized quickselect has an expected time complexity of <em>O(n)</em>. This represented a more efficient performance in practice on the randomly generated data. It was attributed to the simplicity of implementation and lower constant factors. In contrast the deterministic selection algorithm guaranteed an <em>O(n)</em> worst case time complexity. In the observations, it was slower on average in comparison to the randomized quickselect. In the second part of the project, elementary data structures were investigated. It emphasized the distinct efficiencies and tradeoffs of operations for each of the data structures. Arrays and matrices highlighted their <em>O(1)</em> time complexity for random access by index due to their connecting memory allocation. However, their performance degrades to <em> O(n)</em> for inserts and deletions as it requires shifting elements. Stacks implemented with array offer a <em>O(1)</em> for both push and pop operations. For queues, there is a large trade off observed when using arrays. The enqueue operation achieves a <em>O(1)</em>, but the dequeue has a <em>O(n)</em> due to element shifting. Linked lists based queues have been proven to have better performance for these operations. It is due to the use of pointers resulting in a <em>O(1)</em> time complexity. Lastly linked lists have a <em>O(1)</em> time for inserts and deletions as these operations only require pointer adjustments. One of the main drawbacks for linked lists are for random access which achieves a <em>O(n)</em> time complexity due to the need to traverse from the beginning. 


### How to Run Code
* Clone the repository or save all Python files into a folder.
* Open terminal or preferred IDE.
* Navigate and open the save file.
* Run the scripts using a Python interpreter.
