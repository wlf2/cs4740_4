#!/usr/bin/env python
from combine import *
import chunker
import mlpy

def question_candidates(q_id):
#Incomplete
	'''Select some useful subset of the candidates for a particular question.
	Return them in a list.
	'''
	all_chunks = chunker.run(q_id)
	return all_chunks[:40] # need better way to filter

def all_candidates(first = 201, last = 399):
	# make sure the parameters are good
	if first > last: last, first = first, last
	# list of question id numbers
	q_ids=range(first,last+1)
	return reduce(lambda a,b: a+question_candidates(b),q_ids,[])

def check_candidates(candidates,q_id=204):
	#Put q_id in the candidates storage thingy
	return map(lambda a: check_answers.check_answer(q_id,a),candidates)

def run_validation():
	candidates_train=all_candidates(first = 201, last = 359)
	y_train=check_candidates(candidates_train)
	
	candidates_validation=all_candidates(first = 360, last = 399)
	y_validation=check_candidates(candidates_validation)

	evaluator_combinations=[
	[dummy_evaluator],
	[dummy_evaluator2],
	[dummy_evaluator,dummy_evaluator2]
	]

	validation_runs=[]
	for combination in evaluator_combinations:
		x_train=run_evaluators(candidates_train,combination)
		x_validation=run_evaluators(candidates_validation,combination)

		#Vary parameters here
		for model in [mlpy.Svm,mlpy.Fda]:
		#Incomplete
			model_trained=train(model,y_train,x_train)
			#Return a list of scores and corresponding candidates
			#It would be nice to sort this by question
			print map(lambda a:[test(model_trained,a),a],x_validation)
			#Then select the best answers and send to the scorer
			#And then get the score
			score = 0.72
			#Then return the overall score of the validation run
			validation_runs.append((score,model_trained,model,combination))
	return validation_runs

def select_parameter_combination(validation_runs):
#Incomplete
	#Select the best parameter combination from the validation runs
	#This currently picks just the first combination.
	return validation_runs[0][1]

def run_test(model_trained):
	#Run the model on the test data
	candidates_test=all_candidates(first = 10000, last = 10035)
	x_test=run_evaluators(candidates_test)
	y_test=check_candidates(candidates_test)
	#Check the score
	score=0.68
	return score

def main():
	runs=run_validation()
	#Save runs to a file so we can write about it
	out=open('validation_runs','w')
	out.write(str(runs))
	out.close()
	#Then select the best run and use it to run the test
	print run_test(select_parameter_combination(runs))

if __name__ == '__main__':
	main()
