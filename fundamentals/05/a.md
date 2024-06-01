在Python中，使用@property装饰器来定义属性的getter和setter方法是一种常见的做法，尤其是在你希望在获取或设置属性值时添加额外逻辑或验证时。下面是对你代码的详细解释：
首先，你定义了一个名为People的类：

```
class People:
```


接着，你在类中定义了构造函数__init__，它会在创建People类的新实例时被调用。在这个函数中，self是指向实例本身的引用，而name和age是传递给构造函数的参数：

```
def __init__(self, name, age):
```

在构造函数内部，你将传入的name和age值分别赋给了实例属性_name和_age。这里_name和_age使用了下划线前缀，这通常表示这些属性是内部使用，不应该直接从类外部访问：

```
        self._name = name
        self._age = age
```

然后，你使用@property装饰器来定义属性访问器，这样name和age就会看起来像是实例的属性而不是方法。@name.setter和@age.setter分别定义了对应的setter方法，用于设置name和age的值：

```
    @property
    def name(self):
        return self._name
    @name.setter
    def name(self, value):
        self._name = value
    @property
    def age(self):
        return self._age
    @age.setter
    def age(self, value):
        self._age = value
```

name和age属性的getter方法分别定义了如何获取属性值，而setter方法定义了如何设置属性值。这样的设计允许你在不直接访问实例属性的情况下，对属性的读写进行控制。例如，你可以在setter方法中添加验证逻辑，确保设置的值符合要求。
综上所述，你的代码遵循了Python的命名和编程规范，提供了一种有效的方式来封装实例属性。