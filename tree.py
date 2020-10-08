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

		self.trav_index = 0  # tracks tree traversal
		self.num_products = 0  # number of products in tree

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
		metabolite_id_list = []
		metID = 1  # use unique id like this, or just use the product's metabolite id (duplicate ids for same products)
		for row in csv_data:

			product_parent_id = row["Metabolite ID"] + "-" + row["Precursor ID"]

			if product_parent_id in metabolite_id_list:
				print("product_parent_id already exists, skipping: {}".format(product_parent_id))
				continue

			new_csv_data.append(Product(
				id = str(metID),  # NOTE: may need unique id
				parent_id = row["Precursor ID"].split("0")[-1],
				data = {
					"smiles": row["SMILES"],
					"routes": row["Reaction"]
				},
				name = None,
				children = []
			).__dict__)

			# Only add product if it's (Medtabolite ID) doesn't already exist with the same parent (Precursor ID)
			metabolite_id_list.append(row["Metabolite ID"] + "-" + row["Precursor ID"])

			metID += 1

		return new_csv_data

	def traverse(self, parent_smiles, products_list):
		root = Product(id="", parent_id=None, children=[], data={'smiles': parent_smiles}, name=None).__dict__
		node_list = {'': root}
		for i in range(0, len(products_list)):
			node_list[products_list[i]['id']] = products_list[i]
			parent_index = products_list[i]['parent_id']
			child_index = node_list[products_list[i]['id']]
			node_list[parent_index]['children'].append(child_index)
		return root



if __name__ == "__main__":

	csv_file = open("models/results3.csv")
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