# import numpy as np
# import matplotlib.pyplot as plt
#
# # Yurak shakli uchun matematik tenglama
# t = np.linspace(0, 2 * np.pi, 1000)
# x = 16 * np.sin(t) ** 3
# y = 13 * np.cos(t) - 5 * np.cos(2 * t) - 2 * np.cos(3 * t) - np.cos(4 * t)
#
# # Grafikni chizish
# plt.figure(figsize=(6, 6))
# plt.plot(x, y, color='red')
# plt.fill(x, y, 'red', alpha=0.3)
# plt.title('Yurak shakli')
# plt.axis('equal')
# plt.show()


# import numpy as np
# import matplotlib.pyplot as plt
# from mpl_toolkits.mplot3d import Axes3D
#
# # Yurakning matematik tenglamasi
# theta = np.linspace(0, 2 * np.pi, 100)
# z = np.linspace(-1.5, 1.5, 100)
# theta, z = np.meshgrid(theta, z)
# r = 1 - np.sin(theta)
#
# x = r * np.sin(theta)
# y = r * np.cos(theta)
#
# # 3D grafikni yaratish
# fig = plt.figure(figsize=(8, 8))
# ax = fig.add_subplot(111, projection='3d')
#
# # Yurak shaklini chizish
# ax.plot_surface(x, y, z, color='red', alpha=0.7, rstride=5, cstride=5)
#
# # Yurak shakli atrofida nur taralishini taqlid qilish (gradient)
# ax.scatter(x, y, z, color='orange', s=0.1, alpha=0.2)
#
# # Aylanma harakatni taqlid qilish uchun o'q burchagini o'rnatish
# ax.view_init(elev=30, azim=120)
#
# plt.title('3D Yurak shakli')
# plt.show()

#
# import numpy as np
# import matplotlib.pyplot as plt
# from mpl_toolkits.mplot3d import Axes3D
# from matplotlib.animation import FuncAnimation
#
# # Yurakning matematik tenglamasi
# theta = np.linspace(0, 2 * np.pi, 100)
# z = np.linspace(-1.5, 1.5, 100)
# theta, z = np.meshgrid(theta, z)
# r = 1 - np.sin(theta)
#
# x = r * np.sin(theta)
# y = r * np.cos(theta)
#
# # Grafikni yaratish
# fig = plt.figure(figsize=(8, 8))
# ax = fig.add_subplot(111, projection='3d')
#
# # Yurak shaklini chizish
# surface = ax.plot_surface(x, y, z, color='red', alpha=0.8, rstride=5, cstride=5)
#
# # Yurak shakli atrofida nur taralishini taqlid qilish (gradient)
# ax.scatter(x, y, z, color='orange', s=0.1, alpha=0.2)
#
# # Animatsiyani yaratish funksiyasi
# def rotate(angle):
#     ax.view_init(elev=30, azim=angle)
#
# # Animatsiya sozlamalari
# ani = FuncAnimation(fig, rotate, frames=np.arange(0, 360, 2), interval=50)
#
# # Grafikni ko'rsatish
# plt.title('3D Yurak shakli')
# plt.show()

import pygame
import math

# Pygame-ni boshlash
pygame.init()

# O'yin ekranining o'lchamlari
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Pygame 3D Cube')

# Ranglar
white = (255, 255, 255)
black = (0, 0, 0)

# Kubning koordinatalari
cube_vertices = [
    (-1, -1, -1),
    (1, -1, -1),
    (1, 1, -1),
    (-1, 1, -1),
    (-1, -1, 1),
    (1, -1, 1),
    (1, 1, 1),
    (-1, 1, 1)
]

# Kub qirralari (tugunlar orasidagi chiziqlar)
cube_edges = [
    (0, 1), (1, 2), (2, 3), (3, 0),
    (4, 5), (5, 6), (6, 7), (7, 4),
    (0, 4), (1, 5), (2, 6), (3, 7)
]

def rotate_vertex(vertex, angle_x, angle_y, angle_z):
    x, y, z = vertex
    # X o'qi atrofida aylantirish
    x1 = x
    y1 = y * math.cos(angle_x) - z * math.sin(angle_x)
    z1 = y * math.sin(angle_x) + z * math.cos(angle_x)

    # Y o'qi atrofida aylantirish
    x2 = x1 * math.cos(angle_y) + z1 * math.sin(angle_y)
    y2 = y1
    z2 = -x1 * math.sin(angle_y) + z1 * math.cos(angle_y)

    # Z o'qi atrofida aylantirish
    x3 = x2 * math.cos(angle_z) - y2 * math.sin(angle_z)
    y3 = x2 * math.sin(angle_z) + y2 * math.cos(angle_z)
    z3 = z2

    return x3, y3, z3

def project(vertex):
    # 3D koordinatalarni 2D ekran koordinatalariga aylantirish
    scale = 200
    x, y, z = vertex
    distance = 5
    factor = scale / (z + distance)
    x_proj = int(width / 2 + x * factor)
    y_proj = int(height / 2 - y * factor)
    return x_proj, y_proj

def main():
    angle_x, angle_y, angle_z = 0, 0, 0
    clock = pygame.time.Clock()
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill(black)

        # Har bir tugunni aylantirish
        rotated_vertices = [rotate_vertex(v, angle_x, angle_y, angle_z) for v in cube_vertices]
        # Har bir tugunni ekranga proyeksiya qilish
        projected_vertices = [project(v) for v in rotated_vertices]

        # Kubning qirralarini chizish
        for edge in cube_edges:
            pygame.draw.line(screen, white, projected_vertices[edge[0]], projected_vertices[edge[1]], 1)

        pygame.display.flip()
        clock.tick(60)

        # Burchaklarni yangilash (kubni aylantirish)
        angle_x += 0.01
        angle_y += 0.01
        angle_z += 0.01

    pygame.quit()

if __name__ == "__main__":
    main()
