from Grafo import Grafo

N_SIMILAR = 3

def abrir_archivo(grafo):
	with open ("youtube.txt","r") as archivo:
		for linea in archivo:
			if linea[0] != "#":
				v1,v2 = linea.rstrip("\n").split("\t")
				if not grafo.existe_verice(v1):
					grafo.agregar_vertice(v1)
				if not grafo.existe_verice(v2):
					grafo.agregar_vertice(v2)
				if not grafo.son_adyacentes(v1,v2):
					agregar_arista(v1,v2)
			if linea[0] == "#":
				datos = linea.rstrip("\n")
				if len(datos) == 5:
					cant_vertices = datos[2]
					cant_aristas = datos[4]
		return 

def simlares(id, n_sim):
	similar = {}
	for i in range (0, N_SIMILAR):

	
def random_walks(grafo, vertice, n):
	actual = vertice
	caminos = {}
	vertices_visitados = []
	for i in range(0, n):
		ady = grafo.adyacentes(actual)
		if not actual in caminos:
			caminos[actual] = 1
		if actual in caminos:
			caminos[actual] += 1
		actual = random.choice(ady)
		vertices_visitados.append(actual)
	return caminos
