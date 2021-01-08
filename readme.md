# Problem Solved in DSA Course 📖 <!-- omit in toc -->

The repository contains various approaches and their solutions of questions solved as part of Data Structures and Algorithms Course (CS 301).

## Contents 💻 <!-- omit in toc -->

- [1 Islands War 🏝️](#1-islands-war-️)
- [2 Boxes and Balls ⚽](#2-boxes-and-balls-)
- [3 Appleman and Toastman 🍎](#3-appleman-and-toastman-)
- [4 Stable Marriage 👫](#4-stable-marriage-)

### 1 Islands War 🏝️

### 2 Boxes and Balls ⚽

### 3 Appleman and Toastman 🍎

### 4 Stable Marriage 👫

**Question:** [Link](https://www.codechef.com/problems/STABLEMP) | **Solution** : [C++ Link](./Week1/4_stableMarriage.py) , [Python Link](./Week1/4_stableMarriage.py)    

**Approach:**           
* Initialize All the engangement of men to be -1.
* While there are no single men:
  * Now each of the men would propose to their top preferred woman.    
      * If the womam is not engaged, she would accept the proposal.
      * Else, check the rank of the proposed person, if it is lower(highly preferred) than her husband, she would break the engagement and create a new one with the latest proposer. Her husband would become single now.   
