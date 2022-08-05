"""
Calling biotransformer from Python.
https://bitbucket.org/djoumbou/biotransformerjar
"""

import subprocess
import logging
import os
import uuid
import glob
import time
import csv

# Local imports:
from models.product import Product
from tree import Tree

PROJECT_ROOT = os.path.abspath(os.path.dirname(__file__))
print("PROJECT_ROOT: {}".format(PROJECT_ROOT))

# BT_JAR_PATH = os.environ.get('BT_JAR_PATH', os.path.join(PROJECT_ROOT, "biotransformerjar", "biotransformer-1-0-9.jar"))
BT_JAR_PATH = os.environ.get('BT_JAR_PATH', os.path.join(PROJECT_ROOT, "biotransformerjar"))
print("BT_JAR_PATH: {}".format(BT_JAR_PATH))

BT_JAR_NAME = os.environ.get("BT_JAR_NAME", "BioTransformer3.0_20220504.jar")

# JAVA_PATH = os.environ.get('JAVA_PATH')  # isn't there an env for this already?



class BTCLI:

	def __init__(self):

		# CLI Args/Options:
		self.tasks = ["pred", "cid"]  # predictions or compund identification
		self.bt_options = ["ecbased", "cyp450", "phaseII", "hgut", "superbio", "envimicro"]
		self.input_types = ["--ismiles", "--molinput", "--sdfinput"]
		self.output_types = ["--csvoutput", "--sdfoutput"]
		self.gen_limit = "--nsteps"
		self.masses = "-m"  # or --mSteps - given starting compound, finds all metabolites with specified masses, and show a metabolism pathway. A whitespace-separated list of masses is expected.
		self.mass_tolerance = "-t"  # or --mTolerance - Mass tolerance for metabolite identification (default is 0.01)
		self.formulas = "-f"  # or --formulas - semicolon-separated list of formulas of compunds to identify
		self.annotate = "-a"  # or --annotate - serach PuChem for each product, and annotate with CID and synonyms

		# CLI Example(s):
		self.cli_example_1 = "java -jar biotransformer-1-0-8.jar --task pred --btType cyp450 --ismiles CCCO --csvoutput results.csv --nsteps 3"

	# def execute_bt(self, smiles, pred_type, gen_limit, predictions_filename):
	# 	"""
	# 	Executes biotransformer jar file for predictions.
	# 	"""
	# 	subprocess.run(["java", "-jar", "biotransformer-1.1.5.jar",
	# 		"--task", "pred",
	# 		"--btType", pred_type,
	# 		"--ismiles", smiles,
	# 		"--csvoutput", predictions_filename,
	# 		"--nsteps", str(gen_limit)
	# 	], cwd=BT_JAR_PATH)

	def execute_bt3(self, smiles, pred_type, gen_limit, predictions_filename):
		"""
		Executes biotransformer jar file for predictions.
		"""
		subprocess.run(["java", "-jar", BT_JAR_NAME,
			"--task", "pred",
			"--btType", pred_type,
			"--ismiles", smiles,
			"--csvoutput", predictions_filename,
			"--nsteps", str(gen_limit)
		], cwd=BT_JAR_PATH)

	def build_endpoint_args(self):
		"""
		Creates string of endpoint args (pchem properties) to predict.
		Note: cts_endpoints from opera_cli_args.CLIArgs.
		Command-line example: opera -s input_file.smi -o predictions.csv -e MP BP logVP
		"""
		arg_string = ""
		for endpoint in self.cts_endpoints:
			arg_string += endpoint + " "
		return arg_string

	def generate_filename(self):
		"""
		Generates a universally unique identifier for temp filenames.
		"""
		return str(uuid.uuid4())

	def remove_temp_files(self, *args):
		"""
		Closes and removes input and output temp files.
		"""
		for tempfile in args:
			tempfile.close()
			os.remove(tempfile.name)

	def remove_all_temp_files(self):
		"""
		Removes all temp files.
		"""
		for file in glob.glob("temp/*"):
			os.remove(file)

	def get_predictions_orig(self, predictions_filename):
		"""
		Reads result CSV and returns predictions.
		TODO: Parse output to make sense for CTS.
		"""
		tempfile_obj = open(predictions_filename)
		content = tempfile_obj.read()
		tempfile_obj.close()
		return content

	def get_predictions(self, parent_smiles, predictions_filename):
		init_tree = Product(id="", parent_id=None, children=[], data={'smiles': parent_smiles}, name=None).__dict__
		if not os.path.isfile(predictions_filename):
			return {
				"tree": init_tree,
				"total_products": 0,
				"unique_products": 0
			}
		tree_builder = Tree()
		with open(predictions_filename) as csv_file:
			csv_dict = csv.DictReader(csv_file)
			csv_data = tree_builder.parse_csv_results(csv_dict)
		# return csv_data

		tree_builder.num_products = len(csv_data)
		tree, unique_products = tree_builder.traverse(parent_smiles, csv_data)
		return {
			"tree": tree,
			"total_products": len(csv_data),
			"unique_products": len(unique_products)
		}

	def run_bt_routine(self, smiles, pred_type="ecbased", gen_limit=1):
		"""
		Runs full biotransformer CLI routine.
		"""
		start = time.time()
		try:
			predictions_full_path = os.path.join(PROJECT_ROOT, "temp", self.generate_filename() + ".csv")  # generates unique filename
			# print("Predictions CSV path: {}".format(predictions_full_path))
			# self.execute_bt(smiles, pred_type, gen_limit, predictions_full_path)  # runs opera cli
			self.execute_bt3(smiles, pred_type, gen_limit, predictions_full_path)  # runs opera cli
			# print("Finished executing biotransformer CLI.")
			predictions_data = self.get_predictions(smiles, predictions_full_path)  # gets predictions from .csv
			self.remove_all_temp_files()
			# print("Results: {}".format(predictions_data))
		except Exception as e:
			logging.warning("Exception running biotransformer: {}".format(e))
			return {"error": "Error getting data from biotransformer."}
		end = time.time()
		print("Execution time (s): {}".format(end - start))
		return predictions_data



if __name__ == '__main__':
	bt_cli = BTCLI()
	bt_cli.run_bt_routine("CC(=O)OC1=C(C=CC=C1)C(O)=O", "ecbased", 2)
