import csv
import time

# def subtree(node, relationships):
# 	return {
# 		v: subtree(v, relationships) 
# 		for v in [x[0] for x in relationships if x[1] == node]
# 	}


# (child, parent) pairs where -1 means no parent    
# smiles_tree = [
# 	("CC(=O)O", "CC(=O)OC1=C(C=CC=C1)C(O)=O"),
# 	("C1(=C(C=CC=C1)C(O)=O)O", "CC(=O)OC1=C(C=CC=C1)C(O)=O"),
# 	("C1(=C(C=CC=C1)C(=O)NCC(O)=O)O", "C1(=C(C=CC=C1)C(O)=O)O"),
# 	("C1(=C(C=CC=C1)C(O)=O)OC2OC(C(O)C(O)C2O)C(O)=O", "C1(=C(C=CC=C1)C(O)=O)O"),
# 	("C1(=C(C=CC=C1)C(OC2OC(C(O)C(O)C2O)C(O)=O)=O)O", "C1(=C(C=CC=C1)C(O)=O)O"),
# 	("C1(=C(C=CC=C1)C(=O)NCC(O)=O)OC2OC(C(O)C(O)C2O)C(O)=O", "C1(=C(C=CC=C1)C(=O)NCC(O)=O)O"),
# 	# ("C1(=C(C=CC=C1)C(O)=O)O", "C1(=C(C=CC=C1)C(O)=O)OC2OC(C(O)C(O)C2O)C(O)=O"),
# 	# ("C1(OC(C(O)C(O)C1O)C(O)=O)O", "C1(=C(C=CC=C1)C(O)=O)OC2OC(C(O)C(O)C2O)C(O)=O"),
# 	# ("C1(=C(C=CC=C1)C(O)=O)O", "C1(=C(C=CC=C1)C(OC2OC(C(O)C(O)C2O)C(O)=O)=O)O"),
# 	# ("C1(OC(C(O)C(O)C1O)C(O)=O)O", "C1(=C(C=CC=C1)C(OC2OC(C(O)C(O)C2O)C(O)=O)=O)O"),
# 	# ("C1(=C(C=CC=C1)C(O)=O)O", "C1(=C(C=CC=C1)C(OC2OC(C(O)C(O)C2O)C(O)=O)=O)O"),
# 	# ("C1(OC(C(O)C(O)C1O)C(O)=O)O", "C1(=C(C=CC=C1)C(OC2OC(C(O)C(O)C2O)C(O)=O)=O)O")
# ]


# # actual results example:
# smiles_dict = [
# 	{'child': 1, 'parent': -1, 'data': {}},
# 	{'child': 2, 'parent': -1, 'data': {}},
# 	{'child': 3, 'parent': 2, 'data': {}},
# 	{'child': 4, 'parent': 2, 'data': {}},
# 	{'child': 5, 'parent': 2, 'data': {}},
# 	{'child': 6, 'parent': 3, 'data': {}},
# 	{'child': 2, 'parent': 4, 'data': {}},
# 	{'child': 7, 'parent': 4, 'data': {}},
# 	{'child': 2, 'parent': 5, 'data': {}},
# 	{'child': 7,'parent':  5, 'data': {}},
# 	{'child': 2,'parent':  5, 'data': {}},
# 	{'child': 7,'parent':  5, 'data': {}}
# ]

smiles_dict = [
	{'id': 1, 'parent': -1, 'data': {}},
	{'id': 2, 'parent': -1, 'data': {}},
	{'id': 3, 'parent': 2, 'data': {}},
	{'id': 4, 'parent': 2, 'data': {}},
	{'id': 5, 'parent': 2, 'data': {}},
	{'id': 6, 'parent': 3, 'data': {}},
	{'id': 2, 'parent': 4, 'data': {}},
	{'id': 7, 'parent': 4, 'data': {}},
	{'id': 2, 'parent': 5, 'data': {}},
	{'id': 7,'parent':  5, 'data': {}},
	{'id': 2,'parent':  5, 'data': {}},
	{'id': 7,'parent':  5, 'data': {}}
]

smiles_dict_2 = [
  {
    'id': 'BTM00001',
    'parent': '',
    'data': {
      'smiles': 'CC(=O)O',
      'routes': 'Hydrolysis of carboxylic acid ester'
    }
  },
  {
    'id': 'BTM00002',
    'parent': '',
    'data': {
      'smiles': 'C1(=C(C=CC=C1)C(O)=O)O',
      'routes': 'Hydrolysis of carboxylic acid ester'
    }
  },
  {
    'id': 'BTM00003',
    'parent': 'BTM00002',
    'data': {
      'smiles': 'C1(=C(C=CC=C1)C(=O)NCC(O)=O)O',
      'routes': 'Glycination of aromatic acid'
    }
  },
  {
    'id': 'BTM00004',
    'parent': 'BTM00002',
    'data': {
      'smiles': 'C1(=C(C=CC=C1)C(O)=O)OC2OC(C(O)C(O)C2O)C(O)=O',
      'routes': 'Aromatic OH-glucuronidation'
    }
  },
  {
    'id': 'BTM00005',
    'parent': 'BTM00002',
    'data': {
      'smiles': 'C1(=C(C=CC=C1)C(OC2OC(C(O)C(O)C2O)C(O)=O)=O)O',
      'routes': 'O-Glucuronidation of aromatic acid'
    }
  },
  {
    'id': 'BTM00006',
    'parent': 'BTM00003',
    'data': {
      'smiles': 'C1(=C(C=CC=C1)C(=O)NCC(O)=O)OC2OC(C(O)C(O)C2O)C(O)=O',
      'routes': 'Aromatic OH-glucuronidation'
    }
  },
  {
    'id': 'BTM00002',
    'parent': 'BTM00004',
    'data': {
      'smiles': 'C1(=C(C=CC=C1)C(O)=O)O',
      'routes': 'Glycoside hydrolysis'
    }
  },
  {
    'id': 'BTM00007',
    'parent': 'BTM00004',
    'data': {
      'smiles': 'C1(OC(C(O)C(O)C1O)C(O)=O)O',
      'routes': 'Glycoside hydrolysis'
    }
  },
  {
    'id': 'BTM00002',
    'parent': 'BTM00005',
    'data': {
      'smiles': 'C1(=C(C=CC=C1)C(O)=O)O',
      'routes': 'Glycoside hydrolysis'
    }
  },
  {
    'id': 'BTM00007',
    'parent': 'BTM00005',
    'data': {
      'smiles': 'C1(OC(C(O)C(O)C1O)C(O)=O)O',
      'routes': 'Glycoside hydrolysis'
    }
  },
  {
    'id': 'BTM00002',
    'parent': 'BTM00005',
    'data': {
      'smiles': 'C1(=C(C=CC=C1)C(O)=O)O',
      'routes': 'Hydrolysis of carboxylic acid ester'
    }
  },
  {
    'id': 'BTM00007',
    'parent': 'BTM00005',
    'data': {
      'smiles': 'C1(OC(C(O)C(O)C1O)C(O)=O)O',
      'routes': 'Hydrolysis of carboxylic acid ester'
    }
  }
]


def traverse(orig_tree, new_tree):
	trav_index = 0
	for node in orig_tree:
		if node['parent'] == new_tree['id']:
			new_tree['children'].append({
				'id': node['id'],
				'children': [],
				'data': node['data']
			})
			trav_index += 1
		else:
			new_parent = node['parent']
			child_index = 0
			for _node in new_tree['children']:
				if _node['id'] == new_parent:
					new_tree['children'][child_index] = {
						'id': _node['id'],
						'children': [],
						'data': node['data']
					}
					new_tree_2 = new_tree['children'][child_index]
					orig_tree_2 = orig_tree[trav_index:]
					traverse(orig_tree_2, new_tree_2)
				child_index += 1
	return new_tree



if __name__ == '__main__':
	start = time.time()
	tree = {'id': -1, 'children': [], 'data': {}}
	# print(traverse(smiles_dict, tree))
	print(traverse(smiles_dict_2, tree))
	print("Time: {}".format(time.time() - start))