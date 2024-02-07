class Filter:
    # 使用__slots__特殊属性来限制一个类的实例只能有特定的属性。__slots__是一个类变量，它是一个字符串列表，列表中的每个字符串都是一个允许的属性名。
    __slots__ = ["value", "label"]

    def __init__(self, value, label):
        self.value = value
        self.label = label

    def to_dict(self):
        return {"value": self.value, "label": self.label}
