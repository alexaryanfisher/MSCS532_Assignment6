# <center> Project Report - Medians and Order Statistics & Elementary Data Structures </center>
### <center> by Alexa Fisher </center>
<br>
This report aims to review the importance of order statistics, medians, and data structures. It will provide a detailed overview of the performance analysis for deterministic and randomized selection algorithms in terms of time complexity and space complexity. In the latter part of the report elementary data structures are analyzed via a performance analysis and practical applications are represented. The combination of topics will provide a deeper understanding of these algorithmic concepts.

## <center>Part I. Selection Algorithms Analysis: Randomized and Deterministic </center>
## <center>Performance Analysis </center>
### Time Complexity
The time complexity of the selection algorithms can be differing depending on the type. The two algorithms that are being reviewed are randomized quickselect and the deterministic median of medians. The time complexity for randomized quickselect is <em> O(n)</em> (Reddy, 2021). In this algorithm, in each recursive call it partitions the array and only continues with only one of the subarray (Reddy, 2021). The best-case recurrence relation for this is <em>T(n) = T(n/2) + O(n)</em>, which results in <em> O(n)</em>. In contrast, the worst case would have a recurrence relation of <em>T(n) = T(n-1) + O(n)</em>, which results in <em> O(n^2)</em>. The deterministic median of medians worst case would have the same time complexity of <em> O(n)</em> (Eberl, 2017). This algorithm selects the pivot that guarantees an optimal partition. It divides the array into groups of five and locates the median of each of the groups. It recursively calls and identifies the median of the medians (Cormen et al, 2022). It serves as the pivot. This can be represented as the recurrence relation of <em>T(n) <= T(n/5) +T(7n/10) +O(n)</em>, which solves to <em> O(n)</em> (Cormen et al, 2022).

### Space Complexity
The space complexity of selection algorithms are highly dependent on their recursive calls. In the randomized quickselect, the average case space complexity is <em> O ( </em>log<em> n)</em> due to the recursion stack partitioning the array into somewhat equal halves (Cormen et al, 2022). In the worst case when the pivot leads to unbalanced partitions the space complexity will downgrade to <em>O(n)</em>. In comparison, the deterministic selection as a worst case space complexity of <em>O(n)</em>. The algorithm involves creating temporary arrays when splitting into groups and the recursive calls during the partitioning. These features make it less space efficient but provides guaranteed linear time performance (Cormen et al, 2022).

## <center> Empirical Analysis </center>
### Observation
The empirical analysis of the selection algorithms confirms the theoretical findings. On the randomly generated data, the randomized quickselect had a faster running time in practice. In the deterministic algorithm, it was slower due to the overhead of partitioning, grouping, sorting the grouped arrays, and recursively finding the median of medians. This was strongly observed in the below Figure 1.

<strong> Figure 1</strong>
<br>
<strong><em>Deterministic and Randomized Selection Algorithm Comparsion Results</em></strong>

         Performance Testing of Selection Algorithms.

        Testing for array size: 1000
        Finding the 1-th smallest element.
        Finding the 500-th smallest element.
        Finding the 999-th smallest element.
        Randomized Quickselect: 0.3509000000576634 ms.
        Median of Medians: 0.28859999997621344 ms.

        Testing for array size: 10000
        Finding the 1-th smallest element.
        Finding the 5000-th smallest element.
        Finding the 9999-th smallest element.
        Randomized Quickselect: 0.8519000000433152 ms.
        Median of Medians: 3.004899999950794 ms.

        Testing for array size: 50000
        Finding the 1-th smallest element.
        Finding the 25000-th smallest element.
        Finding the 49999-th smallest element.
        Randomized Quickselect: 3.1347999999979947 ms.
        Median of Medians: 17.278399999895555 ms.

        Testing for array size: 100000
        Finding the 1-th smallest element.
        Finding the 50000-th smallest element.
        Finding the 99999-th smallest element.
        Randomized Quickselect: 7.799299999987852 ms.
        Median of Medians: 28.78950000012992 ms.

## <center>Part II. Elementary Data Structures </center>

## <center>Performance Analysis </center>
### Time Complexity
Data structures have different time complexities  and tradeoffs. The below chart, Chart 1,  provides a visual representation of the various data structures

<strong>Chart 1</strong>
<br>
<strong><em>Elementary Data Structures Time Complexity</em></strong>
<br>
| Data Structure |   Operation   | Time Complexity |
|--------------- | --------- | --------------- |
| Array & Matrices |  Access | <em>O(1)</em>|
| | Insert / Delete |<em>O(n)</em>|
| Stack | Push / Pop | <em>O(1)</em>|
| Queue | Enqueue | <em>O(1)</em>|
|  | Dequeue | <em>O(n)</em>|
| Linked List | Access | <em>O(n)</em>|
| | Insert at Start | <em>O(1)</em>|
|  | Insert at End | <em>O(n)</em>|

### Array vs Linked Lists - Trade-offs and Comparison Analysis
There are distinct tradeoffs in performance and efficiency when using arrays or linked lists for implementing stacks and queues. For stacks, an array-based implementation is ideal because both the push (adding element) and pop (removing element) operations can be performed at the end of an array. This typically provides <em>O(1)</em> time complexity. With connecting memory allocation of the array allows for direct access to the top element. However, the same is not true for queues and the tradeoffs are more noticeable. The enqueue operation of adding to the back has the same time complexity as push, <em> O(1)</em>. It is not the case with dequeue operation of removing from the front, which has a time complexity of <em>O(n)</em>. It is due to shifting all the subsequent elements to fill the empty space. Queues would have better performance with linked lists as it can achieve <em> O(1)</em> time complexity for both the enqueue and dequeue operations. It is achieved by the use of pointers to the head and tail so that elements can be added to one end and removed from another without the need for shifting.

## <center>Practical Applications </center>
There are practical applications for each of the data structures in real world scenarios. This is shown below.
- <strong> Arrays & Matrices:</strong> Arrays provide simplicity and a <em>O(1)</em> random access time.This would be ideal for storing data that needs to be fast or require random access by index capabilities. A good example would be spreadsheet applications. 
- <strong>Stacks: </strong> Stacks operate in a last in first out approach. It is used in function call stacks to manage program executions. It would be ideal for undo and redo functionality in software. An array-based stack provides a <em>O(1)</em> for push and pull operations that provide better cache performance due to contiguous memory allocation.
- <strong>Queues: </strong> Best used for managing resources that require a sequential order. This data structure as a first in first out approach. A good example would be printing job scheduling.
- <strong>Linked Lists: </strong> Ideal for cases needing frequent inserts or deletes at beginning or end of sequences. Linked lists have a higher memory overhead due to the storage required for pointers. A practical application for a linked list would be a music playlist.

## <center> References </center>

Cormen, T. H., Leiserson, C. E., Rivest, R. L. & Stein, C. (2022). Introduction to Algorithms, <em>4th edition</em>. Cambridge. The MIT Press.

Eberl, M. (2017). The Median-of-Medians Selection Algorithm. Archive of Formal Proofs.

Reddy, P. (2021 June 29). Quick Select Algorithm. Medium. https://medium.com/nerd-for-tech/quick-select-algorithm-17ac146b6218
