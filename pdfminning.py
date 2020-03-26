import PyPDF2
def clean_item(item):
    item = item.replace('\n', ' ')
    item = item.strip()
    return item


def perctenage(item):
    item=item.split(' ')
    A="A."+item[1]
    B="B."+item[2]
    C="C."+item[3]
    D="D."+item[4]
    perctenage=A+" "+" "+B+" "+" "+C+" "+D
    return perctenage



pdffileobj=open('relatorio1.pdf','rb')
pdfreader=PyPDF2.PdfFileReader(pdffileobj)
x=pdfreader.numPages
print(x)
#58 -642

for i in range(622,643):
    print(i)
    pageobj=pdfreader.getPage(i)
    text=pageobj.extractText()
    #print(text)
    text=clean_item(text)
    #print(text)
    data=text.split('ENDEREÇO')
    #print(data[0])
    Title=(data[0])
    #print(Title)
    data=data[1].split("TELEFONE")
    #print(data[0])
    Enderco=data[0]
    #print(Enderco)
    data=data[1].split("WEBSITE")
    #print(data[0])
    Telephone=data[0]
    #print(Telephone)
    data=data[1].split("DATA DE INAUGURAÇÃO")
    Website=data[0]
    #print(Website)
    data=data[1].split("TIPO DE SHOPPING")
    DataDe=data[0]
    #print(DataDe)
    #print(data[0])
    data=data[1].split("ABL")
    TipoDe=data[0]
    #print(data[0])
    #print(TipoDe)
    data=data[1].split("ÁREA CONSTRUÍDA")
    #print(data[0])
    Abl=data[0]
    #print(Abl)
    data=data[1].split("ÁREA DO TERRENO")
    Area=data[0]
    #print(Area)
    #print(data[0])
    data=data[1].split("ADMINISTRAÇÃO")
    AreaDo=data[0]
    #print(AreaDo)
    #print(data[0])
    data=data[1].split("TOTAL DE LOJAS")
    print(data[0])
    try:
        if data[0] != ' ':
            Admin=data[0]
            print("ADMIN1")
            print(Admin)
    except:
        ()
    data=data[1].split("LOJAS ÂNCORA")
    Total=data[0]
    #print(data[0])
    #print(Total)
    data=data[1].split("MEGALOJAS")
    Lojas=data[0]
    #print(data[0])
    #print(Lojas)
    data=data[1].split("SATÉLITES")
    #print(data[0])
    Mega=data[0]
    #print(Mega)
    data=data[1].split("CONVENIÊNCIA E SERVIÇOS")
    Satelittes=data[0]
    #print(Satelittes)
    #print(data[0])
    data=data[1].split("ALIMENTAÇÃO")
    Conveniencia=data[0]
    #print(Conveniencia)
    #print(data[1])
    data=data[1].split("ENTRETENIMENTO")
    Alimen=data[0]
    #print(data[0])
    #print(Alimen)
    data=data[1].split("CINEMA")
    Entret=data[0]
    #print(Entret)
    #print(data[0])
    data=data[1].split("ESTACIONAMENTO")
    Cinema=data[0]
    #print(data[0])
    #print(Cinema)
    data=data[1].split("PISOS DO SHOPPING")
    Estacion=data[0]
    #print(Estacion)
    #print(data[0])
    data=data[1].split("PERFIL DOS FREQUENTADORES")
    Pisos=data[0].replace('B C D A','')
    #print(Pisos)
    #print(data[1])
    data=data[1].split("B")
    #print(data[0])
    Perfil=perctenage(data[0])
    #print(Perfil)
    #data=data[1].split("VOLTAR")
    #print(data[0])
    data=data[1].replace('C D A', '')
    #print(data)
    data=data.split('VOLTAR')
    try:
        if Admin ==' ':
            Admin=data[0]
    except:
        ()
    List=(Title,Enderco,Telephone,Website,DataDe,TipoDe,Abl,Area,AreaDo,Admin,Total,Lojas,Mega,Satelittes,Conveniencia,Alimen,Perfil,Entret,Cinema,Estacion,Pisos)
    with open('PdfData.csv','a+', newline='') as csv_file:
                writer = csv.writer(csv_file,lineterminator='\n')
                writer.writerows([List],)

