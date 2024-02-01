
# singleton函数是一个装饰器，用于实现单例模式。单例模式是一种设计模式，它保证一个类只有一个实例，并提供一个全局访问点

class DatabaseConnection:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        # 连接到数据库...
```

然后，无论你何时创建 `DatabaseConnection` 的实例，都会得到同一个实例：

```python
db1 = DatabaseConnection('localhost', 27017)
db2 = DatabaseConnection('localhost', 27017)
assert db1 is db2  # 这个断言会成功，因为 db1 和 db2 是同一个实例
```

def singleton(cls):   

    instances = {}

    def _wrapper(*args, **kwargs):

        if cls not in instances:

            instances[cls] = cls(*args, **kwargs)

        return instances[cls] 

    return _wrapper 
