import numpy as np
import plotly.graph_objects as go

# ==========================================
# CREAR OBJETO SÓLIDO
# ==========================================
np.random.seed(42)
cantidad_puntos = 800 


radio_aleatorio = np.random.rand(cantidad_puntos) ** (1/3) 
phi = np.arccos(1 - 2 * np.random.rand(cantidad_puntos))
theta = 2 * np.pi * np.random.rand(cantidad_puntos)


x = radio_aleatorio * np.sin(phi) * np.cos(theta) * 0.7
y = radio_aleatorio * np.sin(phi) * np.sin(theta) * 0.7
z = radio_aleatorio * np.cos(phi) * 1.2

factor_grosor = 1.0 + 0.25 * z
x *= factor_grosor
y *= factor_grosor
x -= 0.3 * (z**2) 


X = 2.5 + x
Y = 2.5 + y
Z = 2.5 + z


papa_reticulada = go.Scatter3d(
    x=X, y=Y, z=Z,
    mode='markers+lines',
    marker=dict(
        size=4, 
        color='purple', 
        opacity=0.9
    ),
    line=dict(
        color='rgba(0, 0, 0, 0.25)', 
        width=1
        
    ),
    name='Red Conceptual (Papa)'
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

fig = go.Figure(data=[papa_reticulada, esfera_azul, esfera_verde])

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