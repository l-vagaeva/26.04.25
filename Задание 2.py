class Rectangle:
    def init(self, height, length):
        self.__height = height
        self.__length = length
        self.__square = None
        self.__perimeter = None

    def get_high(self):
        return self.__height

    def set_high(self, value):
        if value <= 0:
            raise ValueError("Высота должна быть положительной")
        self.__height = value
        self.__update_square_and_perimeter()

    def get_length(self):
        return self.__length

    def set_length(self, value):
        if value <= 0:
            raise ValueError("Ширина должна быть положительной")
        self.__length = value
        self.__update_square_and_perimeter()

    def get_square(self):
        if self.__square is None:
            self.__update_square_and_perimeter()
        return self.__square

    def get_perimeter(self):
        if self.__perimeter is None:
            self.__update_square_and_perimeter()
        return self.__perimeter

    def __update_square_and_perimeter(self):
        self.square = self.height * self.__length
        self.perimeter = 2 * (self.height + self.__length)

if __name__ == "__main__":
    rect = Rectangle(height=5, length=7)

    print(f"Высота: {rect.get_high}")
    print(f"Ширина: {rect.get_length}")
    print(f"Площадь: {rect.get_square}")
    print(f"Периметр: {rect.get_perimeter}")

    rect.set_high = 8
    rect.set_length = 12

    print("После изменения размеров:")
    print(f"Высота: {rect.get_high}")
    print(f"Ширина: {rect.get_length}")
    print(f"Площадь: {rect.get_square}")
    print(f"Периметр: {rect.get_perimeter}")
