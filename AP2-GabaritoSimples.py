nova-feature
mickael
jonathan

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
