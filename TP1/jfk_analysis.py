def numLigneFichier(file):
    fichier=open(file,"r")
    numLigne=0
    while(fichier.readline()):  
        numLigne+=1
    fichier.close()
    return numLigne

"permet de separer les donnees de chaque ligne ; ou ;""; ou ""; dans un tableau"
def fonction(ligne):
    while(1):
        H=ligne.split(';"',1)
     
        check=H[0].split('";')
        if len(check)==2:
        
            tabFinal=[]
            tabFinal.append(check[0])
            tabFinal+=check[1].split(';')

            
        else:
            tabFinal=H[0].split(';')
  
            
        if len(H)==2:
            tab=H[1].split('";',1)
            tabFinal+=tab

        if len(H)==1:
            break
        
        tab1=tabFinal[-1]
        tabFinal.pop()
        tabFinal+=fonction(tab1)
        break
    
    return(tabFinal)


def question1(file):
    ligneTotal=numLigneFichier(file)
    resultat=True

    fichier=open(file,"r")
    numField=len(fichier.readline().split(";"))
    compteur=1
    
    while(1):
        ligne=fonction(fichier.readline())
        
        compteur+=1

        if(len(ligne)!=numField):
            resultat=False
            print("la ligne",compteur,"ne contient pas le meme nombre de champs")
        
        if(compteur==ligneTotal):
            break
        
    if(resultat==True):
        print("Toutes les lignes ont le meme nombre de champs")
    
    fichier.close()

    return(resultat)
    


def question2Moyenne(file):
    ligneTotal=numLigneFichier(file)

    fichier=open(file,"r")

    fichier.readline()
    numLigne=1
    
    sommePageRealeased=0
 
    while(numLigne<ligneTotal):
        ligne=fonction(fichier.readline())
        numLigne+=1
       
        "Page Realeased "
        t=ligne[-1].split("\n")
        if(t[0]!=''):
            sommePageRealeased+=(int(t[0]))
                  
    fichier.close()

    moyennePage = sommePageRealeased/(ligneTotal-1)
     
    return(moyennePage)
            




def question2MinMax(file,docName):
    ligneTotal=numLigneFichier(file)

    fichier=open(file,"r")

    fichier.readline()
    numLigne=1

    tabPageDocTotal=[]
    position=NameDocumentLignePosition(file,docName)
    
    while(numLigne<ligneTotal):
        ligne=fonction(fichier.readline())
        numLigne+=1

        tab=[]

        "Page Realeased "
        t=ligne[-1].split("\n")
        if(t[0]!=''):
            tab.append(t[0])
        else:
            tab.append(0)
            
        "Num Page "   
        if(ligne[11]!=''):
            tab.append(ligne[11])
        else:
            tab.append(0)

        tabPageDocTotal.append(tab)        
   
    fichier.close()

    return(min(tabPageDocTotal[position])),max(tabPageDocTotal[position])



def NameDocumentLignePosition(file,docName):
    ligneTotal=numLigneFichier(file)

    fichier=open(file,"r")

    fichier.readline()
    numLigne=1

    compteur=0

    while(1):
        ligne=fonction(fichier.readline())
        if(ligne[0]==docName):            
            break
        compteur+=1
    return(compteur)


def question2MissingPage(file):
    ligneTotal=numLigneFichier(file)

    fichier=open(file,"r")

    fichier.readline()
    numLigne=1

    missingPage=0
    
    while(numLigne<ligneTotal):
        ligne=fonction(fichier.readline())
        numLigne+=1

        "Num Page " 
        if(ligne[11]!=''):
            missingPage+=1
    
    fichier.close()
  
    return(missingPage)
            
def question2ZeroPage(file):
    ligneTotal=numLigneFichier(file)

    fichier=open(file,"r")

    fichier.readline()
    numLigne=1

    while(numLigne<ligneTotal):
        ligne=fonction(fichier.readline())
        numLigne+=1

        "Num Page " 
        if(ligne[11]!=''):
             if(int(ligne[11])==0):
                print(ligne,"contient 0 page car doc manquant dans les archives")
    
    fichier.close()
  
question1("jfkrelease-2017-dce65d0ec70a54d5744de17d280f3ad2.csv")

print("la moyenne de toutes les pages par document est ",question2Moyenne("jfkrelease-2017-dce65d0ec70a54d5744de17d280f3ad2.csv"))

print("le (min,max) de page du doc ","DOCID-32121528.pdf est ",question2MinMax("jfkrelease-2017-dce65d0ec70a54d5744de17d280f3ad2.csv","DOCID-32121528.pdf"))

print("il y a ",question2MissingPage("jfkrelease-2017-dce65d0ec70a54d5744de17d280f3ad2.csv")," pages manquantes")

question2ZeroPage("jfkrelease-2017-dce65d0ec70a54d5744de17d280f3ad2.csv")
