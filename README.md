# 📚 geometry_engine_librairie

Ce répertoire contient la bibliothèque principale du moteur de géométrie.

## Description

`geometry_engine_librairie` regroupe les classes et outils mathématiques de base nécessaires à la manipulation d'objets géométriques simples en deux dimensions (ℝ²). Ces classes peuvent être trouvées dans le répertoire `Mathy`.

## Contenu actuel

- `Vector2` : représente un point ou un vecteur dans ℝ², avec des opérations élémentaires (addition, soustraction, produit scalaire, norme, etc.).
- `Vector3` : représente un vecteur dans ℝ³. Une classe fille qui hérite de cette classe peut être utilisée pour manipuler des coordonnées homogènes dans ℝ² (par exemple pour les transformations géométriques) : 
 - `HomogeneousVector3` : génère un vecteur en coordonnées homogènes à partir des coordonnées (x, y) d'un vecteur dans ℝ².
- `Matrix2x2` : représente une matrice 2×2, utilisée pour les transformations linéaires et les calculs de produits matriciels.
- `Matrix3x3` : classe de base pour représenter une matrice 3×3, utilisée pour les transformations homogènes. Trois classes filles héritent de cette classe : 
  - `TranslationMatrix3x3` : génère une matrice de translation à partir d’un vecteur de déplacement (x, y).
  - `RotationMatrix3x3` : génère une matrice de rotation pour un angle donné (en degrés).
  - `HomothetyMatrix3x3` : génère une matrice d’homothétie pour une mise à l’échelle selon un facteur donné.
- `Triangle` : représente un triangle défini par trois sommets, avec des méthodes pour calculer le périmètre, l'aire, calculer le cercle circonscrit et son rayon et vérifier si le triangle est rectangle.
- `Renderer` : classe dédiée à l'affichage graphique avec Pygame, permettant de dessiner des objets géométriques comme des points, des segments, des triangles, des cercles et du texte.

## Exemple d'utilisation

Le bloc ci-dessous montre un exemple d'utilisation de la bibliothèque. Il illustre des opérations vectorielles et matricielles, la manipulation d'un triangle, ainsi qu'une démonstration d'affichage avec Pygame.

```python
from Mathy import Vector2, Matrix2x2, Triangle
from Renderer import Renderer

# Vector operations
v1 = Vector2(3, 4)
v2 = Vector2(1, 2)

v3 = v1.add(v2)
print(f"v3 = v1 + v2 = {v3}")  # Vector2(4, 6)
print(f"Norm of v1: {v1.norm:.2f}")  # 5.00

# Matrix operations
m1 = Matrix2x2(1, 2, 3, 4)
m2 = Matrix2x2(0, 1, 1, 0)

m3 = m1.prod(m2)
print(f"m1 * m2 =\n{m3}")

# Solving a linear system Ax = b
b = Vector2(5, 6)
solution = m1.solve_system(b)
print(f"Solution of m1 * x = b is x = {solution}")

# Triangle example
triangle = Triangle((0, 0), (4, 0), (0, 3))
print(f"Triangle perimeter: {triangle.perimeter():.2f}")
print(f"Triangle area: {triangle.area():.2f}")
print(f"Is the triangle right-angled? {triangle.right_angled()}")

# Rendering a triangle with Pygame (minimal setup)
renderer = Renderer(400, 300, "Triangle Demo")
while renderer.running:
    renderer.handle_events()
    renderer.clear()
    renderer.draw_triangle(*triangle.get_vertices(), color=(0, 128, 255), width=2)
    renderer.draw_text("Triangle Demo", (10, 10), font_size=24)
    renderer.update()
    renderer.clock.tick(60)
renderer.quit()
