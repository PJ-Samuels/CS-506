
from turtle import right


def read_triangle(filepath):
    """
    input is a file path
    output is a list of lists of
    """
    triangle = []
    with open (filepath, "r+" ) as triangle_file:
        lines = triangle_file.readlines()
        for line in lines:
            level = [int(x) for x in line.split(" ")]
            triangle.append(level)
        return triangle


def fold (prev_level, next_level):
    left_options =map(lambda x:x[0]+ x[1], zip(prev_level.append(0),next_level))
    right_options = map(lambda x:x[0]+x[1] ,zip([0]+prev_level, next_level))
    #print(list(left_options))
    #print(list(right_options))
    return next_level


def fold_triangle(triangle):
    """
    input list of lists of ints
    output list of ints
    """
    prev_level = triangle [0]
    for i in range(1,len(triangle)):
        next_level = triangle[i]
        prev_level = fold(prev_level, next_level)
    return prev_level
print(max(fold_triangle(read_triangle("./triangle_file.txt"))))