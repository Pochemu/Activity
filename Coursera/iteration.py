collections = ['list', 'tuple', 'dict', 'set']

for collection in collections:
    print('Learning {}...'. format(collection))

for idx, collection in enumerate(collections):
    print('#{} {}'.format(idx, collection))

for idx, collection in enumerate(collections):
    print('#{i} {}'.format(collection, i=idx))
