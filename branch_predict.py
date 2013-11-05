import random

def test_prediction(br_dist, predictor):
	# distribution of predictions
	pred_dist = []
	# number of branches taken
	num_taken = 0

	# for each branch in the distribution
	for b in br_dist:
		# predict the branch
		pred_dist.append(predictor.predict())
		# update the predictor with whether the branch was taken or not
		predictor.update(b)
		# update num_taken
		if(b == 1):
			num_taken += 1

	# calculate % predictions correct
	num_correct = 0
	for i in range(len(br_dist)):
		if (br_dist[i] == pred_dist[i]):
			num_correct += 1

	# prints
	# - the number of predictions tested
	# - the percentage of those predictions that were correct
	# - the number of branches taken in the distribution (and %)
	# - the number of branches not taken (and %)
	proportion_correct = (float(num_correct) / float(len(br_dist))) * 100
	print(str(len(br_dist)) + " predictions were tested, " 
			+ str(proportion_correct) + "% were correct.")
	print("In this distribution, " + str(num_taken) + " branches were taken (" 
			+ str(float(num_taken * 100) / float(num_branches)) + "%), " 
			+ str(num_branches - num_taken) + " were not taken (" 
			+ str(((num_branches - num_taken) * 100) / float(num_branches)) 
			+ "%).")

def generate_distribution(num_branches):
	dist = []
	value = random.randint(0,1000)
	for i in dist:
		if (value <= 200):
			dist.append(0)
		elif (value <= 1000):
			dist.append(1)

	return dist

class twobit_saturated_counter:
	counter = 2
	def predict():
		if (counter >= 2):
			return 1
		if (counter <= 1):
			return 0
	def update(taken):
		if (taken == 1 and counter <3):
			counter += 1
		if (taken == 0 and counter >0):
			counter -= 1


