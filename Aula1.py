print "Programa de média\n"

nome = raw_input("Qual seus nome? ")
n1 = input("Digite a primeira nota: ")
n2 = input("Digite a segunda nota: ")
n3 = input("Digite a terceira nota: ")

media = (n1+n2+n3)/3

print "\nMedia = ", media

if(media>=6):
    print "\nAluno", nome, " APROVADO com média ", media
else:
    print "\nAluno", nome, " REPROVADO com média ", media
    