# Binary Search Algorithm.

#### A Binary search algorithm finds an item in a _sorted_ list in O(logn time).

A brute force search would walk through a whole list, taking O(n) time in worst case scenario. Let's say we have a sorted listed of numbers, to find a number with a binary search:

- **Start with a middle number: is it bigger or smaller than our taraget number?** Since the list is sorted, this tells us if the target  would be in a _left_ half or _right_ half of our list.
- **We have effectively divided our problem in half**. We can _rule out_ the half of list which doesn't bear our desired/target number.
- **Repeating the same approach (of starting in the middle)** on the new half-size problem. We repeat this again and again until we get our target number or we _rule out_ whole set.
