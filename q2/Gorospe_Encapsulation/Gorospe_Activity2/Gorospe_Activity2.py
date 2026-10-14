class Rectangle:
    def __init__(self, width, height):
        self.__width = width
        self.__height = height

    @property
    def width(self):
        return f"{self.__width:.1f}cm"

    @property
    def height(self):
        return f"{self.__height:.1f}cm"

    @width.setter
    def width(self, new_width):
        if new_width > 0:
            self.__width = new_width
        else:
            print("WIDTH MUST BE GREATER THAN 0")

    @height.setter
    def height(self, new_height):
        if new_height > 0:
            self.__height = new_height
        else:
            print("HEIGHT MUST BE GREATER THAN 0")

rectangle = Rectangle(3, 4)

rectangle.width = 5
rectangle.height = 6

print(rectangle.width)
print(rectangle.height)

# How does using @property make your code easier to read compared to using traditional get_ and set_ methods?

# Using @property makes code easier to read because you can access and change values like normal variables instead of using get_ and set_ methods. It also lets you control the values and check if they are valid. It also makes the code look cleaner.
