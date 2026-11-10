"""
=============================================================================
        DSA MASTERY ROADMAP - From Zero to Hero (Python)
=============================================================================

FAMOUS DSA SHEETS / RESOURCES TO FOLLOW:
-----------------------------------------
1. Striver's A2Z DSA Sheet (takeuforward.org/strivers-a2z-dsa-course)
   - Best for ABSOLUTE BEGINNERS → Advanced
   - 450+ problems, topic-wise, with video explanations
   - Starts from basics (patterns, math) and goes to graphs, DP

2. NeetCode 150 (neetcode.io/roadmap)
   - 150 curated LeetCode problems organized by pattern
   - Great video explanations on YouTube
   - Best after you know basics of each data structure

3. Blind 75 (subset of NeetCode 150)
   - 75 most important interview problems
   - Good for revision / quick prep after learning

4. LeetCode Study Plans (leetcode.com/studyplan)
   - Built-in guided paths on LeetCode itself

5. Love Babbar DSA Sheet (450 problems)
   - Another popular Indian DSA sheet

RECOMMENDATION: Start with Striver's A2Z (it teaches from zero).
             Use NeetCode 150 later to master patterns.

=============================================================================
        YOUR TOPIC-WISE LEARNING ORDER (16 PHASES)
=============================================================================

PHASE 1: Python Basics & Complexity Analysis (Week 1)
-------------------------------------------------------
Topics:
  - Time Complexity: O(1), O(n), O(n²), O(log n), O(n log n)
  - Space Complexity
  - Python basics: lists, dicts, sets, strings, loops, functions
Practice:
  - No LeetCode yet. Just understand how to measure efficiency.

PHASE 2: Basic Math & Number Problems (Week 2)
------------------------------------------------
Topics:
  - Count digits, reverse number, palindrome number
  - GCD/HCF (Euclidean algorithm), LCM
  - Check prime, Armstrong number
  - Factorial, Fibonacci
LeetCode Problems:
  - #9   Palindrome Number (Easy)
  - #7   Reverse Integer (Medium)
  - #1281 Subtract Product and Sum of Digits (Easy)
  - #204  Count Primes (Medium)

PHASE 3: Arrays - Basics (Week 3-4)
-------------------------------------
Topics:
  - Traversal, insertion, deletion
  - Find max/min, reverse array
  - Left/right rotation
  - Linear search
  - Prefix sum
LeetCode Problems:
  - #1    Two Sum (Easy) ⭐
  - #26   Remove Duplicates from Sorted Array (Easy)
  - #283  Move Zeroes (Easy)
  - #268  Missing Number (Easy)
  - #136  Single Number (Easy)
  - #121  Best Time to Buy and Sell Stock (Easy) ⭐
  - #53   Maximum Subarray - Kadane's Algo (Medium) ⭐

PHASE 4: Sorting Algorithms (Week 5)
--------------------------------------
Topics:
  - Bubble Sort, Selection Sort, Insertion Sort
  - Merge Sort (important!), Quick Sort (important!)
  - Counting Sort
  - When to use which sort
LeetCode Problems:
  - #912  Sort an Array (Medium)
  - #75   Sort Colors (Medium) - Dutch National Flag ⭐
  - #56   Merge Intervals (Medium)
  - #179  Largest Number (Medium)

PHASE 5: Binary Search (Week 6)
---------------------------------
Topics:
  - Basic binary search on sorted array
  - Binary search on answer (very important pattern!)
  - Lower bound, upper bound
  - Search in rotated sorted array
LeetCode Problems:
  - #704  Binary Search (Easy)
  - #35   Search Insert Position (Easy)
  - #34   First and Last Position (Medium) ⭐
  - #33   Search in Rotated Sorted Array (Medium) ⭐
  - #153  Find Minimum in Rotated Sorted Array (Medium)
  - #875  Koko Eating Bananas (Medium)

PHASE 6: Strings (Week 7)
---------------------------
Topics:
  - String manipulation, reversal
  - Palindrome check
  - Anagram check
  - String matching basics
LeetCode Problems:
  - #125  Valid Palindrome (Easy)
  - #242  Valid Anagram (Easy)
  - #3    Longest Substring Without Repeating Characters (Medium) ⭐
  - #49   Group Anagrams (Medium)
  - #20   Valid Parentheses (Easy) ⭐

PHASE 7: Hashing (HashMap / HashSet) (Week 8)
-----------------------------------------------
Topics:
  - Hash maps and hash sets in Python (dict, set)
  - Frequency counting
  - Two Sum pattern using hashmap
LeetCode Problems:
  - #1    Two Sum (Easy) - revisit with hashmap approach
  - #217  Contains Duplicate (Easy)
  - #349  Intersection of Two Arrays (Easy)
  - #560  Subarray Sum Equals K (Medium) ⭐
  - #347  Top K Frequent Elements (Medium)

PHASE 8: Two Pointers & Sliding Window (Week 9-10)
-----------------------------------------------------
Topics:
  - Two pointer technique (start-end, slow-fast)
  - Sliding window (fixed size and variable size)
LeetCode Problems:
  - #167  Two Sum II (Medium)
  - #15   3Sum (Medium) ⭐
  - #11   Container With Most Water (Medium) ⭐
  - #209  Minimum Size Subarray Sum (Medium)
  - #76   Minimum Window Substring (Hard) ⭐
  - #239  Sliding Window Maximum (Hard)

PHASE 9: Linked Lists (Week 11-12)
-------------------------------------
Topics:
  - Singly linked list: create, insert, delete, traverse
  - Doubly linked list
  - Fast & slow pointer technique (Floyd's cycle detection)
  - Reverse a linked list
LeetCode Problems:
  - #206  Reverse Linked List (Easy) ⭐
  - #21   Merge Two Sorted Lists (Easy) ⭐
  - #141  Linked List Cycle (Easy) ⭐
  - #19   Remove Nth Node From End (Medium)
  - #143  Reorder List (Medium)
  - #23   Merge K Sorted Lists (Hard) ⭐

PHASE 10: Stacks & Queues (Week 13)
--------------------------------------
Topics:
  - Stack (LIFO): push, pop, peek
  - Queue (FIFO): enqueue, dequeue
  - Monotonic stack
  - Implement stack using queue and vice versa
LeetCode Problems:
  - #20   Valid Parentheses (Easy) ⭐
  - #155  Min Stack (Medium)
  - #150  Evaluate Reverse Polish Notation (Medium)
  - #739  Daily Temperatures (Medium) ⭐
  - #84   Largest Rectangle in Histogram (Hard) ⭐

PHASE 11: Recursion & Backtracking (Week 14-15)
--------------------------------------------------
Topics:
  - Recursion basics: base case, recursive case
  - How call stack works
  - Subsets, permutations, combinations
  - N-Queens, Sudoku solver
LeetCode Problems:
  - #509  Fibonacci Number (Easy) - understand recursion
  - #78   Subsets (Medium) ⭐
  - #46   Permutations (Medium) ⭐
  - #39   Combination Sum (Medium) ⭐
  - #79   Word Search (Medium)
  - #51   N-Queens (Hard) ⭐

PHASE 12: Trees (Binary Tree & BST) (Week 16-18)
---------------------------------------------------
Topics:
  - Binary tree: create, traversals (inorder, preorder, postorder, level-order)
  - Height, diameter, balanced tree check
  - Binary Search Tree (BST): insert, delete, search
  - Lowest Common Ancestor (LCA)
LeetCode Problems:
  - #104  Maximum Depth of Binary Tree (Easy) ⭐
  - #226  Invert Binary Tree (Easy)
  - #100  Same Tree (Easy)
  - #102  Binary Tree Level Order Traversal (Medium) ⭐
  - #98   Validate BST (Medium) ⭐
  - #230  Kth Smallest Element in BST (Medium)
  - #236  Lowest Common Ancestor (Medium) ⭐
  - #124  Binary Tree Maximum Path Sum (Hard) ⭐

PHASE 13: Heaps / Priority Queues (Week 19)
----------------------------------------------
Topics:
  - Min heap, max heap
  - Python heapq module
  - Top K problems
  - Median finding
LeetCode Problems:
  - #703  Kth Largest Element in Stream (Easy)
  - #215  Kth Largest Element in Array (Medium) ⭐
  - #347  Top K Frequent Elements (Medium) ⭐
  - #295  Find Median from Data Stream (Hard) ⭐

PHASE 14: Graphs (Week 20-22)
-------------------------------
Topics:
  - Graph representation: adjacency list, adjacency matrix
  - BFS (Breadth First Search)
  - DFS (Depth First Search)
  - Cycle detection
  - Topological sort
  - Shortest path: Dijkstra's, Bellman-Ford
  - Union-Find (Disjoint Set)
LeetCode Problems:
  - #200  Number of Islands (Medium) ⭐
  - #133  Clone Graph (Medium)
  - #695  Max Area of Island (Medium)
  - #207  Course Schedule (Medium) ⭐
  - #210  Course Schedule II (Medium)
  - #743  Network Delay Time (Medium) - Dijkstra's
  - #323  Number of Connected Components (Medium)
  - #127  Word Ladder (Hard)

PHASE 15: Dynamic Programming (Week 23-26)
---------------------------------------------
Topics:
  - What is DP? Memoization vs Tabulation
  - 1D DP: climbing stairs, house robber, fibonacci
  - 2D DP: grid problems, LCS, edit distance
  - Knapsack problems (0/1, unbounded)
  - DP on strings, DP on subsequences
LeetCode Problems:
  - #70   Climbing Stairs (Easy) ⭐
  - #198  House Robber (Medium) ⭐
  - #322  Coin Change (Medium) ⭐
  - #300  Longest Increasing Subsequence (Medium) ⭐
  - #1143 Longest Common Subsequence (Medium) ⭐
  - #62   Unique Paths (Medium)
  - #416  Partition Equal Subset Sum (Medium)
  - #72   Edit Distance (Medium) ⭐
  - #10   Regular Expression Matching (Hard)

PHASE 16: Tries & Advanced Topics (Week 27-28)
-------------------------------------------------
Topics:
  - Trie (prefix tree)
  - Segment tree (basics)
  - Bit manipulation
LeetCode Problems:
  - #208  Implement Trie (Medium) ⭐
  - #211  Design Add and Search Words (Medium)
  - #191  Number of 1 Bits (Easy)
  - #338  Counting Bits (Easy)
  - #371  Sum of Two Integers (Medium)

=============================================================================
        HOW WE WILL WORK TOGETHER
=============================================================================

For EVERY problem, we will follow this approach:

Step 1: UNDERSTAND - Read the problem, identify inputs/outputs, draw examples
Step 2: BRUTE FORCE - Think of the simplest (even slow) solution first
Step 3: OPTIMIZE - Can we use a better data structure or algorithm?
Step 4: CODE - Write clean Python code
Step 5: DRY RUN - Trace through the code with an example
Step 6: ANALYZE - Time & Space complexity

Golden Rules:
  - No shame in not knowing. Everyone starts at zero.
  - Solve EASY problems first. Don't jump to Medium/Hard.
  - If stuck for 20 min, ask me. I'll give hints, not answers.
  - Understand the PATTERN, not just the solution.
  - Revise problems after 3 days, then after 7 days.

=============================================================================
        LET'S START! Tell me when you're ready for Phase 1.
=============================================================================
"""
