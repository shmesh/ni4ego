def find_left_corner(x):
    res = [1920 , 1080]
    find_x = (res[0] - x[0]) / 2
    find_y = (res[1] - x[1]) / 2
    return find_x , find_y + 450

