import dill

counter = 0

for i in range(100):
    counter += 1
    if i == 25:
        dill.dump_module('mySession.dil')

dill.load_module('mySession.dil')
print(counter)