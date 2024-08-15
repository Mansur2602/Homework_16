import time

def stopwatch(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()  
        result = func(*args, **kwargs)  
        end_time = time.time()  
        elapsed_time = end_time - start_time  
        print(f"Время выполнения {elapsed_time:.4f} секунд")
        return result  
    return wrapper


@stopwatch
def example_function(n):
    total = 0
    for i in range(n):
        total += i
    return total

number = int(input("Введите число: "))

example_function(number)