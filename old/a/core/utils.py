def current(cpath: str, name: str = 'current'):
    def wrapper(path: str):
        return name if cpath == path else ''

    return wrapper