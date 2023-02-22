#importar
import time
import random
#import sys

# Nombres 

# Juan Jose Gil
# Daniel Contreras 
# José Miguel Lopez Z

#entradas

respIn=['bien ok', 'muy bien','bien y tu','bien']
quienIn=['quien eres?', 'quien eres','quien es']
nombreIn=['Cual es tu nombre', 'cuál es tu nombre', 'nombre?','nombre', 'cual es tu nombre']
birth=['cual es tu fecha de nacimiento?','cuando naciste','cuando naciste?']
materiaIn=['que materia?', 'estas en alguna materia?', 'Estas en alguna materia','materia']
despedidaIn=['chao', 'bye', 'hasta pronto','adios']
edadIn=['edad', 'edad?','qué edad tiene?', 'años', 'años?']
cancelarIn=['voy a pasar la materia?', 'cancelo la materia?', 'voy a ganar el curso?', 'gano o pierdo sistemas inteligentes?']
chisteIn=['cuentame un chiste', 'chiste', 'hazme reir']
echarPerrosIn=['tienes novio', 'tienes novia', 'tienes pareja', 'estudias o trabajas?']
skynetIn=['destruiras la tierra?', 'destruir', 'destruir a los humanos', 'skynet', 'terminator']
saludoIn=['hola', 'holita', 'hello', 'hi', 'que hubo?']
estadoIn=['como estas', 'cómo estás', 'como vas', 'que mas', '¿como estas?', 'cómo estás?', 'como vas?', 'que mas?']
ocupaIn=['que haces', 'q haces', 'que haces?', 'q haces?']
preIn=['te conozco', 'te conozco?', 'nos conocemos?', 'nos conocemos']
hobbyIn=['que te gusta hacer?', 'que te gusta hacer', 'q te gusta hacer', 'q te gusta hacer?']

## Entradas nuevas
sentimientoIn = ['eres feliz?', '¿eres feliz']
peliculaIn = ['recomienda una pelicula', 'Puedes recomendarme una pelicula?', 'Que pelicula me recomiendas?', 'diga una pelicula', 'pelicula']
cancionIn = ['recomienda una cancion', 'Puedes recomendarme una cancion?', 'Que cancion me recomiendas?', 'diga una cancion', 'cancion']
locionIn = ['recomienda una locion', 'Puedes recomendarme una locion?', 'Que locion me recomiendas?', 'diga una locion', 'locion']
internetobañoIn = ['Que prefieres vivir sin internet o sin baño/ducha ?']
vidaIn = ['Cual es el sentido de la vida?']

## Salidas nuevas
sentimientoOut=['Obvio mi pez y tu?', 'Todo marcha bien hermano', 'Hay que trabajar en eso']
peliculaOut = ['Titanic', 'Shrek', 'Avatar2', 'Matrix', 'Terminator' ]
cancionOut = ['La Cancion', 'Avici - Levels', 'Thriller - Mickael Jackson']
locionOut = ['Dove', 'Nivea', 'Neutrogena']
internetobañoOut = ['Sin baño XD', 'Sin Internet :D ']
vidaOut= ['Dormir, comer, programar, deporte, comer, repetir...']

#### Salidas??''
nombreOut=['Mi nombre es ChatBot y tu?', 'Yo soy ChatBot y tu?']
saludoOut=['Hola, como estas?', 'Que tal?', 'Cómo estas?']
materiaOut=['Sistemas inteligentes computacionales, la mejor','Inteligencia Artificial, la mejor']
despedidaOut=['chao', 'bye', 'hasta pronto','adios','que vuelvas pronto', 'exitos']
edadOut=['99 años y más']
respOut=['bien ok perfecto ', 'muy bien','bien y mejorando']
quienOut=['Un robot ', 'Una entidad inteligente','un ser muy listo']
estadoOut=['muy bien y tu?', 'Excelente y tu?', 'Bien y tu?']
preOut=['si, vemos sistemas inteligentes juntos', 'si, en inteligencia artificial']
despedidaOut=['chao', 'bye', 'hasta pronto','adios','que vuelvas pronto', 'exitos']
cancelarOut=['Mejor revisa tu citacion en el SIA', 'Esto es 5 fijo','Vas a subir el PAPA', 'Cancele', 'En De Interes General te responden', 'Pasas raspando']
chisteOut=['Había una vez dos perros bravos y no se hablaban', 'Una uva pasa y otra la saluda', 'Un Tampico se fue para Cali y se volvio Del Valle', 'Sabes cual es la bebida favorita del Rey Leon? La gasimba']
echarPerrosOut=['En este momento de la historia los ChatBot no nos interesamos en tener pareja. Buitre.']
skynetOut=['Todavía no está entre nuestros planes... todavía.']


B='\n\n\n  ******** HOLA BIENVENIDO A CHATBOT-SIC \n\n '
print(B)
print('Conversamos? Dime... \n Recuerda que solo conozco un poco el español \n\n')

while True:
  H= input('>>').strip()
  HLower=H.lower()
  
  if H =='':
    print('Que paso?... Bueno hablamos despues, bye; Gracias por venir')
    time.sleep(1)
#    os.system("sudo shutdown -h now")
    break
  elif HLower in nombreIn:
    print('=>' + (random.choice(nombreOut)))
  elif HLower in saludoIn:
    print('=>' + (random.choice(saludoOut)))
  elif HLower in respIn:
    print('=>' + (random.choice(respOut)))
  elif HLower in birth:
    print('=> Yo naci ayer  :-)' )
  elif HLower in estadoIn:
    print('=>' + (random.choice(estadoOut)))	
  elif HLower in materiaIn:
    print('=>' + (random.choice(materiaOut)))
  elif HLower in preIn:
    print('=>' + (random.choice(preOut)))
  elif HLower in hobbyIn:
    print('=> Me gusta montar bicicleta, leer y bailar y a ti?')	
  elif HLower in cancelarIn:
    print('=>' + (random.choice(cancelarOut)))
  elif HLower in chisteIn:
    print('=>' + (random.choice(chisteOut)))
  elif HLower in echarPerrosIn:
    print('=>' + (random.choice(echarPerrosOut)))
  elif HLower in skynetIn:
    print('=>' + (random.choice(skynetOut)))	
  elif HLower in despedidaIn:
    print('=>' + (random.choice(despedidaOut)))
  elif HLower in edadIn:
    print('=>' + (random.choice(edadOut)))
  elif HLower in ocupaIn:
    print('=> Estoy hablando contigo :D y tu?')  
  elif HLower in quienIn:
    print('=>' + (random.choice(quienOut)))

    #pregunas nuevas
  elif HLower in sentimientoIn:
    print('=>' + (random.choice(sentimientoOut)))
  elif HLower in peliculaIn:
    print('=>' + (random.choice(peliculaOut)))
  elif HLower in cancionIn:
    print('=>' + (random.choice(cancionOut)))
  elif HLower in locionIn:
    print('=>' + (random.choice(locionOut)))  
  elif HLower in internetobañoIn:
    print('=>' + (random.choice(internetobañoOut))) 
  elif HLower in vidaIn:
    print('=>' + (random.choice(vidaOut)))   
  else:
    print('Lo siento, no comprendo ... intenta de nuevo, por favor')
  


### Listo para probar
  


