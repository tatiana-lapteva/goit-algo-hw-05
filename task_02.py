"""
Реалізувати двійковий пошук для відсортованого масиву з дробовими числами. 
Написана функція для двійкового пошуку повинна повертати кортеж, де першим 
елементом є кількість ітерацій, потрібних для знаходження елемента. 
Другим елементом має бути "верхня межа" — це найменший елемент, який є більшим 
або рівним заданому значенню.
"""

def binary_search(arr, x):
    low = 0
    high = len(arr) - 1
    mid = 0
    iter = 0
    while low <= high:
        iter += 1
        mid = (high + low) // 2
        if arr[mid] < x:
            low = mid + 1
        elif arr[mid] > x:
            high = mid - 1
        else:
            return iter, arr[high]
    return iter, -1


if __name__ == "__main__":

    arr = [2, 3, 4, 5.34, 6.42, 8.15, 10.30, 12.20, 14, 40]
    x = 8.15
    iter, result = binary_search(arr, x)
    if result != -1:
        print(f"The number of iterations required to find the element is {iter} iterations. The upper bound is {result}")
    else:
        print("Element is not present in array")
