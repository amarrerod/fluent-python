import time

DEFAULT_FMT = "[{elapsed_time:0.8f}s {name}({args}) --> {result}]"


class clock:
    def __init__(self, fmt=DEFAULT_FMT):
        self.fmt = fmt

    def __call__(self, func):
        def clocked(*_args, **_kwargs):
            start = time.perf_counter()
            _result = func(*_args, **_kwargs)
            elapsed_time = time.perf_counter() - start
            name = func.__name__
            arg_lst = [repr(arg) for arg in _args]
            arg_lst.extend(f"{k}={v}" for k, v in _kwargs.items())
            args = ", ".join(arg_lst)
            result = repr(_result)
            print(self.fmt.format(**locals()))
            return _result

        return clocked
