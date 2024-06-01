class Rect:
    def __init__(self, width, height):
        self._width = width
        self._height = height

    @property
    def width(self):
        return self._width

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, value):
        self._height = value

    @property
    def area(self):
        return self._height * self._width

    @width.setter
    def width(self, value):
        self._width = value


if __name__ == '__main__':
    rect = Rect(height=80, width=60)
    rect.width = 10  # 800
    area = rect.area  # 注意这里使用了点号
    print(area)  # 800
