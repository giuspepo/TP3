import random

class Grafo:
	"""implementacion de clase grafo"""
	def __init__(self, bool_dirigido):
		"""..."""
		self.grafo = {}
		self.dirigido = bool_dirigido 

	def adyacentes(self, vertice):
		"""devuelve una lista de adyacentes del vertice pasado por parametro,
		si no tiene ninguno devuelve lista vacia"""
		return self.grafo[vertice]

	def inicio_aleatorio(self):
		"""elige un vertice aleatorio para iniciar el recorrido"""
		return random.choice(self.vertice)

	def agregar_vertice_con_ady(self, nuevo, ady):
		"""agrega un vertice nuevo al grafo, adyacentes es una lista"""
		self.grafo[nuevo] = ady
		for elem in ady:
			#crea el vertice si no existia
			if not elem in self.grafo:
				self.grafo[elem] = []
			#crea la arista de regreso si el grafo no es dirigido
			if self.dirigido == False:
				(self.grafo[elem]).append(nuevo)

	def agregar_vertice(self,vertice)
		if not vertice in self.grafo:
			self.grafo[vertice] = []

	def agregar_arista(self, origen, vecino):
		"""agrega arista entre dos vertices del grafo"""
		#Esto lo resume un poco. Si no estan los vertices los crea. 
		if not origen in self.grafo:
			self.grafo[origen] = []
		if not vecino in self.grafo:
			self.grafo[vecino] = []
		#luego crea la arista
		self.grafo[origen].append(vecino)

		#si la arista no es dirigida
		if self.dirigido == False:
			self.grafo[vecino].append(origen)

		

	def son_adyacentes(self, vertice, adyacente):
		"""devuelve true si algunos de los parametros se encuentra en la lista de
		adyacencias del otro, independientemente de que sea dirigido o no"""
		return (adyacente in self.grafo[vertice]) or (vertice in self.grafo[adyacente])

	def existe_vertice(self, vertice):
		"""comprueba si un vertice se encuentra en el grafo"""
		return (self.grafo).has_key(vertice)

	def cantidad_vertices(self):
		"""devuelve la cantidad de vertices en el grafo"""
		return len(self.grafo)

	def bfs(self, inicio, cant_corte = self.cantidad_vertices()):
		"""itera en anchura la cantidad de vertices, totales o las que se pasen por parametro"""
		visitados, pila = [], [inicio]
		cont = 0
		while pila and not cont == cant_corte:
			actual = pila.pop()
			for w in self.adyacentes(actual):
				if not w in visitados:
					visitados.append(w)
					pila.append(w)
					cont += 1
		return visitados

	def dfs(self, actual, visitados = [], cant_corte = self.cantidad_vertices(), cont = 1):
		"""itera en profundidad, """
		if cont == cant_cor:
			return visitados
		visitados.append(actual)
		for w in self.adyacentes(actual)
			self.dfs(w,visitados,cant_corte,cont +1)
