## Aliasing and Cloning in Python

When working with objects in Python, it's crucial to understand the difference between **aliasing** and **cloning** (or copying), especially with mutable objects like lists or dictionaries.

### 🔗 Aliasing (References)

**Aliasing** occurs when **two or more variables refer to the exact same object** in memory. When you assign one variable to another, Python does not create a new object; it simply makes the second variable an *alias* (another name) for the original object.

  * **How it works:** `b = a`
  * **Key Characteristic:** If you modify the object using one variable, the change is visible through all other variables (aliases) because they all point to the same memory location. This is often the source of unexpected side effects.

 *Example:* If `a` is a list and you do `b = a`, then `b.append(10)` will also change the list `a`.

 **Code:**

 ```python
 list_a = [1, 2]
 list_b = list_a # Aliasing
 list_b.append(3)
 # list_a is now [1, 2, 3]
 ```


### Cloning (Copying)

**Cloning** is the process of creating a **new, separate object** that has the same value as the original object. This ensures that changes made to the copy do not affect the original.

Cloning in Python typically comes in two forms: **Shallow Copy** and **Deep Copy**.

### Shallow Copy

A **shallow copy** creates a new object, but it **does not recursively copy nested objects** (like lists inside a list). Instead, it populates the new object with **references** to the nested objects found in the original.

  * **How to create:** `new_list = old_list[:]`, `new_list = list(old_list)`, or using `copy.copy()`.
  * **Result:**
      * The top-level objects are separate (modifying an element at the top level won't affect the original).
      * **Nested mutable objects are still aliased** (modifying a nested object *will* affect the original).

### 2 Deep Copy

A **deep copy** creates a new object and then **recursively copies all objects** it finds in the original. This means it creates entirely independent copies of all nested mutable objects as well.

  * **How to create:** Use the `copy.deepcopy()` function from the `copy` module.
  * **Result:** The copy is completely independent of the original. Changes to the deep copy, even in nested structures, will not affect the original object.

| Feature | Aliasing | Shallow Copy | Deep Copy                      |
|---------|----------|--------------|--------------------------------|
| **Independence**   | No | Partially (Top level only) | Yes (Fully) |
| **Nested Objects** | Shared/Aliased | Shared/Aliased | Independent |



## When to use Lists vs tuples
Tu



