from harvest import *

def create_melon_objs(filename):
    melon_data = open(filename)
    melon_list = []
    for line in melon_data:
        attr = line.split(' ')
        shape_rate, color_rate, type_code = attr[1:7:2]
        # print(type_code)
        harvester = attr[-4]
        field = attr[-1]
        melon_type_dict = make_melon_type_lookup(make_melon_types())
        # print(melon_type_dict)
        # print(melon_type_dict[type_code])
        melon_type = melon_type_dict[type_code]
        melon = Melon(melon_type, shape_rate, color_rate, field, harvester)
        melon_list.append(melon)
    print(melon_list[0:10])

create_melon_objs('harvest_log.txt')

# (self, melon_type, shape_rate, color_rate, field, harvester)