def f(k1, k2, w, step):
	if k1 + k2 >= w and step == 2:
		return True
	else:
		if k1 + k2 < w and step == 2:
			return False
	return (f(k1 + 2, k2, w, step+1) or
					f(k1, k2 + 2, w, step+1) or
					f(k1 * 2, k2, w, step+1) or
					f(k1, k2 * 2, w, step+1))


for s in range(1, 70):
	if f(5, s, 75, 0):
		print(s)
		break
