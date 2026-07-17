import pygame

# Dimensiones de la ventana
ANCHO = 962
ALTO = 600

pygame.init()
pantalla = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Bandera de Noruega")

# Colores (RGB)
ROJO = (186, 12, 47)
BLANCO = (255, 255, 255)
AZUL = (0, 50, 91)

# Fondo rojo
pantalla.fill(ROJO)

# Proporciones de la bandera
unidad = ALTO / 16  # 16 unidades de alto

# Posiciones de la cruz
x_cruz = 6 * unidad
y_cruz = 6 * unidad

# Anchos de las franjas
blanco = 2 * unidad
azul = 1 * unidad

# Cruz blanca vertical
pygame.draw.rect(
    pantalla,
    BLANCO,
    (x_cruz - blanco / 2, 0, blanco, ALTO)
)

# Cruz blanca horizontal
pygame.draw.rect(
    pantalla,
    BLANCO,
    (0, y_cruz - blanco / 2, ANCHO, blanco)
)

# Cruz azul vertical
pygame.draw.rect(
    pantalla,
    AZUL,
    (x_cruz - azul / 2, 0, azul, ALTO)
)

# Cruz azul horizontal
pygame.draw.rect(
    pantalla,
    AZUL,
    (0, y_cruz - azul / 2, ANCHO, azul)
)

pygame.display.flip()

# Mantener la ventana abierta
ejecutando = True
while ejecutando:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            ejecutando = False

pygame.quit()