# def factorial(x):
# 	if x - 1 == 0 :
# 		return x
# 	else :
# 		return x * factorial (x-1)

# def factorial2(x):
# 	if x == 0:
# 		return 1
# 	elif x <= 0:
# 		raise Exception, "factorial: input must not be negative"
# 	else:
# 		fact = 0
# 		for i in range(1,x+1):
# 			fact = fact * x
		
# 		return fact

# # print(factorial(1))
# # print(factorial2(-1))


# def cube(x):
#     return x*x*x;


# print(cube(-3))


# for i in range(1,x+1):


# pattern = ('a', 'b')

# print(pattern)







def count_pattern(pattern, lst):
	count = 0
	pattern_length = len(pattern)
	print (len(lst) <= len(pattern))
	if ( len(lst) <= len(pattern) ) :
		print('here')
		if pattern == lst :
			print('here2')
			return 1
	else :
		print('pattern', pattern)
		print('lst', lst[0:len(pattern)])
		print(pattern == lst[0:len(pattern)])
		if ( pattern == lst[0:len(pattern)] ):
			print('here')
			count = 1 + count_pattern(pattern, lst[1:len(lst)])
		else:
			count = count_pattern(pattern, lst[1:len(lst)])
	return count




pattern = [2,3]

lst = [1,2,3,2,3,4,3,4,5]

# print(count_pattern(pattern, lst))


# def depth(expr):
	# depth = 0
	# if (isinstance(expr, (tuple))):
	# 	depth += 1
	# 	for item in expr:
	# 		depth += depth(item)
	# else:
	# 	return depth
	# return depth
	# return 0

# depth('x')

# def test_answer():
# 	correct = 0
# 	total = 0
# 	total += 1
# 	if depth('x') == 0:
# 		correct += 1

# 	total += 1
# 	if depth(('expt', 'x', 2)) == 1:
# 		correct += 1

	# total += 1
	# if depth(('+', ('expt', 'x', 2), ('expt', 'y', 2))) == 2:
	# 	correct += 1
	
	# total += 1
	# if depth(('/', ('expt', 'x', 5), ('expt', ('-', ('expt', 'x', 2), 1), ('/', 5, 2)))) == 4:
	# 	correct += 1
		
	# print("[" + str(correct) + "/" + str(total) + "] correct answers")

		

# test_answer()


x = ('ok', 'ok2')
y = 'ok'
z = (('ok', 'ok', 'ok', ('ok')))

# print(isinstance(x, (tuple )))
# print(isinstance(y, (tuple )))
# print(isinstance(z, (tuple )))

# print(len (x))
# print(len (y))
# print(len (z))

# for x in z:
# 	if (isinstance(x, (tuple))):
# 		print(x)

# def dig_deeper(expr, level):
# 	if (isinstance(expr, (tuple))):
# 		level += 

# def depthtest(expr):
# 	print('here')
# 	depths = [depthtest(expr) for item in expr if isinstance(item, tuple)]
# 	print(depths)
# 	if len(depths) > 0 :
# 		return (1 + max(depths))
# 	return 1

# print('tests:::::::::::::::::')

# a = ('expt', 'x', 2)

# print(depthtest(x))
# print(depthtest(y))
# print(depthtest(z))
# # print(depthtest(('expt', 'x', 2)))

# # print(depthtest(('expt', 'x', 2)) == 1)

# print(x[len(x)-1])


def depth(expr):
   if isinstance(expr, tuple):
	   depths = [depth(item) for item in expr if isinstance(item, tuple)]
	   if len(depths) > 0:
		   return 1 + max(depths)
	   else:
		   return 1
   else:
	   return 0

#    depths = [depth(item, counter) if isinstance(item, tuple) else 0 for item in l]
#    print(item)
#    print(counter)
#    print(depths)
#    return depths;
   
   
#    return squares2
   
    # depths = [depth(item) for item in l if isinstance(item, tuple)]
	# if (True):
	# 	print('D: ', depths)
	# 	return 1
    # if len(depths) > 0:
    #     return 1 + max(depths)
	# print('hey')
    # return 1


# squares = list(map(lambda x: x**2, range(10)))
# print('squares:', squares)

# squares2 = [x**2 for x in range(10) if (x < 5)]
# print('squares2:', squares2)

ls0 = ('x')
ls2 = ('expt', 'x', 2)
ls3 = ('+', ('expt', 'x', 2), ('expt', 'y', 2))
ls4 = ('/', ('expt', 'x', 5), ('expt', ('-', ('expt', 'x', 2),1), ('/', 5, 2)))

ls1 = ( ('x', ('y', 'z') )     )
tuples = [ls0, ls2, ls3, ls4]
# , ls1, ls2, ls3, ls4]
for tup in tuples:
    print(depth(tup))

# print('break')
# l = ('+', ('expt', 'x', 2), ('expt', 'y', 2))

# d = 0

# def go(expr):
# 	depths = [item for item in expr]
# 	if isinstance(item, tuple):
# 		go(item)
# 	print(depths)

# go(l)