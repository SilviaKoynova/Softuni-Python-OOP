# def print_row(size, star_count):
#     for row in range(size - star_count):
#         print(" ", end="")
#     for row in range(1, star_count):
#         print("*", end=" ")
#     print("*")
#
#
# size = int(input())
# for star_count in range(1, size):
#   print_row(size, star_count)
# for star_count in range(size, 0, -1):
#   print_row(size, star_count)
#
def repeat_str(text, count_to_repeat):
    return ''.join([text for i in range(count_to_repeat)])


class Rhombus:
    def __init__(self, n):
        self.n = n

    def draw(self):
        upper_down_rows = n - 1

        for j in range(upper_down_rows + 1):
            print(repeat_str(" ", upper_down_rows - j) + repeat_str("* ", j + 1))

        for k in range(upper_down_rows - 1, -1, -1):
            print(repeat_str(" ", upper_down_rows - k) + repeat_str("* ", k + 1))


n = int(input())
rhombus = Rhombus(n)
rhombus.draw()
