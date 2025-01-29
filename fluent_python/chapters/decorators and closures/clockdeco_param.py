import time
import functools

DEFAULT_FMT = '[{elapsed:0.8f}s] {name}({args}) -> {result}'

def clock(fmt=DEFAULT_FMT): # Фабрика параметризованных декораторов
    def decorate(func): # Декоратор
        def clocked(*_args): # Обработчик декорированной функции
            t0 = time.perf_counter()
            _result = func(*_args)
            elapsed = time.perf_counter() - t0
            name = func.__name__
            args = ", ".join(repr(_arg) for _arg in _args)
            result = repr(_result)
            print(fmt.format(**locals()))
        return clocked
    return decorate

if __name__ == '__main__':

    @clock()
    def snooze(seconds):
        time.sleep(seconds)
    
    for i in range(3):
        snooze(.123)