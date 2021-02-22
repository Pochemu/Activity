collections_map = {
    'mutable': ['list', 'set', 'dict'],
    'immutable': ['tuple', 'frozenset']
}
print(collections_map['immutable'])
print(collections_map.get('irresistible', 'not found'))