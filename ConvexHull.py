from scipy.spatial import ConvexHull, convex_hull_plot_2d # бібліотекв для відображення опуклої оболонки
import matplotlib.pyplot as plt
import matplotlib.pyplot as mpl
import numpy as np


# альтернатиний варіант перетворення txt в array
# def create_points():
#    with open( FILENAME, 'r') as f:
#        data = f.read()
#    res: list[int] = [int(i) for i in data.split()]
#    return res


plt.axis ( [0, 960, 0, 540] ) # розміри вікна
points = np.loadtxt ( "DS2.txt", dtype=int ) # за допоммогою numpy, перетворення txt в Array
print("точки датасета:\n", points) # За умовою, Відображає точки вихідного датасету
hull = ConvexHull(points) # заповнюємо оболонку точками

# Будуємо графік
plt.plot ( points[:, 1], points[:, 0], 'o')
for simplex in hull.simplices:
    plt.plot ( points[simplex, 1], points[simplex, 0], 'k-', color='blue')
    # Відображає опуклу оболонку за допомогою відрізків синього кольору;

plt.plot(points[hull.vertices, 1], points[hull.vertices, 0], 'r--', lw=2, color='blue') # будуємо лінії
plt.plot(points[hull.vertices[0], 1], points[hull.vertices[0], 0], 'ro', color='blue') # будуємо лінії
plt.show() # Відображення картинки
