
ChatGPT prompt: "using python, using recursion, calculate 2^4."

Sure! Here’s a simple **recursive Python function** that calculates ( 2^4 ) (or any ( a^b )) using recursion:

```python
def power(base, exponent):
    # Base case: anything to the power of 0 is 1
    if exponent == 0:
        return 1
    # Recursive case
    return base * power(base, exponent - 1)

# Example: calculate 2^4
result = power(2, 4)
print(result)
```

### Explanation:

* When `exponent == 0`, the function returns `1`.
* Otherwise, it multiplies the base by the result of the same function with the exponent reduced by 1.
* So for `power(2, 4)`:

  ```
  2 * power(2, 3)
  2 * (2 * power(2, 2))
  2 * (2 * (2 * power(2, 1)))
  2 * (2 * (2 * (2 * power(2, 0))))
  ```

  → ( 2 * 2 * 2 * 2 = 16 )

✅ **Output:**

```
16
```
