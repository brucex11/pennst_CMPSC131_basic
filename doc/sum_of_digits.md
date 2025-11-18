
ChatGPT prompt: "using python, using recursion, calculate the sum of the digits of a positive integer, for example, 12345."

Sure! Here’s a **Python recursive function** that calculates the **sum of the digits** of a positive integer (like `12345`):

```python
def sum_of_digits(n):
    # Base case: when n is 0, sum of digits is 0
    if n == 0:
        return 0
    # Recursive case: add the last digit to the sum of the rest
    return (n % 10) + sum_of_digits(n // 10)

# Example: calculate sum of digits of 12345
result = sum_of_digits(12345)
print(result)
```

### 🧠 Explanation

* `n % 10` gives the **last digit** of the number.
* `n // 10` removes the **last digit** (integer division).
* The recursion continues until `n` becomes 0.

So for `12345`:

```
sum_of_digits(12345)
= 5 + sum_of_digits(1234)
= 5 + 4 + sum_of_digits(123)
= 5 + 4 + 3 + sum_of_digits(12)
= 5 + 4 + 3 + 2 + sum_of_digits(1)
= 5 + 4 + 3 + 2 + 1 + sum_of_digits(0)
= 15
```

✅ **Output:**

```
15
```


