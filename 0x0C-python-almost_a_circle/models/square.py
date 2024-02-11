from models.rectangle import Rectangle


class Square(Rectangle):
    """Type class square that inherits from Rectangle"""

    def __init__(self, size, x=0, y=0, id=None):
        """__init__ function"""

        super().__init__(size, size, x, y, id)


    @property
    def size(self):
        """size function public"""

        return self.width

    @size.setter
    def size(self, value):
        """size function for setter"""

        self.width = value
        self.height = value

    def __str__(self) -> str:
        """string representation"""
        id = self.id
        size = self.__size
        x = self.x
        y = self.y
        return "[Square] ({}) {}/{} - {}".format(id, x, y, size)

    def update(self, *args, **kwargs):
        """update arguments"""
        attr = ['id', 'size', 'x', 'y']
        if args:
            for at, numb in zip(attr, args):
                setattr(self, at, numb)
        elif kwargs:
            for key, value in kwargs.items():
                if key in attr:
                    setattr(self, key, value)

    def to_dictionary(self):
        """to_dictionary function"""

        return {
            "id": self.id, "size": self.width, "x": self.x, "y": self.y
        }
