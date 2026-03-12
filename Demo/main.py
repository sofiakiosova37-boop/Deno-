from fib_lib import fibonacci

def run():
    print("--- Тестирование локальной библиотеки ---")
    fib = fibonacci()
    
    for i in range(10):
        print(f"Число {i+1}: {next(fib)}")

if __name__ == "__main__":
    run()