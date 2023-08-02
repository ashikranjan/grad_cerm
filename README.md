- Here I have used the python to solve the problem mentioned in the problem_statement.txt
- to run the code you can clone the repo and run the python python_soln.py
- You can try with different days by changing the value of days
- Please make sure that you have python installed and running python_soln.py 
- from the same directory where this file exist



Please find below my approach that i used to solve the problem


- In the problem statement we have two problem 1st is to find the number of ways to attend the class at N days and another to find the probability of not missing graduation ceremoney


Lets check how manyally we can find the number of ways
days=1, ways=1

days=2, ways=2
11
01

days=3, ways=4
111
011
101
001

days=4, ways=7
1111
0111
1011
1101
0011
0101
1001

days=5, ways=14
11111
01111
10111
11011
11101
00111
01011
01101
10011
10101
11001
00011
00101
10001


from the above example we can see that Nth day have relation with previoud days and that can be formulated as


f(n) = f(n - 1) +  f(n - 2) + f(n - 3) + f(n - 4)