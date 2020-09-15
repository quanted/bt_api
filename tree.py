import csv
from models.product import Product



class Tree:

	def __init__(self):
		self.keys = [
			"InChI",
			"InChIKey",
			"SMILES",
			"Synonyms",
			"PUBCHEM_CID",
			"Molecular formula",
			"Major Isotope Mass",
			"ALogP",
			"Lipinski_Violations",
			"Insecticide_Likeness_Violations",
			"Post_Em_Herbicide_Likeness_Violations",
			"Metabolite ID",
			"cdk:Title",
			"Reaction",
			"Reaction ID",
			"Enzyme(s)",
			"Biosystem",
			"Precursor ID",
			"Precursor SMILES",
			"Precursor InChI",
			"Precursor InChIKey",
			"Precursor ALogP",
			"Precursor Major Isotope Mass"
		]  # v1.1.5 keys

	def _get_metabolite_id(self):
		"""
		Gets ID number from biotransformer CSV's "Metabolite ID" key.
		"""
		pass

	def parse_csv_results(self, csv_data):
		"""
		Gets data from CSV results and formats
		data to be converted to a tree structure.
		"""
		new_csv_data = [] 
		metID = 1  # use unique id like this, or just use the product's metabolite id (duplicate ids for same products)
		for row in csv_data:
			# row = dict(row)
			new_csv_data.append({
				"id": row["Metabolite ID"],
				"parent": row["Precursor ID"],
				"data": {
					"smiles": row["SMILES"],
					"routes": row["Reaction"]
				}
			})
			metID += 1
		return new_csv_data

	def traverse(self, orig_tree, new_tree):

		# NOTE: genKey gets added on the frontend, cts_gentrans_tree.html

		trav_index = 0
		for node in orig_tree:
			if node['parent'] == new_tree['id']:
				new_tree['children'].append(Product(
					id=node['id'],
					children=[],
					data=node['data'],
					name=None
				).__dict__)
				trav_index += 1
			else:
				new_parent = node['parent']
				child_index = 0
				for _node in new_tree['children']:
					if _node['id'] == new_parent:
						new_tree['children'][child_index] = Product(
							id=_node['id'],
							children=[],
							data=node['data'],
							name=None
						).__dict__
						new_tree_2 = new_tree['children'][child_index]
						orig_tree_2 = orig_tree[trav_index:]
						self.traverse(orig_tree_2, new_tree_2)
					child_index += 1
		return new_tree



if __name__ == "__main__":

	csv_file = open("results3.csv")
	csv_dict = csv.DictReader(csv_file)
	print("\nRaw CSV data: {}\n".format(csv_dict))
	
	results_parser = CSVResults()
	csv_data = results_parser.parse_csv_results(csv_dict)
	csv_file.close()
	print("\nCurated CSV data: {}\n".format(csv_data))

	# NOTE: (For BTM000X IDs) Make sure this initial 'id' is parent's "precusor id", which is "" (blank string)
	# tree = {'id': -1, 'children': [], 'data': {}}
	tree = {'id': "", 'children': [], 'data': {}}
	tree_data = results_parser.traverse(csv_data, tree)
	print("\nTree structure: {}\n".format(tree_data))