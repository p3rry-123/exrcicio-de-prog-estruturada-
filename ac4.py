"""
Programação Estruturada
2024.1
08/03/2024
AC4
"""

def ler_nome():
    """Retorna o nome do aluno inserido pelo usuário."""
    return input("Informe o seu nome: ")

def ler_notas():
    """Lê as notas de AP1, AP2, AS e AC do aluno, e retorna essas notas."""
    ap1=float (input("informe sua Ap1: "))
    ap2=float (input("informe sua Ap2: "))
    asub=float (input("informe sua Asub:"))
    ac=float (input ("informe sua AC:"))
    return ap1,ap2,asub,ac

def analisar_subst(ap1, ap2, asub):
    if asub > ap1 and ap1 > ap2:
        ap2 = asub
    elif asub > ap2 and ap2> ap1:
        ap1 = asub
    elif asub > ap1 and ap1 == ap2:
        ap1 = asub 
    return ap1 , ap2 

    """
    Retorna as duas notas a serem usadas no cálculo.
    A AS deve substituir a AP1 ou AP2 se for maior que elas.
    """

def calcular_media(ap1, ap2, asub, ac):
    """Calcula e retorna a média final do aluno."""
    prova1, prova2 = analisar_subst(ap1, ap2, asub)
    return (prova1 + prova2) * 0.4 + ac * 0.2

def aluno_foi_aprovado(media):
    """Retorna True se a média foi suficiente para aprovação do aluno."""
    return media >= 7

def notas_sao_validas(ap1, ap2, asub, ac):
    return 0 <= ap1 <= 10 and 0 <=ap2 <= 10 and 0 <= asub <= 10 and 0 <= ac <= 10 
    """Retorna True se todas as notas estão entre 0 e 10, inclusive."""

def main():
    nome = ler_nome()
    if nome:
        ap1, ap2, asub, ac = ler_notas()
        if notas_sao_validas(ap1, ap2, asub, ac):
            media = calcular_media(ap1, ap2, asub, ac)
            if aluno_foi_aprovado(media):
                print("Aluno foi aprovado.", media)
            else:
                print("Aluno foi reprovado.")

main()