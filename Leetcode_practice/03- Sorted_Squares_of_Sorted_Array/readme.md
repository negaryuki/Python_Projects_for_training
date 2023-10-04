# Sorted Squares of Sorted Array

This Python program takes an integer array sorted in non-decreasing order and returns an array of the squares of each number sorted in non-decreasing order.

## Table of Contents

- [Problem Statement](#problem-statement)
- [Examples](#examples)
- [How to Use](#how-to-use)
- [Solution Explanation](#solution-explanation)
- [Contributing](#contributing)
- [License](#license)

## Problem Statement

Given an integer array `nums` sorted in non-decreasing order, the task is to return an array of the squares of each number sorted in non-decreasing order.

### Example:

Input: `nums = [-4,-1,0,3,10]`

Output: `[0,1,9,16,100]`

Explanation: After squaring, the array becomes `[16,1,0,9,100]`. After sorting, it becomes `[0,1,9,16,100]`.

### Constraints:

- `1 <= nums.length <= 104`
- `-104 <= nums[i] <= 104`
- `nums` is sorted in non-decreasing order.

