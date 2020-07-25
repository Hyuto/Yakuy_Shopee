# Shopee Programming Contest 2
Complete 1.5 dari 5 soal:
## 1. Highest Mountains
### Desc
Victor is assigned a task for planning quarterly team outings in Shopee. He is trying to organize an outdoor activity to climb the highest mountain among a mountain range. However, it is difficult to tell which mountain is the highest in the mountain range from a distance. Help Victor to identify the highest mountain given the height of the mountains.

In order to climb a mountain, the mountain needs to either increase or decrease consistently by 1 and has at least one side to be able to be seen connected to the ground. Given that 1 is ground level, “2324” is not a valid mountain to be climbed, while “1234” and “4321” are valid mountains with height of 4.

Find the height of the highest climbable mountain.
<br>
### Input
The first line will specify the N number of mountain ranges
Subsequent N sets will have length L and a series of numbers separated by space representing the height (H)
```
Height: 1 <= H <= 1000
Length: 1 <= L <= 1000
```

```
SAMPLE INPUT
6

10
1 2 3 2 3 4 2 3 2 5

10
3 2 3 2 3 4 3 2 1 4

5
1 1 1 1 1

10
10 9 8 7 6 5 4 3 2 1

1
5

1
1
```
### Output
Integer specifying the height (H) of the highest mountain and index (I) of the peak. If there are multiple mountains with the same height, return the leftmost mountain.
If the height or index is not available, return -1. Return the result for each case with format “Case #{N}: H I”

```
SAMPLE OUTPUT
Case #1: 3 2
Case #2: 4 5
Case #3: 1 0
Case #4: 10 0
Case #5: -1 -1
Case #6: 1 0
```
### Note : Lancar tanpa error
## 2. Conectivity
### Desc
In Shopee Data Center, there are many switches and some of the switches are interconnected to form a network. Sometimes, we add a new connection to the network and if we find that there is some issue, we may remove the last added connections. You will need to solve a similar problem.

You are given an empty network with N switches (numbered 1 to N) and no connections between switches. You will also face Q scenarios in chronological order. Each scenario can be any of the following:

PUSH u v : You have to add a new connection between switches u and v. (u ≠ v, 1 <= u, v <= N). Note that there can be multiple connections between the same pair of switches.

POP : From all the connections currently present in the network, remove the one that was added most recently. There will be at least one connection in the network when this scenario is given.

Also, after performing the operation in each scenario, print the number of connected components formed by the switches in this network.
### Input
The first line of test case begins with integer 
```
Q (1 <= Q <= 5 * 105)
N (1 <= N <= 5 * 105) 
```
indicating the number of scenarions and number of switches in the network. Next, Q lines will each contain a scenario as described above.
```
SAMPLE INPUT
12 5
PUSH 1 2
PUSH 2 3
PUSH 1 4
POP
PUSH 1 3
PUSH 4 5
PUSH 1 4
POP
POP
POP
POP
POP
```
### Output
For each query, you will need to print the answer in a separate line.
```
SAMPLE OUTPUT
4
3
2
3
3
2
1
2
3
3
4
5
```
### Note : Kayaknya kena limit waktu deh wkwk