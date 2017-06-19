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
		if self.dirigido == False:
			for elem in ady:
				if elem in self.grafo:
					(self.grafo[elem]).append(nuevo)

	def agregar_vertice(self,vertice)
		if not vertice in self.grafo:
			self.grafo[vertice] = []

	def agregar_arista(self, origen, vecino):
		"""agrega arista entre dos vertices del grafo"""
		if origen in self.grafo:
			self.grafo[origen].append(vecino)

		if not origen in self.grafo:
			self.grafo[origen] = [vecino]

		if vecino in self.grafo:
			self.grafo[vecino].append(origen)

		if not vecino in self.grafo:
			self.grafo[vecino] = [origen]

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
	
	def random_walks(self, largo, inicial):		
	recorrido = []	
	v = inicial	
	if not inicial v = random.choice(self.vertice)	
	recorrido.append(v)	
		
	for x in range(0, largo):	
		v = random.choice(self.grafo[v])
		recorrido.append(v)
		
	return recorrido	
	
	def label_propagation (self):		
	label = {}	
	#inicializamos	
	i = 0	
	for v in self.vertice:	
		label[v] = i
		i += 1
	#Aqui va una condicion. algo desde que un vertice y sus vecinos tengan todos el mismo label, o un maximo de iteraciones.	
	while not condicion:	
		for v in self.vertice:
			if self.grafo[v] == [] continue		
					
			freq = {}		
			for w in self.grafo[v]:		
				if not label[w] in freq:	
					freq[label[w]] = 0
				freq[label[w]] += 1	
			#Devuelve el label con la mayor frecuencia		
			lmax = max(freq.iterkeys(), key=(lamda key: freq[key]))		
			label[v] = lmax
			
		#Las comunidades son aquellos grupos de vertices que tienen el mismo label	
	
