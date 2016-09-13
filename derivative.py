def derivative(a):
    d = []
    for i in range(0, len(a)-2):
	d.append((a[i+1] - a[i]) / 0.1)
    return d
