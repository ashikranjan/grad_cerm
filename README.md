- Here I have used Python to solve the problem mentioned in the problem_statement.txt
- to run the code you can clone the repo and run the python python_soln.py
- You can try with different days by changing the value of days
- Please make sure that you have Python installed and running python_soln.py 
- from the same directory where this file exists



Please find below the approach that I used to solve the problem


- In the problem statement we have two problems 1st is to find the number of ways to attend the class at N days and another to find the probability of missing the graduation ceremony


- Let's check how manually we can find the number of ways to attend classes
days=1, ways=2    0, 1

days=2, ways=4    11, 01, 00, 10 

days=3, ways=8    111, 011, 101, 110, 000, 001, 010, 100

days=4, ways=15   1111, 0111, 1011, 1101, 1110, 0011, 0101, 0110, 1001, 1010, 1100, 0001, 0010, 1000, 0000


- Let's check how manually we can find the number of ways to miss the ceremony

days=1, ways=1  0

days=2, ways=2  00, 10

days=3, ways=4  000, 110, 010, 100

days=4, ways=7  1110, 0110, 1010, 1100, 0010, 0100, 1000



from the above example, we can see that the Nth day has a relation with previous days and that can be formulated as
f(n) = f(n - 1) +  f(n - 2) + f(n - 3) + f(n - 4)