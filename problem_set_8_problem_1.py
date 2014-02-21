'''
Problem 1:

He catches the flu in September, October and November.

1/10 * 1/10 * 1/10
1/1000


He catches the flu in September and then again in November, but not in October.

1/10 * 9/10 * 1/0
9/1000


He catches the flu exactly once in the three months from September through November.

(1/10 * 9/10 * 9/10) + (9/10 * 1/10 * 9/10) + (9/10 * 9/10 * 1/10)
(81/1000) + (81/1000) + (81/1000)
3 * (81/1000)
243/1000


He catches the flu in two or more of the three months from September through November.

(1/10 * 1/10 * 9/10) + (1/10 * 9/10 * 1/10) + (9/10 * 1/10 * 1/10) + (1/10 * 1/10 * 1/10)
(9/1000) + (9/1000) + (9/1000) + (1/1000)
(28/1000)
(28/1000)/4
7/250
'''
