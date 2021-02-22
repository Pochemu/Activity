collections = ['list', 'tuple', 'dict', 'set']

collections.append('OrderedDict')
print(collections)

collections.extend(['ponyset', 'unicorndict'])
print(collections)

collections += [None]
print(collections)

del collections[7]
print(collections)

print(', '.join(collections))