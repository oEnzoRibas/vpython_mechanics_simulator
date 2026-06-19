from vpython import *
#Web VPython 3.2

# 1. Configuração da Cena 3D
scene = canvas(title="<b>Simulador Cinemático: Posição, Velocidade e Aceleração</b>", width=600, height=400, center=vector(40, 20, 0), background=color.gray(0.9))
scene.camera.pos = vector(40, 20, 100)

# 2. Configuração dos Gráficos Educativos
g_yt = graph(title="Posição Vertical vs Tempo (y x t)", xtitle="Tempo t (s)", ytitle="Altura y (m)", width=400, height=200, align="left")
curva_yt = gcurve(graph=g_yt, color=color.blue, width=2)

g_vt = graph(title="Componentes da Velocidade vs Tempo (v x t)", xtitle="Tempo t (s)", ytitle="Velocidade (m/s)", width=400, height=200, align="right")
curva_vx = gcurve(graph=g_vt, color=color.cyan, width=2, label="vx (horizontal)")
curva_vy = gcurve(graph=g_vt, color=color.orange, width=2, label="vy (vertical)")

g_at = graph(title="Aceleração Vertical vs Tempo (ay x t)", xtitle="Tempo t (s)", ytitle="Aceleração (m/s²)", width=400, height=150, align="left")
curva_ay = gcurve(graph=g_at, color=color.red, width=2)

# 3. Parâmetros Físicos Constantes
g_val = -10
g = vector(0, g_val, 0)
dt = 0.01

# 4. Objetos do Cenário e Eixos Cartesianos
chao = box(pos=vector(40, -1, 0), size=vector(200, 2, 20), color=vector(0.2, 0.6, 0.2))
projetil = sphere(pos=vector(0, 0, 0), radius=1.5, color=color.purple, make_trail=True, trail_type="points", interval=10)

# Vetores visuais acoplados ao projétil (Seta Ciano = Velocidade, Seta Vermelha = Aceleração)
seta_v = arrow(pos=projetil.pos, axis=vector(0,0,0), color=color.cyan, shaftwidth=0.4, headwidth=1.2)
seta_a = arrow(pos=projetil.pos, axis=vector(0,0,0), color=color.red, shaftwidth=0.4, headwidth=1.2)

# Eixos fixos no cenário mundial
eixo_x = arrow(pos=vector(0,0,0), axis=vector(150,0,0), color=color.black, shaftwidth=0.2)
eixo_y = arrow(pos=vector(0,0,0), axis=vector(0,95,0), color=color.black, shaftwidth=0.2)
label(pos=vector(155, 0, 0), text="x (m)", box=False, line=False, color=color.black)
label(pos=vector(0, 100, 0), text="y (m)", box=False, line=False, color=color.black)

for x_tick in range(20, 141, 20):
    box(pos=vector(x_tick, 0, 0), size=vector(0.2, 2, 2), color=color.black)
    label(pos=vector(x_tick, -3, 0), text=str(x_tick), box=False, line=False, color=color.black, height=10)

for y_tick in range(20, 91, 20):
    box(pos=vector(0, y_tick, 0), size=vector(2, 0.2, 2), color=color.black)
    label(pos=vector(-4, y_tick, 0), text=str(y_tick), box=False, line=False, color=color.black, height=10)

# 5. Variáveis de Controle da Simulação
lancando = False
v = vector(0,0,0)
t = 0

# === INTERFACE DE USUÁRIO (UI) ===
scene.append_to_caption('\n<b>Parâmetros de Lançamento</b>\n')

# Slider para Velocidade Inicial (v0)
def atualiza_v0(s):
    texto_v0.text = f" {s.value} m/s"

scene.append_to_caption('Velocidade Inicial (v₀): ')
sl_v0 = slider(min=10, max=50, value=40, step=1, length=200, bind=atualiza_v0)
texto_v0 = wtext(text=" 40 m/s")
scene.append_to_caption('\n')

# Slider para Ângulo (theta)
def atualiza_angulo(s):
    texto_angulo.text = f" {s.value} graus"

scene.append_to_caption('Ângulo de Lançamento (θ): ')
sl_angulo = slider(min=0, max=90, value=90, step=1, length=200, bind=atualiza_angulo)
texto_angulo = wtext(text=" 90 graus")
scene.append_to_caption('\n\n')

# Botão de Disparo executável
def disparar(b):
    global lancando, t, v
    if lancando: return
    
    # Reset completo das curvas e do rastro
    projetil.pos = vector(0, 0, 0)
    projetil.clear_trail()
    curva_yt.data = []
    curva_vx.data = []
    curva_vy.data = []
    curva_ay.data = []
    t = 0
    
    # Coleta de dados dos sliders refletores de deslocamento
    v0_mag = sl_v0.value
    theta = radians(sl_angulo.value)
    
    # Montagem vetorial da velocidade linear inicial
    v = vector(v0_mag * cos(theta), v0_mag * sin(theta), 0)
    lancando = True

button(text="<b>▶ Iniciar Lançamento</b>", bind=disparar, color=color.white, background=color.blue)
scene.append_to_caption('\n\n<i>Dica didática: Teste o ângulo em 90 graus. No topo do voo, a seta azul (velocidade) desaparece por um instante, mas a seta vermelha (aceleração) continua idêntica apontando para baixo!</i>')

# 6. Loop de Atualização em Tempo Real
while True:
    rate(100)
    
    if lancando:
        # Integração via Método de Euler
        v = v + g * dt
        projetil.pos = projetil.pos + v * dt
        t = t + dt
        
        # Posicionamento e dimensionamento dos vetores acoplados (multiplicadores para escala visual)
        seta_v.pos = projetil.pos
        seta_v.axis = v * 0.4
        
        seta_a.pos = projetil.pos
        seta_a.axis = g * 1.5
        
        # Plotagem síncrona nos eixos de tempo
        curva_yt.plot(t, projetil.pos.y)
        curva_vx.plot(t, v.x)
        curva_vy.plot(t, v.y)
        curva_ay.plot(t, g_val)
        
        # Condição de impacto com a superfície plano-horizontal
        if projetil.pos.y < 0:
            lancando = False
            projetil.pos.y = 0
            seta_v.axis = vector(0,0,0)
            seta_a.axis = vector(0,0,0)