def f(x, y, A):
	f = ((x < 6) <= (x * x < A)) and ((y * y <= A) <= (y <= 6))
	return f

def main():
	res = 0
	for A in range(100):
		arr = [f(x, y, A) for x in range(100) for y in range(100)]
		if arr.count(True) == 10000:
			res += 1
	print(res)

main()  # 23