#Use python3
import time
def timer(func):
	def newfunc(*args, **kws):
		t0 = time.time()
		result = func(*args, **kws)
		t1 = time.time()
		print(func.__name__,*args)
		print(t1 - t0)
		return result
	return newfunc

@timer	 
def project1(n):
	sumnum = 0
	for i in range(1,n+1):
		for j in range(i,n+1):
			for k in range(j**2,n+1):
				sumnum += 0 + 0 + 0
	return sumnum

if __name__ == "__main__":
	result0 = project1(250)
	result1 = project1(500)
	result2 = project1(1000)
	result3 = project1(2000)
	result4 = project1(4000)




