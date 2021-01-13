# Problem Solved in DSA Course 📖 <!-- omit in toc -->

The repository contains various approaches and their solutions of questions solved as part of Data Structures and Algorithms Course (CS 301).

## Contents 💻 <!-- omit in toc -->

- [Greedy Algorithms](#greedy-algorithms)
  - [1 Islands War 🏝️](#1-islands-war-️)
  - [2 Boxes and Balls ⚽](#2-boxes-and-balls-)
  - [3 Appleman and Toastman 🍎](#3-appleman-and-toastman-)
  - [4 Stable Marriage 👫](#4-stable-marriage-)

## Greedy Algorithms

### 1 Islands War 🏝️
**Question:** [Link](hhttps://atcoder.jp/contests/abc103/tasks/abc103_d) | **Solution** : [Python Link](./Week1/1_islandWar.py)

**Approach:**
* Related to Interval Scheduling Topic.
* Let's say the the bridge is between the source and the destination. (source, destination)
* Sort the collection of tuples according the index of destination islands.
* Now if we traverse, the collection of requests, we could skip all the requests with source before the current minimum destination. Since, breaking a bridge would eventually disrupt the roots to those destinations.
* when the source becomes higher than the destination, we will have to break another bridge, and change the current minimum destination to the latest one.
* **Time Complexity**: O(N)
### 2 Boxes and Balls ⚽
**Question:** [Link](https://codeforces.com/contest/884/problem/D) | **Solution** : [Python Link](./Week1/2_boxesAndApples.py)

**Approach:**
* 

### 3 Appleman and Toastman 🍎

### 4 Stable Marriage 👫

**Question:** [Link](https://www.codechef.com/problems/STABLEMP) | **Solution** : [C++ Link](./Week1/4_stableMarriage.py) , [Python Link](./Week1/4_stableMarriage.py)    

**Approach:**           
* Initialize All the engangement of men to be -1.
* While there are no single men:
  * Now each of the men would propose to their top preferred woman.    
      * If the womam is not engaged, she would accept the proposal.
      * Else, check the rank of the proposed person, if it is lower(highly preferred) than her husband, she would break the engagement and create a new one with the latest proposer. Her husband would become single now.   
* Time Complexity: O(N^2)