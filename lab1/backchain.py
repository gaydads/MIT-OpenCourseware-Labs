from re import split
from production import AND, OR, NOT, PASS, FAIL, IF, THEN, \
	 match, populate, simplify, variables
from zookeeper import ZOOKEEPER_RULES

# This function, which you need to write, takes in a hypothesis
# that can be determined using a set of rules, and outputs a goal
# tree of which statements it would need to test to prove that
# hypothesis. Refer to the problem set (section 2) for more
# detailed specifications and examples.

# Note that this function is supposed to be a general
# backchainer.  You should not hard-code anything that is
# specific to a particular rule set.  The backchainer will be
# tested on things other than ZOOKEEPER_RULES.

# Backchain for antecedents found in matching hypothesis
def antecedent_goal_tree(rule, rules, binding):
	subtrees = OR()
	if (isinstance(rule.antecedent(), (AND))):
		subtrees = AND()
		for antecedent in rule.antecedent():
			new_hypothesis = populate(antecedent, binding)
			subtrees.append(backchain_to_goal_tree(rules, new_hypothesis))
	elif (isinstance(rule.antecedent(), (OR))):
		subtrees = OR()
		for antecedent in rule.antecedent():
			new_hypothesis = populate(antecedent, binding)
			subtrees.append(backchain_to_goal_tree(rules, new_hypothesis))
	else:
		new_hypothesis = populate(rule.antecedent(), binding)
		subtrees.append(backchain_to_goal_tree(rules, new_hypothesis))
		return subtrees
	return subtrees


# Backchain for each hypothesis/rule
def backchain_to_goal_tree(rules, hypothesis):
	subtrees = OR()
	subtrees.append(hypothesis)
	isNoMatch = True
	for rule in rules:
		if (match(rule.consequent()[0], hypothesis) != None):
			isNoMatch = False
			binding = match(rule.consequent()[0], hypothesis)
			subtree = antecedent_goal_tree(rule, rules, binding)
			subtrees.append(subtree)
	if isNoMatch:
		return hypothesis
	return simplify(subtrees)

# Alternate implementation
# def backchain_to_goal_tree(rules, hypothesis):
    
#     length = len(rules) 

#     if length==0:
#         return hypothesis
#     tree = OR()
    
#     for element in rules:
#         con = element.consequent()
#         mat = match(con[0], hypothesis)
#         if mat is not None and len(mat)>=0:
#             antec = element.antecedent()
#             if isinstance(antec, list):
#                 sub = AND()
#                 if isinstance(antec, OR): sub = OR()
#                 for x in antec:
#                     new_tree = backchain_to_goal_tree(rules, populate(x, mat))
#                     sub.append(new_tree)
#                 tree.append(sub)
#             else:
#                 new_tree = backchain_to_goal_tree(rules, populate(antec, mat))
#                 tree.append(AND(new_tree))
#         else:
#             tree.append(hypothesis)
#     new = simplify(tree)
#     return new

# it to see it work:
print('subtrees: ', backchain_to_goal_tree(ZOOKEEPER_RULES, 'opus is a penguin'))