## What are Lambda functions?

 Lambda functions are anonymous functions that allow you to create a function that takes n a value and returns ta value based on conditions in one line ``lambda x: work`` where the enter code returns the value after `work` has been computed 

 For example:
`lambda x: x % 2 == 0` would return true if x is given an even number as that is what the lambda function checks.
`(lambda x: x % 2 == 0)(8) is a way the lambda function can be called with a value passed` 


## Tuples
- Tuples are a type lists that are immutable. It used the ``()`` notation instead of `[]`.
- Tuples cannot be modified when they are created compared to lists that can be modified.
- Elements in tuples can be referred to just like the way lists ca, with tuples also being able to be nested just they way lists can.
- We can iterate over tuples like we would in a list and grab each element using a for loop.
- Tuples allow us to swap values so ```(x,y) = (y,x)``` will swap the values of x and y
- Tuples can be used to return more than one return value like`` return (a,b)``
