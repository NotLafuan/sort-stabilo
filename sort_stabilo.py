from typing import NamedTuple
from utils.color_math import shortest_index
from statistics import mean


class Pen(NamedTuple):
    number: int
    name: str
    color: tuple[int, int, int]


pen_list = [
    Pen(37, 'mud green', (130, 126, 55)),
    Pen(66, 'khaki', (188, 174, 99)),
    Pen(13, 'ice green', (55, 182, 170)),
    Pen(43, 'light green', (117, 184, 66)),
    Pen(14, 'lime green', (201, 215, 110)),
    Pen(33, 'apple green', (162, 191, 22)),
    Pen(33, 'neon green', (133, 189, 63)),
    Pen(34, 'pistachio', (156, 181, 90)),
    Pen(35, 'moss green', (127, 140, 71)),
    Pen(12, 'eucalyptus', (117, 177, 165)),
    Pen(63, 'olive green', (65, 94, 56)),
    Pen(16, 'light emerald', (135, 198, 149)),
    Pen(53, 'pine green', (0, 118, 103)),
    Pen(36, 'green', (0, 146, 78)),
    Pen(54, 'orange', (234, 87, 37)),
    Pen(30, 'pale vermillion', (236, 103, 36)),
    Pen(54, 'neon orange', (251, 187, 50)),
    Pen(26, 'apricot', (246, 175, 148)),
    Pen(85, 'papaya', (229, 193, 126)),
    Pen(25, 'light orange', (227, 181, 130)),
    Pen(51, 'turquoise', (0, 155, 180)),
    Pen(22, 'nightblue', (34, 22, 92)),
    Pen(32, 'ultramarine', (0, 133, 205)),
    Pen(41, 'blue', (15, 66, 149)),
    Pen(57, 'azure', (28, 186, 222)),
    Pen(11, 'ice blue', (164, 218, 243)),
    Pen(31, 'neon blue', (63, 192, 240)),
    Pen(31, 'light blue', (0, 142, 207)),
    Pen(65, 'umber', (104, 83, 65)),
    Pen(89, 'dark ochre', (195, 97, 26)),
    Pen(88, 'light ochre', (209, 154, 86)),
    Pen(87, 'curry', (214, 182, 59)),
    Pen(75, 'sienna', (131, 78, 56)),
    Pen(86, 'beige', (231, 213, 184)),
    Pen(45, 'brown', (109, 64, 44)),
    Pen(46, 'black', (0, 19, 26)),
    Pen(28, 'blush', (204, 143, 138)),
    Pen(56, 'pink', (237, 110, 167)),
    Pen(56, 'neon pink', (237, 109, 166)),
    Pen(29, 'light pink', (240, 138, 159)),
    Pen(17, 'heliotrope', (228, 150, 192)),
    Pen(47, 'rust red', (201, 76, 81)),
    Pen(48, 'light red', (227, 0, 15)),
    Pen(50, 'crimson', (206, 16, 65)),
    Pen(49, 'strawberry red', (192, 68, 89)),
    Pen(40, 'neon red', (244, 167, 182)),
    Pen(38, 'sanguine', (195, 63, 52)),
    Pen(40, 'red', (227, 0, 15)),
    Pen(95, 'medium cold grey', (148, 155, 167)),
    Pen(96, 'dark grey', (106, 117, 135)),
    Pen(93, 'warm grey', (176, 172, 164)),
    Pen(94, 'light grey', (186, 201, 216)),
    Pen(97, 'deep cold grey', (78, 82, 92)),
    Pen(98, 'payne\'s grey', (27, 66, 110)),
    Pen(59, 'light lilac', (188, 153, 203)),
    Pen(19, 'purple', (179, 36, 81)),
    Pen(55, 'violet', (91, 34, 130)),
    Pen(60, 'plum', (146, 84, 147)),
    Pen(58, 'lilac', (154, 53, 181)),
    Pen(62, 'grey violet', (144, 106, 147)),
    Pen(67, 'mustard', (212, 208, 114)),
    Pen(44, 'yellow', (250, 210, 0)),
    Pen(23, 'light yellow', (247, 234, 160)),
    Pen(24, 'neon yellow', (252, 233, 0)),
    Pen(24, 'lemon yellow', (246, 234, 76)),
]

allow = [44,
         56,
         94,
         58,
         96,
         57,
         13,
         32,
         51,
         43,
         54,
         50,
         40,
         89,
         36,
         41,
         45,
         63,
         55,
         46,]

new_list: list[Pen] = []
for pen in pen_list:
    if pen.number not in allow:
        continue
    if not new_list:
        new_list.append(pen)
        continue
    index = shortest_index(pen.color, [new_pen.color for new_pen in new_list])
    if mean(pen.color) > mean(new_list[index].color):
        new_list.insert(index, pen)
    else:
        new_list.insert(index+1, pen)

max_len_1 = max(len(str(pen.number)) for pen in new_list)
max_len_2 = max(len(str(pen.name)) for pen in new_list)
max_len_3 = max(len(str(pen.color)) for pen in new_list)
for pen in new_list:
    print(f'{str(pen.number):<{max_len_1}}',
          f'{str(pen.name)  :<{max_len_2}}',
          f'{str(pen.color) :<{max_len_3}}')
