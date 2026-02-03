# Inventory-Management-System-Update

## Background
This project simulates a feature in a retail inventory management system.
Each product is represented by an integer stock count. A value of `0`
indicates that the product is out of stock.

The system must duplicate each occurrence of `0` in the inventory array
(to represent a restock order) while shifting remaining elements to the
right. The operation must be performed **in place**, without increasing
the size of the array.

---

## Problem Statement
Given an integer array `inventory`, duplicate each occurrence of zero,
shifting the remaining elements to the right.

- Modifications must be done **in place**
- Elements beyond the original array length must be discarded
- No additional arrays may be used

---

## Example

### Input
```text
[4, 0, 1, 3, 0, 2, 5, 0]
```
Output
```text
[4, 0, 0, 1, 3, 0, 0, 2]
```

---

## Clarifying Questions
1. Should the array length remain the same after duplication?
Yes, elements that overflow past the original length are discarded
2. Can we use extra memory?
No, must be done in place
3. Can the array contain negative numbers?
Doesn't matter; only 0 has special meaning

---

## Youtube

5. Do we need to return anything?
No, modify the array directly 
