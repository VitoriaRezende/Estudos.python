import pygame #PYGAME É UMA BIBLIOTECA PARA CRIAÇÃO DE JOGOS, MAS PODE SER USADA PARA TOCAR MÚSICA TAMBÉM
pygame.init()
pygame.mixer.music.load('08ver.mp3')
pygame.mixer.music.play()
input()
pygame.event.wait() #espera o evento de fechar a janela para encerrar o programa
