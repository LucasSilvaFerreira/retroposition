__author__ = 'Lucas'
arquivo = open('Human74.txt','r').readlines()
#arquivo=arquivo.split('/n')
#print type(arquivo)
for linha in arquivo[1:]:
    if len(linha)>0:
        #print linha
        linha_cortada=linha.split()

        #print linha_cortada[8]
        for ensembl_linha in open('ensembl.txt','r').read().split('\n'):
            if len(ensembl_linha)>0:
                ensbl_cortado=ensembl_linha.split()
                if linha_cortada[8]==ensbl_cortado[12]:
                    linha_cortada[5] ="\t".join([ensbl_cortado[2],ensbl_cortado[4],ensbl_cortado[5]])
                    print "chr"+linha_cortada[1]+'\t'+linha_cortada[2]+'\t'+linha_cortada[3]+"\t"+linha_cortada[0]+'\t'+linha_cortada[5]+'\t'+linha_cortada[8]
