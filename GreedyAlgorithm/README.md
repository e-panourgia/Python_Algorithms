This project created to solve the set covering problem using a greedy algorithm and implementing it with python.
Specifically, we will see how to represent a problem in python using class and data structures li9ke lists and sets.
In addition, I will use a greedy algorithm to solve the problem. 

Set Covering problem belongs to __Selection Problems__: Given a Set 
data, you are invited to select some of the 
elements in order to optimize someone 
objective. Due to the existence of restrictions 
it is not possible to select all the elements of the 
Set.

Description of set covering problem : 
- data
  U(Universe) consists of m elements, U = { 1, 2, ..., m}
  S(Subset) Scomp = {S1, S2, ..., Sn} with Si belongs to U 
  The goal is to find the minimum number of subsets that will covel all elements of Universe.
  
The specific python projct will solve the set covering problem with data : 
U = { 1,2, ..., 10 } and 

Scomp = {S1, S2, ..., S10 }

S1 = {1, 2}

S2 = {2, 1, 3}

S3 = {3, 4, 5, 6}

S4 = {4, 2, 3, 9}

S5 = {5, 4, 6, 8}

S6 = {6, 7}

S7 = {7, 8}

S8 = {8, 5 , 7 ,10}

S9 = {9, 4, 8}

S10 = {10, 8}

------------------------------
Structure of greedy algorithm : 
S <- 0 # S : solution 

    While(S is not complete)
        df = findNextFeature()
        S = S union df
