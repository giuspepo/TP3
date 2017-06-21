from Grafo import Grafo

N_SIMILAR = 3
LINEAS_COMENTARIOS = 4
LINEA_INFO = 2

def abrir_archivo(grafo):
	with open ("youtube.txt","r") as archivo:
		for i in range(LINEAS_COMENTARIOS +1):
			if i == LINEA_INFO:
				linea = archivo.readline()
				linea = linea.rstrip("\n").split(" ")
				cant_vertices = linea[2]
				cant_aristas = linea[4]

		for linea in archivo:
			v1,v2 = linea.rstrip("\n").split("\t")
			if not grafo.existe_verice(v1):
				grafo.agregar_vertice(v1)
			if not grafo.existe_verice(v2):
				grafo.agregar_vertice(v2)
			if not grafo.son_adyacentes(v1,v2):
				grafo.agregar_arista(v1,v2)


def random_walks(grafo, actual, cant, incluir_ady ):
	caminos = {}
	vertices_visitados = []
	if incluir_ady == False:
		actual = grafo.adyacentes(actual)
	for i in range(0, cant):
		ady = grafo.adyacentes(actual)
		if not actual in caminos:
			caminos[actual] = 1
		if actual in caminos:
			caminos[actual] += 1
		actual = random.choice(ady)
		vertices_visitados.append(actual)
	return caminos

def simlares(grafo, actual, cant):
	if not grafo.existe_verice(actual):
		print("No existe vertice")
		return
	similares = random_walks(grafo, cant, True)
	lista_mas_similares = #crear lista con mas similares

def recomendar(grafo, id, n_sim):

def caminos(grafo, origen, final):


def bfs(grafo, inicio, cant_corte = self.cantidad_vertices()):
	"""itera en anchura la cantidad de vertices, totales o las que se pasen por parametro"""
	visitados, pila = [], [inicio]
	cont = 0
	while pila and not cont == cant_corte:
		actual = pila.pop()
		for w in grafo.adyacentes(actual):
			if not w in visitados:
				visitados.append(w)
				pila.append(w)
				cont += 1
	return visitados

def dfs(grafo, actual, visitados = [], cant_corte = self.cantidad_vertices(), cont = 1):
	"""itera en profundidad, """
	if cont == cant_cor:
		return visitados
	visitados.append(actual)
	for w in grafo.adyacentes(actual)
		dfs(grafo, w,visitados,cant_corte,cont +1)
