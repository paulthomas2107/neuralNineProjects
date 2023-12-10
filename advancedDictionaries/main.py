from benedict import benedict

normal_dict = {'a': {'b': {'c': 10}}}

print(normal_dict['a']['b']['c'])

special_dict = benedict(normal_dict.a.b.c)
