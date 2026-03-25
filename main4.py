import numpy as np
import plotly.graph_objects as go

# ==========================================
# CREAR OBJETO SÓLIDO (LA PAPA ORGÁNICA)
# ==========================================
resolucion = 40 # Subimos un poco la resolución para que los bultos se vean suaves
phi = np.linspace(0, np.pi, resolucion)
theta = np.linspace(0, 2 * np.pi, resolucion)
phi, theta = np.meshgrid(phi, theta)

# 1. Base ovalada y ligeramente aplastada en un lado
x = np.sin(phi) * np.cos(theta) * 0.8
y = np.sin(phi) * np.sin(theta) * 0.6
z = np.cos(phi) * 1.1

# 2. Generamos "bultos" orgánicos usando ondas matemáticas suaves
bultos = 1.0 + 0.12 * np.sin(3 * phi) * np.cos(2 * theta) + 0.08 * np.sin(theta)
x *= bultos
y *= bultos
z *= bultos

# 3. Mantenemos el hundimiento característico (curvatura)
x -= 0.25 * (z**2) 

X = 2.5 + x
Y = 2.5 + y
Z = 2.5 + z

papa_solida = go.Surface(
    x=X, y=Y, z=Z, 
    colorscale='YlOrBr', 
    showscale=False, 
    name='Cuerpo Principal'
)

# ==========================================
# CREAR LA "MALLA" O RETÍCULA (Sin recortes)
# ==========================================
x_lines, y_lines, z_lines = [], [], []

# Aumentamos la escala para separar la malla de la piel sólida y evitar el recorte visual
escala = 1.035 
X_malla = 2.5 + (X - 2.5) * escala
Y_malla = 2.5 + (Y - 2.5) * escala
Z_malla = 2.5 + (Z - 2.5) * escala

for i in range(resolucion):
    x_lines.extend(X_malla[i, :].tolist() + [None])
    y_lines.extend(Y_malla[i, :].tolist() + [None])
    z_lines.extend(Z_malla[i, :].tolist() + [None])

for j in range(resolucion):
    x_lines.extend(X_malla[:, j].tolist() + [None])
    y_lines.extend(Y_malla[:, j].tolist() + [None])
    z_lines.extend(Z_malla[:, j].tolist() + [None])

malla = go.Scatter3d(
    x=x_lines, y=y_lines, z=z_lines, 
    mode='lines', 
    line=dict(color='rgba(0, 0, 0, 0.7)', width=2.5), 
    showlegend=False,
    hoverinfo='skip'
)

# ==========================================
# CREAR "CUERPOS DE POCO VOLUMEN"
# ==========================================
phi_sph = np.linspace(0, np.pi, 20)
theta_sph = np.linspace(0, 2 * np.pi, 20)
phi_sph, theta_sph = np.meshgrid(phi_sph, theta_sph)

x_sph = 0.2 * np.sin(phi_sph) * np.cos(theta_sph)
y_sph = 0.2 * np.sin(phi_sph) * np.sin(theta_sph)
z_sph = 0.2 * np.cos(phi_sph)

esfera_azul = go.Surface(x=1.5+x_sph, y=3.5+y_sph, z=1.5+z_sph, colorscale='Blues', showscale=False)
esfera_verde = go.Surface(x=3.8+x_sph, y=1.2+y_sph, z=3.8+z_sph, colorscale='Greens', showscale=False)

fig = go.Figure(data=[papa_solida, malla, esfera_azul, esfera_verde])

# ==========================================
# CONFIGURAR EL CUBO (Cámara y Textos)
# ==========================================
estilo_ejes = dict(
    tickvals=[1, 2, 3, 4],
    range=[0.5, 4.5],
    showbackground=True,
    backgroundcolor="rgb(230, 230, 230)",
    gridcolor="white",
    showline=True,
    linewidth=2,
    linecolor="black",
    tickfont=dict(size=11, color="rgb(80, 80, 80)")
)

fig.update_layout(
    scene=dict(
        xaxis=dict(
            title=dict(text='<br><b>Posicionamiento docente</b>', font=dict(size=14, color="black")),
            ticktext=['Describe', 'Relaciona', 'Percibe<br>oportunidades', 'Configura<br>actuaciones'],
            **estilo_ejes
        ),
        yaxis=dict(
            title=dict(text='<br><b>Amplitud del razonamiento</b>', font=dict(size=14, color="black")),
            ticktext=['Ontológico', 'Epistemológico', 'Metodológico', 'Lógico'],
            **estilo_ejes
        ),
        zaxis=dict(
            title=dict(text='<b>Profundidad del razonamiento</b><br>', font=dict(size=14, color="black")),
            ticktext=['Emergente', 'Configurado', 'Situado', 'Expandido'],
            **estilo_ejes
        ),
        aspectmode='cube'
    ),
    scene_camera=dict(projection=dict(type="orthographic")),
    title="Volúmenes de Razonamiento",
    margin=dict(l=0, r=0, b=0, t=40)
)

fig.write_html("index.html")
fig.show()