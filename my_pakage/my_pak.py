def my_fun(x):
	i = 0
	while i < x:
		yield i
		i += 1
	    yield i * 2
