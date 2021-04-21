def f(k1, k2, w, step):
	if k1 + k2 >= w and step == 2:
		return True
	else:
		if k1 + k2 < w and step == 2:
			return False
	return (f(k1+1, k2, w, step + 1) or
					f(k1, k2+1, w, step + 1) or
					f(k1*2, k2, w, step + 1) or
					f(k1, k2*2, w, step + 1))
				
				
for S in range(1, 31):
	if f(9, S, 40, 0):
		print(S)
		break
