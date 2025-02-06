def current(cpath: str, name: str = 'current'):
    def wrapper(path: str):
        return name if cpath == path else ''

    return wrapper


def star(rate: int):
    return '★ ' * rate + '☆ ' * (5 - rate)
