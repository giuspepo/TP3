import random

class Grafo:
	"""implementacion de clase grafo"""
	def __init__(self, bool_dirigido):
		"""..."""
		self.grafo = {}
		self.dirigido = bool_dirigido 
		self.cant_aristas = 0
		self.cant_vertices = 0
		
	def vertices(self):
		return self.grafo.keys()

	def es_dirigido(self):
		return self.dirigido

	def adyacentes(self, vertice):
		"""devuelve una lista de adyacentes del vertice pasado por parametro,
		si no tiene ninguno devuelve lista vacia"""
		if not self.existe_vertice(vertice):
			return None
		return self.grafo[vertice]

	def vertice_ady_aleatorio(self,vertice):
		"""elige un vertice aleatorio para iniciar el recorrido"""
		if not self.existe_vertice(vertice):
			return random.choice(self.grafo.keys())
		return random.choice(self.adyacentes(vertice))

	def agregar_vertice(self,vertice):
		"""si no existe vertice lo agrega"""
		if self.existe_vertice(vertice):
			raise ValueError("El vertice ya existe")
		if not vertice in self.grafo:
			self.grafo[vertice] = []
			self.cant_vertices += 1

	def agregar_arista(self, origen, vecino):
		"""agrega arista entre dos vertices del grafo, si alguno no existe en el grafico, lo crea"""
		if not self.existe_vertice(origen) or not self.existe_vertice(vecino):
			raise ValueError("No existe alguno de los vertices")
		if self.son_adyacentes(origen, vecino):
			raise ValueError ("Ya estan conectados")
		#if origen in self.grafo: no have falta. Ya preguntamos eso hace un rato.
		self.grafo[origen].append(vecino)

		if not self.dirigido:
			self.grafo[vecino].append(origen)
		self.cant_aristas += 1

	def quitar_vertice(self, vertice):
		"""quita un vertice del grafo y elimina sus adyacencias del resto de los vertices"""
		if not self.existe_vertice(vertice):
			raise ValueError("El vertice no existe")
		for clave in self.grafo.keys():
			if vertice in self.grafo[clave]:
				self.grafo[clave].remove(vertice)
				self.cant_aristas -= 1
		#elimina las aristas que conecta el vertice
		#Si el grafo no es dirigido se asume que ya se borraron cuando se recorrio anteriormente
		if not self.dirigido:
			self.cant_aristas -= len(self.grafo[vertice])
		del self.grafo[vertice]
		self.cant_vertices -= 1

	def quitar_arista(self, origen, vecino):
		"""Elimina la union entre dos vertices"""
		if not self.son_adyacentes(origen, vecino):
			raise ValueError("No estan conectados")
		self.grafo[origen].remove(vecino)
		if not self.dirigido:
			self.grafo[vecino].remove(origen)
		self.cant_aristas -= 1

	def son_adyacentes(self, vertice, vecino):
		"""devuelve true si algunos de los parametros se encuentra en la lista de
		adyacencias del otro, independientemente de que sea dirigido o no"""
		if not self.existe_vertice(vertice) or not self.existe_vertice(vecino):
			raise ValueError("No existe alguno de los vertices")
		return (vecino in self.grafo[vertice]) or (vertice in self.grafo[vecino])

	def existe_vertice(self, vertice):
		"""comprueba si un vertice se encuentra en el grafo"""
		return (self.grafo).has_key(vertice)

	def cantidad_vertices(self):
		"""devuelve la cantidad de vertices en el grafo"""
		return self.cant_vertices

	def cantidad_aristas(self):
		"""devuelve la cantidad de aristas del grafo"""
		return self.cant_aristas
	
	def __iter__(self):
		"""crea un iterador del grafo"""
		return iter(self.grafo)
