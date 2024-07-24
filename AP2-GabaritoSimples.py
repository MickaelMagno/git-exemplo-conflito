# -*- coding: utf-8 -*-
"""

Em uma pequena cidade chamada Águas de São Pedro, foi construído um Haras que mantem cavalos de raça com tratamento especializado. Como eles estavam com algumas necessidades de gestão sistêmicas, resolveram fazer uma seleção para contratação de um programador. Como parte do processo seletivo, os candidatos foram desafiados a entregar em 1:50minutos uma solução simples (programa estruturado) com os seguintes requisitos e funcionalidades.

Cenário e Funcionalidades:
•	Eventualmente o veterinário faz visitas ao haras para medicar os animais, e duas medicações dependem do peso do animal: vacina e vermífugo, o programa deve calcular e mostrar a dosagem dos animais para essas duas situações, a partir da pesagem do animal. 
o	A dosagem da vacina é medida em ml injetável, e para cada 100kg deve ser administrado 5 ml da vacina. Ou seja: animais com menos de 100Kg  5 ml, animais acima de 100 até 200kg  10 ml, a partir de 1000kg a dose era única de 100ml.
o	A dosagem do vermífugo é ministrada via pulverização lombar e para cada 200kg do animal deve ser administrado 1litro da solução. Acima de 1200 kg são necessários 20 litros da solução.
o	Não há necessidade de medicar animais com menos de 1 ano ou com mais de 25 anos, pois para esses animais o tratamento é diferenciado e não faz parte do escopo desse programa.
o	A pesagem do animal é feita individualmente quando da visita do veterinário.
•	Além de fornecer a dosagem da medicação o programa deve fazer o cadastro de animal, sem essa informação não seria possível calcular as dosagens. 

Requisitos Obrigatórios:
•	0,5 Criar estruturas de dados necessárias para o programa, e obrigatoriamente um dicionário de listas para cada animal contendo:
o	Nome, raça, idade do animal
•	0,5 O programa deve estar todo modularizado, sem uso de nenhuma variável global.
•	1,0 Não deve existir passagem de parâmetros envolvendo uma lista inteira, somente o(s) valor(es) necessários.
•	(0,5) O programa deve conter três sub-rotinas, além da main(), sendo um procedimento e duas funções todas com passagem de parâmetros. A liberdade criativa fica a seu critério, desde que respeitados os requisitos.
•	(0,5) Ao final, fazer o desenho da modularização resultante do seu programa, especificando a comunicação existente entre as sub-rotinas, mostrada através da representação de funções, procedimentos, parâmetros e retornos.

@author: angela.reis
"""

# PARTE I - Resolver as duas funcionalidades: cadastrar animal e calcular medicação

def Calcular_dose_vacina(P):
   
    if P <= 100: 
        ml= 5
    elif P<=200:
        ml=10
    elif P<=300:
        ml=15
    elif P<=400:
        ml=20
    elif P<=500:
        ml=25
    elif P<=600:
        ml=30
    elif P<=700:
        ml=35
    elif P<=800:
        ml=40
    elif P<=900:
        ml=45
    elif P<=1000:
        ml=50
    else:
        ml=100
    Mostrar_dosagens_medicamento(ml,1)    
        
        
def Calcular_dose_vermifugo(P):
    l = 1
    if P<=200:
        l*=1
    elif P<=400:
        l*=2
    elif P<=600:
        l*=3
    elif P<=800:
        l*=4
    elif P<=1000:
        l*=5
    elif P<=1200:
        l*=6
    else:
        l=20
    Mostrar_dosagens_medicamento(l,0)    
    
        
def Mostrar_dosagens_medicamento(dose,tipomed):
    if tipomed ==1:
        print(" a dosagem da vacina é:", dose, "ml")
    else:
        print(" a pulverização do vermífugo deve ser com:", dose, "litros")
    

def Pedir_Opcao():
    OP = int(input(" \n 1- Cadastrar Animal \n 2- Medicar Animal \n 3- Sair \n==> ")) 
    return OP

    
def Pedir_Dados_Animal():
     N=input("Nome do Animal: ")
     R=input("Raça do Animal: ")
     I=int(input("Idade do Animal:"))
     return N, R, I    
    
def main():
    Cavalo={}
    while True:
        R=Pedir_Opcao()
        #cadastra o animal
        if R == 1:
            nome, raca, idade = Pedir_Dados_Animal()
            Cavalo[nome]=[raca,idade]
            
        # Calcula a dosagem daS medicaçoes  
        elif R == 2:
             
             print(" o calculo não pode ser aplicado a animais com menos de 1 ano e mais de 25 anos")
             Peso = int(input("\n Informe o peso do animal: "))
             Calcular_dose_vacina(Peso)
             Calcular_dose_vermifugo(Peso)
        
        #sai do menu, termina a execução
        elif R == 3:
            break
        else: 
            print("digite uma opção valida")
    print(Cavalo)    
         
    
    
main()
