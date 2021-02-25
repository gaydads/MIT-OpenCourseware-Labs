
tree = (((1, 2), 3), (4, (5, 6)), 7, (8, 9, 10))



def tree_ref(tree, index):
	if len(index) > 1:
		print(tree[index[0]])
		return tree_ref(tree[index[0]], index[1:])
	else:
		return tree[index[0]]
	# print(index)
	# print('Tuple Len?: ', len(index))
	# index = index[1:]
	# print(index)
	# print('Tuple Len?: ', len(index))
	# index = index[1:]
	# print(index)
	# print('Tuple Len?: ', len(index))
	# index = index[1:]
	# print(index)
	# print('Tuple Len?: ', len(index))

	# shortener = 

	# while isinstance(index, (tuple)):
	# 	index = index[1:]
	# 	print(tree[index])

	# while (next(index, None) != None):
	# 	print(next(myit))
	
	# if isinstance(index, (tuple)):

		# print('index is tuple: ', index)
		# tree_path = [[index[0]]]
		# for i in index[1:]:
		# 	print('Arr: ', [index[i]])
		# 	tree_path.extend([[index[i]]])
		# print ('TP: ', tree_path)


		# return tree_ref(tree[index[0]], index[1])
	# else:
	# 	print('index is not tuple: ', index)
	# 	return tree[index]

# print('treeeeee: ', tree[3, [1]])


	# print(tree)


	# return tree [0]


index1 = (3,1)
# print(tree_ref(tree, index1))

index2 = (3)
# print(tree_ref(tree, index2))

index = (1,1,1)


index = (0,)

print('Expecting: 9 - Actual: ', tree_ref(tree, (3,1)) )

print('Expecting: 6 - Actual: ', tree_ref(tree, (1,1,1)))

print('Expecting: ((1, 2), 3) - Actual: ', tree_ref(tree, (0,)))