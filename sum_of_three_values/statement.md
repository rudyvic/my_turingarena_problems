# Sum of three values
This problem is taken from [CSES](https://cses.fi/problemset/task/1641)

You are given an array of n integers, and your task is to find three values (at distinct positions) whose sum is x.

<description for="find_sum">
Find the sum equal to <param>sum</param> in the array <param>a</param> that has <param>n</param> elements.
</description>
<description for="get_result">
Return the <param>i</param>-th element of the results.
</description>

## Input
The first input line has two integers *n* and *x*: the array size and the target sum.<br>
The second line has *n* integers *a1,a2,…,an*: the array values.

## Output
Print **three integers**: the positions of the values.<br>
If there are several solutions, you may print any of them.<br>
If there are no solutions, print **IMPOSSIBLE**.


## Subtasks
**Subtask 1**
```
n=10
0≤x≤10^2
```
**Subtask 2**
```
n=1000
0≤x≤10^5
```
**Subtask 3**
```
n=100000
0≤x≤10^3
```

## Example
### Input:
```
4 8
2 7 5 1
```
### Output:
```
1 3 4
```
