
###################################################
 """coloration algorithm"""                      ##
                          """Reda EL MARHOUCH""" ##
###################################################



def create_mat_dict(N):
    M = [ [0 for j in range(N)] for i in range(N) ]
    D={}
    print('votre graphe comporte',N,' sommets nommés', Names1)
    for i in range(len(Names1)):
        x=input( 'entrer les adjacents de  '+Names1[i]+':  ')
        L=list(x.upper())
        D[Names1[i]]=L
        for elt in L:
            M[i][ord(elt)-65]=1
    return M,D
#################################################
def visualize_mat(M):
    N=len(M)
    print("\t\t /",'   '*(N-1),' \\')
    for i in range(N):
        print("\t\t|  ",end='')
        for j in range (N):
            print (M[i][j],end='  ')
        print("|")
    print("\t\t \\",'   '*(N-1),' /',end='')
    return
#######################
S=[]           #global
#################################################
def sort_sommets(M):
    L=[]
    for k in range( len(M) ):
        d=0
        for l in range(len(M)):
            if M[k][l] > 0:
                d = d + 1
        L+=[(k,d),]
    for p in range(len (M)):
        for q in range (len(M)-1):
            if L[q+1][1]>L[q][1]: L[q+1],L[q]=L[q],L[q+1]

    global S
    for c in L:
        if Names1[c[0]] not in S : S.append(Names1[c[0]])
    return L
###############################################
def adj(M,k):
    adj_ind=[]
    for i in range(len(M)):
        if M[ord(k.upper())-65][i]>0:
            adj_ind += [chr(i+65),]
    return adj_ind
###############################################
def color(M):
    coloration=[]
    chrome=0
    while S!=[]:
        colored=[]
        V=[]
        chrome+=1
        somm=S.pop(0)
        colored.append(somm)
        V=adj(M,somm)
        for e in S:
            if e not in V :
                S.remove(e)
                colored.append(e)
                V+=adj(M,e)
        coloration+=[colored,]
    return coloration
###############################################
def showcolors(M):
    M=color(M)
    ch=len(M)
    for e in M:
        print ('\n\t-les sommets ',e,' sont :',colors.pop(0))
    print('\n\tle nombre chromatique est <=',ch)
###############################################
def find_cliques(P=[], R=[], X=[]):
        if len(R) == 0 and len(X) == 0:
                print ('Cest une clique:', P)
                global p
                if len(P)>p:
                    p=len(P)
        else:
                for sommet in R[:]:
                        newP = P[:]
                        newP.append(sommet)
                        newR = [n for n in R if n in D[sommet]]
                        newX = [n for n in X if n in D[sommet]]
                        find_cliques(newP, newR, newX)
                        R.remove(sommet)
                        X.append(sommet)
        return

###############################################
N=int(input("Entrez le nombre de sommets N= "))
colors=["Red","Blue","Green","Yellow","Pink","Orange","Purple","Cyan","White","Black"]
Names0='ABCDEFGHIJKLMNOPQRSTUVWXYZ' 
Names1=list(Names0[:N])
F=create_mat_dict(N)
M=F[0]
D=F[1]
print("\n\nvotre matrice:")
visualize_mat(M)
print("\n\nsommets tries:")
sort= sort_sommets(M)
print('\t\t',S)
print(showcolors(M))
p=0
find_cliques(R=Names1)
print('\n\tle nombre chromatique est >= ',p)
