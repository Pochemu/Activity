fedor_house = list(map(int, input().split()))
pechkin_house = list(map(int, input().split()))
kotelna_fedor = [0,0]
if fedor_house[0] > 0:
    kotelna_fedor[0] = fedor_house[0]-1
elif fedor_house[0] < 0:
    kotelna_fedor[0] = (fedor_house[0] + 1)*-1

if fedor_house[1] > 0:
    kotelna_fedor[1] = fedor_house[1]-1
elif fedor_house[1] < 0:
    kotelna_fedor[1] = (fedor_house[1] + 1)*-1

print(fedor_house, pechkin_house, kotelna_fedor)