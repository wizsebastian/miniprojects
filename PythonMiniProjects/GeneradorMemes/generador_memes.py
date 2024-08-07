from PIL import Image, ImageDraw, ImageFont


def generar_meme(imagen_path, texto_superior, texto_inferior):
    # Abrir la imagen
    imagen = Image.open(imagen_path)

    # Crear un objeto para dibujar sobre la imagen
    dibujo = ImageDraw.Draw(imagen)

    # Definir la fuente y el tamaño
    fuente = ImageFont.truetype("arial.ttf", 40)

    # Obtener las dimensiones de la imagen
    ancho, alto = imagen.size

    # Añadir texto superior
    dibujo.text(
        (ancho / 2, 50), texto_superior, font=fuente, fill=(255, 255, 255), anchor="mm"
    )

    # Añadir texto inferior
    dibujo.text(
        (ancho / 2, alto - 50),
        texto_inferior,
        font=fuente,
        fill=(255, 255, 255),
        anchor="mm",
    )

    # Guardar la imagen resultante
    imagen.save("meme_generado.jpg")
    print("Meme generado como 'meme_generado.jpg'")


def main():
    imagen_path = input("Ingresa la ruta de la imagen: ")
    texto_superior = input("Ingresa el texto superior: ")
    texto_inferior = input("Ingresa el texto inferior: ")

    generar_meme(imagen_path, texto_superior, texto_inferior)


if __name__ == "__main__":
    main()
