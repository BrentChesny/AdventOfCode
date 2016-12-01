import re, operator
ingredients = [map(int, re.findall("(-?[\d]+)", line)) for line in open("input.txt")]
maxscore = 0

def a(i, left, scores):
	global maxscore

	if i == len(ingredients):
		score = reduce(operator.mul, [max(b,0) for b in scores[:-1]])
		if score > maxscore and scores[-1] == 500:
			maxscore = score
		return

	for x in xrange(0,left + 1):
		s = [z[0] + z[1] for z in zip(scores, [x*b for b in ingredients[i]])]
		a(i+1, left-x, s) 

a(0, 100, [0 for x in xrange(len(ingredients[0]))])
print maxscore