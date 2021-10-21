def singleton(cls):
    instances = dict()

    def wrap(*args, **kwargs):
        if cls not in instances:
            instances[cls] = cls()
        
        return instances[cls]

    return wrap



