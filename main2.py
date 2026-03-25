import matplotlib.pyplot as plt
import numpy as np

# ==========================================
# CREAR OBJETO SÓLIDO
# ==========================================
resolucion = 25
phi = np.linspace(0, np.pi, resolucion)
theta = np.linspace(0, 2 * np.pi, resolucion)
phi, theta = np.meshgrid(phi, theta)


x = np.sin(phi) * np.cos(theta) * 0.7
y = np.sin(phi) * np.sin(theta) * 0.7
z = np.cos(phi) * 1.2

factor_grosor = 1.0 + 0.25 * z
x *= factor_grosor
y *= factor_grosor
x -= 0.3 * (z**2) 

X = 2.5 + x
Y = 2.5 + y
Z = 2.5 + z

# ==========================================
# CREAR "CUERPOS DE POCO VOLUMEN"
# ==========================================
phi_sph = np.linspace(0, np.pi, 20)
theta_sph = np.linspace(0, 2 * np.pi, 20)
phi_sph, theta_sph = np.meshgrid(phi_sph, theta_sph)

x_sph = 0.2 * np.sin(phi_sph) * np.cos(theta_sph)
y_sph = 0.2 * np.sin(phi_sph) * np.sin(theta_sph)
z_sph = 0.2 * np.cos(phi_sph)

# ==========================================
# RENDERIZADO CON MATPLOTLIB
# ==========================================

fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')


ax.plot_surface(X, Y, Z, cmap='YlOrBr', edgecolor='black', linewidth=0.5, alpha=0.9, rstride=1, cstride=1)


ax.plot_surface(1.5+x_sph, 3.5+y_sph, 1.5+z_sph, color='dodgerblue', alpha=0.8)
ax.plot_surface(3.8+x_sph, 1.2+y_sph, 3.8+z_sph, color='forestgreen', alpha=0.8)

# ==========================================
# CONFIGURAR EL CUBO (Cámara y Textos)
# ==========================================

# Eje X
ax.set_xlim(0.5, 4.5)
ax.set_xticks([1, 2, 3, 4])
ax.set_xticklabels(['Describe', 'Relaciona', 'Percibe\noportunidades', 'Configura\nactuaciones'], fontsize=8)
ax.set_xlabel('\nPosicionamiento docente', fontweight='bold', labelpad=15)

# Eje Y
ax.set_ylim(0.5, 4.5)
ax.set_yticks([1, 2, 3, 4])
ax.set_yticklabels(['Ontológico', 'Epistemológico', 'Metodológico', 'Lógico'], fontsize=8)
ax.set_ylabel('\nAmplitud del razonamiento', fontweight='bold', labelpad=15)

# Eje Z
ax.set_zlim(0.5, 4.5)
ax.set_zticks([1, 2, 3, 4])
ax.set_zticklabels(['Emergente', 'Configurado', 'Situado', 'Expandido'], fontsize=8)
ax.set_zlabel('\nProfundidad del razonamiento', fontweight='bold', labelpad=15)

# Título y vista inicial
plt.title("Volúmenes de Razonamiento", fontweight='bold')

# Ajustar la cámara para que se vea más isométrico (ortográfico)
ax.view_init(elev=20, azim=45)

# Mostrar la ventana interactiva
plt.show()