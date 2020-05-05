"""
Testing biotransformer wrapped web services performance when compared with
the biotransformer API.

Initially testing with 1 generation since that's the limit on their API.
"""

import requests
import json
import time
from bs4 import BeautifulSoup

import test_data



def curate_prediction_results():
	"""
	Testing conversion of prediction results to a nested tree for CTS.
	"""
	# data = test_data.test_data_1gen  # 1 generation of sample results
	data = test_data.test_data_2gen
	starting_compound = data['predictions'][0]['starting_compound']
	print("Starting compound: {}".format(starting_compound))
	metabolites_list = data['predictions'][0]['biotransformations']
	print("Number of metabolites: {}".format(len(metabolites_list)))
	tree_obj = make_map(metabolites_list)
	print("Final tree structure: {}".format(tree_obj))

def make_map(list_child_parent):
	"""
	Creates a nested dictionary from the biotransformer predictions data.
	"""
	has_parent = set()
	all_items = {}
	met_id = 1
	for metabolite_obj in list_child_parent:
		parent_obj = metabolite_obj['substrates'][0]
		child_obj = metabolite_obj['products'][0]	
		parent = parent_obj['inchikey']
		child = child_obj['inchikey']
		if parent not in all_items:
			all_items[parent] = {}
			all_items[parent]['id'] = met_id
			all_items[parent]['name'] = ""
			all_items[parent]['data'] = parent_obj
			all_items[parent]['children'] = []
			met_id += 1
		if child not in all_items:
			all_items[child] = {}
			all_items[child]['id'] = met_id
			all_items[child]['name'] = ""
			all_items[child]['data'] = child_obj
			all_items[child]['children'] = []
			met_id += 1
		all_items[parent]['children'].append(all_items[child])
		has_parent.add(child)
	result = {}
	for key, value in all_items.items():
		if key not in has_parent:
			result[key] = value
	return result



def api_query_and_status():
	"""
	Test API request routine.
	"""
	max_response_wait = 60  # seconds
	delay = 5
	delay_sum = 0
	data_received = False

	current_milli_time = lambda: int(round(time.time() * 1000))

	headers = {'Content-type': 'application/json', 'Accept': 'text/html'}

	base_url = 'http://biotransformer.ca'

	api_query = {
	  "biotransformer_option": "CYP450",
	  "number_of_steps": 1,
	  # "query_input": "acetaminophen\tCC(=O)NC1=CC=C(O)C=C1",
	  "query_input": "CC(=O)NC1=CC=C(O)C=C1",
	  "task_type": "PREDICTION"
	}

	start_time = current_milli_time()
	api_response = requests.post(base_url + '/queries.json', json=api_query, headers=headers)
	print("API RESPONSE: {}".format(api_response.content))

	soup = BeautifulSoup(api_response.content, features="html.parser")  # creates an object from the html response
	content = soup.find("div", {"id": "query-status"})  # gets div from response that has query/response id
	request_id = content.get('data-query-id')  # gets 'data-query-id' attr from div, which is the request's id

	print("Query ID: {}".format(request_id))

	# url = base_url + '/queries/' + request_id + '.json'
	url = base_url + '/queries/' + request_id + '.csv'

	while not data_received:
		print("Sleeping {}s before making request".format(delay))
		time.sleep(delay)
		result = requests.get(url)
		result_obj = json.loads(result.content)
		status = result_obj.get('status')
		print("Query Status: {}".format(status))
		if status == "Done":
			print("Predictions: {}".format(result_obj.get('predictions')))
			break
		elif float(delay_sum) / float(max_response_wait) > 1.0:
			print("Exceeded max wait for biotransformer response ({}s)".format(max_response_wait))
			break
		delay_sum += delay

	end_time = current_milli_time()
	print("Execution time: {}ms".format(end_time - start_time))



if __name__ == '__main__':
	# api_query_and_status()
	curate_prediction_results()