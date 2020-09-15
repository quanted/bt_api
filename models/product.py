class Product:
	"""
	A product/node in the tree.
	"""
	def __init__(self, id, name, data, children):
		self.id = id  # NOTE: python uses "id" as well
		self.name = name or "<img class='blank_node' src='/static_qed/cts/images/loader_node.gif' />"
		self.data = ProductData(
			smiles=data['smiles'],
			routes=data.get('routes'),
			accumulation=data.get('accumulation'),
			production=data.get('production'),
			globalAccumulation=data.get('globalAccumulation'),
			likelihood=data.get('likelihood')
		).__dict__
		self.children = children

class ProductData:
	"""
	A product/node's data.
	"""
	def __init__(self, smiles, routes, accumulation, production, globalAccumulation, likelihood):
		self.smiles = smiles
		self.routes = routes or ""
		self.accumulation = accumulation or "N/A"
		self.production = production or "N/A"
		self.globalAccumulation = globalAccumulation or "N/A"
		self.likelihood = likelihood or "N/A"
