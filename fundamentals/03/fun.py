class Car:
    madein = "China"

    def setCarInfo(self):
        self.name = "toyota"


print(Car.madein)
obj = Car
print(obj.madein)

obj.setCarInfo(Car)
print(obj.name)


class fun:
    def functions(num1, num2):
        return num1 + num2
