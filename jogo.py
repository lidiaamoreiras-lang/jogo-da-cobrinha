import random
import asyncio
from pyscript import Element, window

canvas = Element("snakeGame").element
ctx = canvas.getContext("2d")
tamanho = 20
cobra = [[100, 100], [80, 100], [60, 100]]
direcao = [tamanho, 0]
comida = [200, 200]
score = 0
jogo_rodando = True

def desenhar_quadrado(x, y, cor):
    ctx.fillStyle = cor
    ctx.fillRect(x, y, tamanho, tamanho)

async def game_loop():
    global direcao, comida, score, jogo_rodando
    while jogo_rodando:
        nova_cabeca = [cobra[0][0] + direcao[0], cobra[0][1] + direcao[1]]
        
        if (nova_cabeca[0] < 0 or nova_cabeca[0] >= 400 or 
            nova_cabeca[1] < 0 or nova_cabeca[1] >= 400 or 
            nova_cabeca in cobra):
            jogo_rodando = False
            window.alert(f"Fim de Jogo! Pontos: {score}")
            break

        cobra.insert(0, nova_cabeca)
        if nova_cabeca == comida:
            score += 10
            Element("score").element.innerText = str(score)
            comida = [random.randrange(0, 380, 20), random.randrange(0, 380, 20)]
        else:
            cobra.pop()

        ctx.clearRect(0, 0, 400, 400)
        desenhar_quadrado(comida[0], comida[1], "red")
        for parte in cobra:
            desenhar_quadrado(parte[0], parte[1], "#2ecc71")
        await asyncio.sleep(0.15)

def mudar_direcao_btn(dir_nome):
    global direcao
    if dir_nome == "up" and direcao != [0, tamanho]: direcao = [0, -tamanho]
    elif dir_nome == "down" and direcao != [0, -tamanho]: direcao = [0, tamanho]
    elif dir_nome == "left" and direcao != [tamanho, 0]: direcao = [-tamanho, 0]
    elif dir_nome == "right" and direcao != [-tamanho, 0]: direcao = [tamanho, 0]

def reiniciar():
    window.location.reload()

asyncio.ensure_future(game_loop())