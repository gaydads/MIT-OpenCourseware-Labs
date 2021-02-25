from production import IF, AND, OR, NOT, THEN, forward_chain


# Problem 1.3.1: Poker hands

# You're given this data about poker hands:
poker_data = ( 'two-pair beats pair',
			   'three-of-a-kind beats two-pair',
			   'straight beats three-of-a-kind',
			   'flush beats straight',
			   'full-house beats flush',
			   'straight-flush beats full-house' )

# Fill in this rule so that it finds all other combinations of
# which poker hands beat which, transitively. For example, it
# should be able to deduce that a three-of-a-kind beats a pair,
# because a three-of-a-kind beats two-pair, which beats a pair.
# transitive_rule = IF( AND(), THEN() )

transitive_rule =IF(AND( '(?x) beats (?y)',
					'(?y) beats (?z)' ),
	  			THEN( '(?x) beats (?z)' ))

# You can test your rule like this:
# print('forward chain: ', forward_chain([transitive_rule], poker_data))

# Here's some other data sets for the rule. The tester uses
# these, so don't change them.
TEST_RESULTS_TRANS1 = forward_chain([transitive_rule],
									[ 'a beats b', 'b beats c' ])
TEST_RESULTS_TRANS2 = forward_chain([transitive_rule],
  [ 'rock beats scissors', 
	'scissors beats paper', 
	'paper beats rock' ])

# print('TEST_RESULTS_TRANS1: ', TEST_RESULTS_TRANS1)
# print('TEST_RESULTS_TRANS2: ', TEST_RESULTS_TRANS2)
# Problem 1.3.2: Family relations

# First, define all your rules here individually. That is, give
# them names by assigning them to variables. This way, you'll be
# able to refer to the rules by name and easily rearrange them if
# you need to.

#Apply self:
apply_self_rule=IF(OR(
	'male (?x)',
	'female (?x)'),
	THEN(
	'self (?x) (?x)'
	)
)

# 'brother x y': x is the brother of y (sharing at least one parent)
brother_rule =IF (
	AND(
		'male (?x)',
		'parent (?y) (?x)',
		'parent (?y) (?z)',
		NOT('self (?x) (?z)')
	),
	THEN (
		'brother (?x) (?z)'
	)
)
# 'sister x y': x is the sister of y (sharing at least one parent)  
sister_rule=IF(
	AND(
		'female (?x)',
		'parent (?y) (?x)',
		'parent (?y) (?z)',
		NOT('self (?x) (?z)')
	),
	THEN (
		'sister (?x) (?z)'
	)
)
# 'mother x y': x is the mother of y
mother_rule=IF(
	AND(
		'female (?x)',
		'parent (?x) (?y)'
	),
	THEN (
		'mother (?x) (?y)'
	)
)

# 'father x y': x is the father of y
father_rule=IF(
	AND(
		'male (?x)',
		'parent (?x) (?y)'
	),
	THEN (
		'father (?x) (?y)'
	)
)
# 'son x y': x is the son of y
son_rule=IF(
	AND(
		'male (?x)',
		'parent (?y) (?x)'
	),
	THEN (
		'son (?x) (?y)'
	)
)
# 'daughter x y': x is the daughter of y
daughter_rule=IF(
	AND(
		'female (?x)',
		'parent (?y) (?x)'
	),
	THEN (
		'daughter (?x) (?y)'
	)
)
# 'cousin x y': xand y are cousins (a parent of x and a parent of y are siblings)  
cousin_rule=IF(
	AND(
		'parent (?p1) (?x)',
		'parent (?p2) (?y)',
		OR('brother (?p1) (?p2)',
		'brother (?p2) (?p1)',
		'sister (?p1) (?p2)',
		'sister (?p2) (?p1)'),
		NOT('brother (?x) (?y)'),
		NOT('brother (?y) (?x)'),
		NOT('sister (?x) (?y)'),
		NOT('sister (?y) (?x)'),
	),
	THEN (
		'cousin (?x) (?y)'
	)
)
# 'grandparent x y': x is the grandparent of y
grandparent_rule=IF(
	AND(
		'parent (?x) (?y)',
		'parent (?y) (?z)'
	),
	THEN (
		'grandparent (?x) (?z)'
	)
)

# 'grandchild x y': x is the grandchild of y
grandchild_rule=IF(
	AND(
		'parent (?x) (?y)',
		'parent (?y) (?z)'
	),
	THEN (
		'grandchild (?z) (?x)'
	)
)

# Then, put them together into a list in order, and call it
# family_rules.
family_rules = [
	apply_self_rule,
	brother_rule,
	sister_rule,
	mother_rule,
	father_rule,
	son_rule,
	daughter_rule,
	cousin_rule
]	# fill me in

# Some examples to try it on:
# Note: These are used for testing, so DO NOT CHANGE
simpsons_data = ("male bart",
				 "female lisa",
				 "female maggie",
				 "female marge",
				 "male homer",
				 "male abe",
				 "parent marge bart",
				 "parent marge lisa",
				 "parent marge maggie",
				 "parent homer bart",
				 "parent homer lisa",
				 "parent homer maggie",
				 "parent abe homer")
TEST_RESULTS_6 = forward_chain(family_rules,
							   simpsons_data,verbose=False)
# You can test your results by uncommenting this line:
# print('family rules:', family_rules)
print (forward_chain(family_rules, simpsons_data, verbose=True))

print("MOVING ON =============")

black_data = ("male sirius",
			  "male regulus",
			  "female walburga",
			  "male alphard",
			  "male cygnus",
			  "male pollux",
			  "female bellatrix",
			  "female andromeda",
			  "female narcissa",
			  "female nymphadora",
			  "male draco",
			  "parent walburga sirius",
			  "parent walburga regulus",
			  "parent pollux walburga",
			  "parent pollux alphard",
			  "parent pollux cygnus",
			  "parent cygnus bellatrix",
			  "parent cygnus andromeda",
			  "parent cygnus narcissa",
			  "parent andromeda nymphadora",
			  "parent narcissa draco")
print (forward_chain(family_rules, black_data, verbose=True))
# This should generate 14 cousin relationships, representing
# 7 pairs of people who are cousins:

black_family_cousins = [ 
	x for x in 
	forward_chain(family_rules, black_data, verbose=False) 
	if "cousin" in x ]

# To see if you found them all, uncomment this line:
print ('Black Family', len(black_family_cousins))

# To debug what happened in your rules, you can set verbose=True
# in the function call above.

# Some other data sets to try it on. The tester uses these
# results, so don't comment them out.

TEST_DATA_1 = [ 'female alice',
				'male bob',
				'male chuck',
				'parent chuck alice',
				'parent chuck bob' ]
TEST_RESULTS_1 = forward_chain(family_rules, 
							   TEST_DATA_1, verbose=False)

TEST_DATA_2 = [ 'female a1', 'female b1', 'female b2', 
				'female c1', 'female c2', 'female c3', 
				'female c4', 'female d1', 'female d2', 
				'female d3', 'female d4',
				'parent a1 b1',
				'parent a1 b2',
				'parent b1 c1',
				'parent b1 c2',
				'parent b2 c3',
				'parent b2 c4',
				'parent c1 d1',
				'parent c2 d2',
				'parent c3 d3',
				'parent c4 d4' ]

TEST_RESULTS_2 = forward_chain(family_rules, 
							   TEST_DATA_2, verbose=False)

TEST_RESULTS_6 = forward_chain(family_rules,
							   simpsons_data,verbose=False)