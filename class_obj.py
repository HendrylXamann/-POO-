class Moto: #Declaração da classe
    #Func obrigatória para criação da classe(CONSTRUTOR):
    def __init__(self, marcaMoto, modeloMoto, anofab, veloMaxima,corMoto):  
        #Atributos(caracteristicas):
        self.marca = marcaMoto
        self.modelo = modeloMoto
        self.anofab = anofab
        self.veloMaxima = veloMaxima
        self.cor = corMoto
        """
        Este self, assim como o this no Java, faz referência ao objeto atual;
        Os valores são transferidos aos atributos usando o self/this;
        Sem o self, não daria p/ diferenciar entre os atributos da classe e as variáveis locais do método;
        """
    #Método:    
    def embreagem(self,marchaa):
        marcha = int(marchaa)
        if marcha == 2:
            print("Velocidade máxima recomendada até 40 KM/H")  
        elif marcha == 3:  
            print("Velocidade máxima recomendada até 60 KM/H") 
        elif marcha == 4:  
            print("Velocidade máxima recomendada até 75 KM/H")
        elif marcha == 5:  
            print("Velocidade máxima recomendada até 130 KM/H")
        elif marcha >= 6:  
            print("Velocidade máxima recomendada é 'não morra por por favor' ")           
        pass
  
"""
As variáveis abaixo são instâncias da classe, objetos no caso;
Como a classe tem os parametros(atributos), sempre eu chamar ela tenho que passar os valores dos atributos;
""" 
#Objeto 1 da classe: 
minhaMoto = Moto("Honda", "XRE", "2024", "180", "Preta")
#Objeto 2 da classe: 
minhaOutraMoto = Moto("BMW", "GS", "2025", "260", "Branca")
"""
Tanto o Objeto 1 como o 2 tem os mesmos atributos e acesso ao mesmo método, por isso usamos POO pois com uma mesma classe poss fazer
distintas coisas com N valores
""" 

#Pegar apenas um atributo especifico (variavel,ponto,atributo que quero)
print(minhaOutraMoto.anofab)
#Pegar apenas um método (variavel,ponto,nome da função/método de dentro da classe e parenteses -- parametro caso tenha)
minhaOutraMoto.embreagem("8")

