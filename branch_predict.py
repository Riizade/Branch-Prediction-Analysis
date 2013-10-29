import random


num_branches = 1000 #must be at least 1

def test_prediction(branch_distribution, predictor):
	prediction_distribution = [] #distribution of predictions
	num_taken = 0 #number of branches taken

	#for each branch in the distribution
	for b in branch_distribution:
		prediction_distribution.append(predictor.predict()) #predict the branch
		predictor.update(b) #update the predictor with whether the branch was taken or not
		#update num_taken
		if(b == 1):
			num_taken += 1

	#calculate % predictions correct
	num_correct = 0
	for i in range(len(branch_distribution)):
		if (branch_distribution[i] == prediction_distribution[i]):
			num_correct += 1


	proportion_correct = (float(num_correct) / float(len(branch_distribution))) * 100
	print(str(len(branch_distribution)) + " predictions were tested, " + str(proportion_correct) + "% were correct.")
	print("In this distribution, " + str(num_taken) + " branches were taken (" + str(float(num_taken * 100) / float(num_branches)) + "%), " + str(num_branches - num_taken) + " were not taken (" + str(float((num_branches - num_taken) * 100) / float(num_branches)) + "%).")

def generate_branch(prev_branch):
	cur_branch = 0

	if(prev_branch == 1):

	else:
		cur_branch = random.randint(0,1)

def generate_distribution(dist):
	value = float(random.randint(0,1000)) / float(1000)
	for i in dist:
		if (value <=)


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


