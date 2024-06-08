import math as m

def black_hole():
    level = { 
        0:0,
        1:462,
        2:2688,
        3:5885,
        4:11777,
        5:29217,
        6:46255,
        7:63559,
        8:74340,
        9:85483,
        10:95000
    }
    projects = {
        "libft"             : 462,
        "ft_printf"         : 882,
        "get_next_line"     : 882,
        "Born2beroot"       : 577,
        "push_swap"         : 1855,
        "pipex"             : 1142,
        "minitalk"          : 1142,
        "so_long"           : 1000,
        "FdF"               : 1000,
        "fract-ol"          : 1000,
        "Philosophers"      : 3360,
        "minishell"         : 2814,
        "NetPractice"       : 3160,
        "cub3d"             : 5775,
        "miniRT"            : 5775,
        "cpp4"              : 9660,
        "ft_irc"            : 21630,
        "webserv"           : 21630,
        "cpp9"              : 10042,
        "Inception"         : 10042,
        "ft_transcendence"  : 24360
    }


    
    current_level =  float(input("your current level : "))
    current_project = str(input("choose project : "))
    current_xp = level[int(current_level)] * (current_level % 1) + level[int(current_level)]
    x = current_xp
    y = current_xp + projects[current_project]
    result = (((y / 49980)**(0.45)) - ((x / 49980)**(0.45)))*483
    float_part_result = round(result % 1, 2)
    print(int (result) + float_part_result)
black_hole()