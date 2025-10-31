## while loop

-While loops are used when you don't have a fixed number of iterations and when yo are iterating based on particular conditions

- ` While` loops can repeat code infinitely if the condition for breaking out of the loop is never met. There should always be something that leads to the condition becoming false

- `While` loops can be exited by `break` statement and nested `while` loops can be exited the same way, except the break statement only exits the `while` loop that surrounds it.

## for loop

For loops are used when you have a fixed number of items that you want to be iterating over

## Boolean flags

Boolean flags a re variables whose values can be used to keep track of when a change has happened within your code so you can write more code that depends on it's value

### uses

1. State Tracking to record whether a specific event has occurred or if a state has been reached. Tracking if a user is is_authenticated or if a file has_been_saved.

2. Flow Control to signal when a process, such as a loop, should start, continue, or stop. Setting is_running = False to terminate a while loop when a condition is met.

3. Feature Switching to conditionally enable or disable certain blocks of code or program features. Using debug_mode = True to turn on extra logging or diagnostics.

4. Conditional Execution to defer a decision about code execution until later, based on whether the flag was set during an earlier part of the program.
