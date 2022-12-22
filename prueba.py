import base64

with open('imagen1.jpg', 'rb') as imagen:
  contenido = imagen.read()
  
imagen_codificada = base64.b64encode(contenido)

print(type(imagen_codificada))

imagen_decode = base64.b64decode(imagen_codificada)

with open('imagen_decode.jpg', 'wb') as imagen_decodificado:
  imagen_decodificado.write(imagen_decode)
