import random, os, time, math, requests, json
os.system('color')

lista = sorted([
    "abacaxi", "abacate", "abelha",
    "bolacha", "baleia", "bote",
    "cachorro", "cadeira", "cenoura",
    "dente", "dinossauro", "dado",
    "elefante", "espelho", "estrela",
    "formiga", "faca", "fogo",
    "gato", "galinha", "girafa",
    "homem", "horta", "hiena",
    "igreja", "iguana", "ilha",
    "jaca", "janela", "jantar",
    "kiwi", "livro", "laranja",
    "macarrão", "macaco", "maçã",
    "navio", "noite", "ninho",
    "ovo", "olho", "orelha",
    "pássaro", "pera", "pente",
    "queijo", "quarto", "queda",
    "rato", "relógio", "rio",
    "sapo", "sino", "sala",
    "tênis", "tartaruga", "tijolo",
    "uva", "urso", "unicórnio",
    "vaca", "vento", "violão",
    "xícara", "xadrez", "xarope",
    "zebra", "zinco", "zangão",
])

def randomColor():
    print("\033["+str(random.randint(31,37))+"m", end="")

def letrasdif(palavraori, palavra):
    if len(palavra) != len(palavraori):
        return int(math.fabs(len(palavraori)-len(palavra)))
    lterr = 0
    for i in range(0,len(palavraori)-1):
        if str(palavraori[i]) != str(palavra[i]):
            lterr += 1
    return int(lterr)

seedN = random.randint(0,1000000)
while True:
    pontos = 0
    tempoinicial = time.time()
    vidas = 3
    while True:
        randoWord = random.randint(0,len(lista)-1)
        randomColor()
        print("")
        print('''
     _________                        .___   __                               
    /   _____/_____   ____   ____   __| _/ _/  |_ ___.__.______   ___________ 
    \_____  \\\\____ \\_/ __ \\_/ __ \\ / __ |  \\   __<   |  |\\____ \\_/ __ \\_  __ \\
    /        \\  |_> >  ___/\\  ___// /_/ |   |  |  \\___  ||  |_> >  ___/|  | \\/
    /_______  /   __/\\___  >\\____ >____ |   |__|  / ____||   __/ \\___  >__|   
            \\/|__|       \\/      \\/    \\/         \\/     |__|        \\/       
    ''')
        randomColor()
        print("Bem vindo ao speed typer!")
        randomColor()
        print("Digite as palavras para receber os pontos!")
        randomColor()
        print(str("#"*int(pontos-int(pontos/100)*100))+str("."*(100-pontos+int(pontos/100)*100)))
        randomColor()
        print("Vidas:","\033[31m<3 \033[0m"*vidas)
        randomColor()
        print("Pontos:",int(pontos))
        randomColor()
        print("")
        palavra = input(lista[randoWord] + "\033[0m \n").lower()

        url = "https://api.duckduckgo.com/?q="+lista[randoWord]+"&format=json&pretty=1&kl=pt-pt"
        try:
            response = requests.get(url)
            if response.status_code in [200,202]:
                data = response.json()
                if len(data.get("Abstract")) != 0:
                    for n, v in enumerate(data.get("Abstract").split(" ")):
                        lista.append(v)
                    lista = sorted(lista)
                    print("mais palavras foram adicionadas! agora tem:", len(lista), "palavras")
        except:
            pass

        if (palavra == lista[randoWord]) or letrasdif(lista[randoWord], palavra) == 0:
            pontos += len(lista[randoWord])
        elif letrasdif(lista[randoWord], palavra) == 2:
            pontos -= len(lista[randoWord])/2

        if letrasdif(lista[randoWord], palavra) > 2 or len(palavra) != len(lista[randoWord]):
            vidas -= 1
        
        if vidas <= 0:
            tempo2 = time.time()
            randomColor()
            print("Speed typer finalizado! veja seu progresso:")
            print("Pontos: " + str(pontos))
            print("Tempo: " + str(int((tempo2-tempoinicial)*10)/10))
            input("Click ENTER para tentar novamente.")
            os.system("cls")
            break
        os.system('cls')