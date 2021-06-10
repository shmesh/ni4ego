def find_left_corner(x):
    res = [1920 , 1080]
    find_x = (res[0] - x[0]) / 2
    find_y = (res[1] - x[1]) / 2
    return find_x , find_y + 450




def knopka(pos,hitbox):
    a = hitbox[0]
    b = hitbox[1]
    c =  hitbox[0] + hitbox[2]
    d =  hitbox[1] + hitbox[3]
    if pos[0] >= a and pos[0] <= c :
        if pos[1] >= b and pos[1] <= d:
            quit()


