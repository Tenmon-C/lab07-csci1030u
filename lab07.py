# Fill in the two functions and the two classes below (look for the TODO comments).
#
# Parts 1 and 2 must use RECURSION - a function that calls itself on a smaller version
# of the problem. Do NOT use a loop for those two.
#
# Do not rename anything, because the automated tests use these names.


def count_occurrences(target, values):
    # TODO (Part 1, recursion): return how many times `target` appears in the list
    #   `values`.
    #   Base case: an empty list contains it 0 times.
    # uses "not" becuase it askes if the list has no elements and due to it having no elements not works
    # you can also use if values == [] becuase it also asks if there is no elements in the list
    if not values:
        return 0
    #   Recursive case: 1 (if the first item equals `target`, otherwise 0) plus the
    #   count in the rest of the list, values[1:].
    # if the target is in the list add 1 to the count then remove that element from the list and redo until the end of the list
    if values[0] == target:
        return 1 + count_occurrences(target, values[1:])
    # else do not add to the count but still remove the element from the list
    else:
        return count_occurrences (target, values[1:])


def is_sorted(values):
    # TODO (Part 2, recursion): return True if `values` is in non-decreasing order
    #   (every item is <= the one after it), otherwise False.
    #   Base case: a list of 0 or 1 items is already sorted.
    # if the len/length of values is <= 1 it is deamed sorted lust making it true at all times
    # USE len(values) if not it give a traceback becuase it can't combine a list and a int together 
    if len(values) <= 1:
        return True
    #   Recursive case: the first two items are in order AND the rest is sorted.
    # returns true if values[0] <= values[1] if it is complete the "and" statement which calls on the recursive until it is a number that is not in order or it reaches the end 
    # if it reaches the end its true if not it can't use the "and" becuase values[0] has to be <= values[1]
    return values[0] <= values[1] and is_sorted(values[1:])
    


class Rectangle:
    def __init__(self, width, height):
        # TODO (Part 3, OOP): store width and height on self
        # this stores the width and height in the self function for later use 
        self.width = width
        self.height = height

    def area(self):
        # TODO: return width * height
        # this just returns width * height using self
        return self.width * self.height

    def perimeter(self):
        # TODO: return 2 * (width + height)
        # same as last just instead of * it adds the two together then multiplies it by 2
        return 2 * (self.width + self.height)

    def __str__(self):
        # TODO: return "<width>x<height>", e.g. Rectangle(3, 4) -> "3x4"
        #this uses a return f that has the numbers for the width and the height but it just adds the letter x inbetween the two
        # DO NOT use print(f"") it also puts it in a traceback ONLY use return f""
        return f"{self.width}x{self.height}"


class Square(Rectangle):   # Part 4 - stretch (optional)
    def __init__(self, side):
        # TODO: a Square is a Rectangle whose width and height are the same. Call the
        #   Rectangle constructor with `side` for both (use super().__init__(...)).
        #   area, perimeter, and __str__ are then inherited automatically.
        # I just used the example in the description to add the supper().__init__ and due to the wudth a height being the same 
        # therefor the sides are the two that are used
        return super().__init__(side,side)


def main():
    # Optional scratch space - try your work here, then run: python lab07.py
    print(count_occurrences(2, [1, 2, 2, 3, 2]))   # 3
    print(is_sorted([1, 2, 3]))                    # True
    print(Rectangle(3, 4).area())                  # 12
    print(Square(5))                               # 5x5


if __name__ == "__main__":
    main()
