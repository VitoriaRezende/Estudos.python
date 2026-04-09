nota1=float(input("Digite a primeira nota do aluno: "))
nota2=float(input("Digite a segunda nota do aluno: "))
media=(nota1+nota2)/2
if media<5.0:
    print("O aluno foi reprovado com a média {:.1f}".format(media))
elif media >=5.0 and media <=6.9:
    print("O aluno está de recuperação com a media {:.1f}".format(media))
else:
    print("O aluno foi aprovado com a media {:.1f}".format(media))
    