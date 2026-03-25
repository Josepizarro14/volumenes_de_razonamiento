import numpy as np
import plotly.graph_objects as go

# ==========================================
# CREAR OBJETO SÓLIDO
# ==========================================

X, Y, Z = np.mgrid[0.5:4.5:40j, 0.5:4.5:40j, 0.5:4.5:40j]


nucleos = [
    (1.5, 1.5, 1.8, 0.6),  
    (2.5, 2.2, 2.0, 0.7),  
    (3.2, 3.0, 3.0, 1.0)   
]


volumen = np.zeros_like(X)
for cx, cy, cz, r in nucleos:
    volumen += np.exp(-((X - cx)**2 + (Y - cy)**2 + (Z - cz)**2) / (r**2))


papa = go.Isosurface(
    x=X.flatten(),
    y=Y.flatten(),
    z=Z.flatten(),
    value=volumen.flatten(),
    isomin=0.45, 
    isomax=0.45,
    surface_count=1, 
    colorscale='YlOrBr', 
    showscale=False,
    caps=dict(x_show=False, y_show=False, z_show=False), 
    name='Cuerpo Principal'
)

# ==========================================
# CREAR "CUERPOS DE POCO VOLUMEN"
# ==========================================
phi = np.linspace(0, np.pi, 20)
theta = np.linspace(0, 2 * np.pi, 20)
phi, theta = np.meshgrid(phi, theta)

x_sph = 0.2 * np.sin(phi) * np.cos(theta)
y_sph = 0.2 * np.sin(phi) * np.sin(theta)
z_sph = 0.2 * np.cos(phi)

esfera_azul = go.Surface(x=1.5+x_sph, y=3.5+y_sph, z=1.5+z_sph, colorscale='Blues', showscale=False)
esfera_verde = go.Surface(x=3.8+x_sph, y=1.2+y_sph, z=3.8+z_sph, colorscale='Greens', showscale=False)

fig = go.Figure(data=[papa, esfera_azul, esfera_verde])

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
   
            title=dict(
                text='<br><b>Posicionamiento docente</b>',
                font=dict(size=14, color="black")
            ),
            ticktext=['Describe', 'Relaciona', 'Percibe<br>oportunidades', 'Configura<br>actuaciones'],
            **estilo_ejes
        ),
        yaxis=dict(
            title=dict(
                text='<br><b>Amplitud del razonamiento</b>',
                font=dict(size=14, color="black")
            ),
            ticktext=['Ontológico', 'Epistemológico', 'Metodológico', 'Lógico'],
            **estilo_ejes
        ),
        zaxis=dict(
            title=dict(
                text='<b>Profundidad del razonamiento</b><br>',
                font=dict(size=14, color="black")
            ),
            ticktext=['Emergente', 'Configurado', 'Situado', 'Expandido'],
            **estilo_ejes
        ),
        aspectmode='cube'
    ),
    
    scene_camera=dict(
        projection=dict(type="orthographic")
    ),
    title="Volúmenes de Razonamiento",
    margin=dict(l=0, r=0, b=0, t=40)
)

fig.show()