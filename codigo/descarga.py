from urllib2 import urlopen

direccionweb = "http://lorempixel.com"
dimensiontipo = ["abstract", "animals", "business", "cats", "city", "food", "nightlife", "fashion", "people", "nature", "sports", "technics", "transport"]
var = 'Hola'

anchopixeles = raw_input("Cual es el ancho en pixeles (px) __")
altopixeles = raw_input("Cual es el alto en pixeles (px) __")
eligetipo = raw_input("Elige un tipo | 0: Abstracto | 1: Animales | 2: Negocio | 3: Gatos | 4: Ciudad | 5: Comida | 6: Vida nocturna | 7: Moda | 8: Personas | 9: Naturaleza | 10: Deportes | 11: Tecnica | 12: Transporte __")

for imagen in range(5):
	url_req = "%s/%s/%s/%s/%d" % (direccionweb, anchopixeles, altopixeles, dimenciontipo[int(eligetipo)], imagen) 
	resultado = urlopen(url_req)
	lectura = resultado.read()
	f = open("imagen_%d.jpg" % imagen, "wb")
	f.write(lectura)
	f.close()