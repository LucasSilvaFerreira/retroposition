__author__ = 'Lucas'
from multiprocesso_classe import thread_processador
class pseudogenes(thread_processador):
    print 'start'
    #arquivo= open('linc_enseml.txt','r')
    def funcao(self,inicio,fim):
        import re
        self.array_temporario=[]
        self.dados_pgenes=open('arquivo_coluna_coord.bed','r').read()

        for linha in self.arquivo_array[int(inicio):int(fim)]:
            #print linha
            linha_c=linha.split()
            for pgenes in self.dados_pgenes.split("\n"):
                if len(pgenes)>0:
                    if "chr"+linha_c[1]== pgenes.split()[0]:
                        if int(linha_c[2])>int(pgenes.split()[1]) and int(linha_c[2])<int(pgenes.split()[2]):
                            print pgenes.split()[1],'>',linha_c[2],'<',pgenes.split()[2]
                            print linha

            #self.array_temporario.append(saida_join)
        #self.set_saida(self.rray_temporario)

pseudogenes('',4,'saida_pseudo_result.txt')