import streamlit as st
from reportlab.lib.pagesizes import A4
from reportlab.lib.colors import HexColor
from reportlab.pdfgen import canvas
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import Paragraph
from reportlab.platypus import Frame
from reportlab.platypus import Spacer

#@st.cache_data
def criar_contrato(nome, nif, morada, passaporte, emitido, valido, funcao, salario, inicio, fim, residencia, emitido_r, valido_r, tele, pass_ou_res):

    p = canvas.Canvas("contrato.pdf", pagesize=A4)

    image = 'ferpitra.jpg'
    p.drawImage(image, 190, 720, width=200, height=65)

    p.setFillColor(HexColor("#000000"))
    p.setFont("Helvetica", 14)
    p.drawString(90, 690, "CONTRATO DE TRABALHO TEMPORÁRIO A TERMO CERTO")

    p.setFillColor(HexColor("#000000"))
    p.setFont("Helvetica", 11)
    p.drawString(72, 650, "Entre:")

    estilos = getSampleStyleSheet()
    estilo_centralizado = ParagraphStyle('EstiloCentralizado', parent=estilos['Normal'], alignment=4, fontSize=11, leading=15, fontName="Helvetica")

    texto1 = f'''<b>FERPITRA, UNIPESSOAL, LDA</b>, com o número único de matrícula e pessoa coletiva <b>517664836</b>, com sede na Rua 
    Cidade Moçamedes, 242, 1 º DRT. 1800-104 Olivais Sul, neste ato representados, pelo sócio- gerente, com poderes para 
    o ato, <b>Orvando Da Costa Fernandes</b>, adiante designada como Primeiro Contraente, na qualidade e com poderes para o ato 
    1º Outorgante (“<b>Empregador</b>”).'''

    texto2 = f'''<b>{nome},</b> Titular do passaporte N° <b>{passaporte}</b>, emitido aos {emitido}, válido 
    até {valido}, NIF: <b>{nif}</b>, Residente em <b>{morada},</b> 
    adiante designado por 2º Outorgante (“<b>Trabalhador</b>”).'''

    texto2_1 = f'''<b>{nome},</b> Titular da residência N° <b>{residencia}</b>, emitido aos {emitido_r}, válido 
    até {valido_r}, NIF: <b>{nif}</b>, Residente em <b>{morada},</b> 
    adiante designado por 2º Outorgante (“<b>Trabalhador</b>”).'''

    texto2_2 = f'''<b>{nome},</b> Titular da residência N° <b>{residencia}</b>, emitido aos {emitido_r}, válido 
    até {valido_r}, e do passaporte N° <b>{passaporte}</b>, emitido aos {emitido}, válido 
    até {valido}, NIF: <b>{nif}</b>, Residente em <b>{morada},</b> 
    adiante designado por 2º Outorgante (“<b>Trabalhador</b>”).'''

    texto3 = f'''É celebrado e reciprocamente aceite o presente contrato de trabalho temporário a termo certo 
    (“<b>Contrato de Trabalho Temporário</b>”), que se regerá pelas disposições legais aplicáveis bem como pelos termos seguintes:'''

    texto4 = f'''O presente Contrato de Trabalho Temporário é celebrado ao abrigo do disposto nos n°s 1 a 3 do art° 140° e 
    do art° 175° ambos da Lei 7/2009 de 12/02 e tem os seguintes fundamentos, conforme comunicado pelo Utilizador: O 
    presente Contrato de Trabalho Temporário é celebrado ao abrigo do disposto nos n°s 1 a 3 do art° 140° e do art° 
    175° ambos da Lei 7/2009 de comunicado em execução de contrato de prestação de serviço para <b>{funcao}.</b>'''

    texto5 = f'''<b>2.1 O Primeiro Contraente</b> admite ao seu serviço o (a) Contraente para que, sob a direção e orientação 
    desempenhe as funções inerentes á categoria profissional de <b>{funcao}</b> pela designação do <b>CAE 41200-R3</b>, 
    fazendo parte da atividade da empresa.'''

    texto6 = f'''<b>3.1 O (a) Segundo Contraente</b> obriga-se a prestar 8.0 horas de trabalho diário e 40.0 horas de trabalho 
    semanal, <b>40 horas semanal, 8 horas diária, com duas folgas rotativas a definir por escala semanal ou mensal organizada 
    pela empresa.</b>'''

    texto7 = f'''<b>3.2</b> A presente cláusula apenas aplica-se às situações em que o período normal de trabalho definido no 
    ponto 3.1 antecedente, for de <b>8 horas</b> diárias e <b>40 semanais</b>: o período normal do Trabalhador Temporário poderá ser 
    definido em termos médios, no período de referência legal, caso em que o período normal de trabalho diário pode 
    atingir às <b>10 horas</b> e o <b>trabalho semanal 50 horas</b>, não se incluindo neste o trabalho suplementar prestado por 
    motivo de força maior. Nas semanas em que a duração do trabalho for inferior a <b>40 horas</b>, a redução pode 
    consistir em <b>horas, meios-dias</b> ou <b>dias</b>.'''

    texto8 = f'''<b>4.1 O (a) Segundo Contraente</b> obriga-se a prestar sua atividade fora das instalações da <b>Papelaria 
    FERPITRA Unipessoal, LDA, localizada na Rua Cidade Moçamedes, 1800-104, Olivais Sul, adstrito a todas as deslocações 
    inerentes às suas funções, pois exercendo o teletrabalho a cargo da empresa.</b>'''

    texto8_1 = f'''<b>4.1 O (a) Segundo Contraente</b> obriga-se a prestar sua atividade dentro das instalações da <b>Papelaria 
    FERPITRA Unipessoal, LDA, localizada na Rua Cidade Moçamedes, 1800-104, Olivais Sul, adstrito a todas as deslocações 
    inerentes às suas funções, pois exercendo o trabalho a cargo da empresa.</b>'''

    texto9 = f'''<b>5.1</b> Dado que as funções e tarefas para qual o (a) <b>Segundo</b> (a) Contraente é contratado (a) 
    são condicionados á duração de Trabalho Temporário existente com o Primeiro Contraente, o presente 
    <b>Contrato de Trabalho Temporário</b>, é celebrado a Termo Certo, com início a <b>{inicio}, e 
    tendo com fim de em {fim}, mantendo-se em vigor enquanto se mantiver a causa justificativa 
    até o limite da duração máxima admitida por Lei.</b>'''

    texto10 = f'''<b>6.1</b> Como contrapartida pelo trabalho prestada o (a) Segundo (a) Contraente auferirá a título de 
    retribuiçãomensal ilíquida, a quantia de <b>{salario} euros,</b> que corresponde á tabela salarial em vigor, para categoria 
    profissional de <b>{funcao}.</b>'''

    texto11 = f'''O (a) <b>Segundo</b> (a) <b>Contraente</b> receberá ainda outras remunerações:'''

    texto12 = f'''<b>6.2 As remunerações acima referidas são sujeitas aos descontos legalmente fixados na lei.</b>'''

    texto13 = f'''<b>6.3 O (a) Segundo (a) Contraente especificamente e consente que o subsídio de férias 
    possa ser processado em duodécimos mensais, na proporção do tempo de duração do Contrato.</b>'''

    texto14 = f'''<b>6.4 O (a) Segundo (a) Contraente terá direito a um Subsídio de Natal em proporção do 
    tempo de duração do Contrato.</b>'''

    texto15 = f'''<b>7.1</b> O(a) Segundo(a) Contraente tem direito a um período de férias nos termos da Lei, 
    a determinar nos termos do disposto nos <b>artigos 237</b>.º e seguintes do <b>Código do Trabalho, Lei 
    7/2009</b>, de 12 de Fevereiro.'''

    texto16 = f'''<b>8.1 O presente contrato caduca quando, prevendo-se a ocorrência do termo incerto, o 
    Primeiro Contraente comunique ao segundo contraente a cessação do mesmo com a antecedência mínima 7, 
    15, 30 ou 60 dias, conforme o contrato tenha durado até 6 meses, de 6 meses até 2 anos ou por período superior.</b>'''

    texto17 = f'''<b>8.2</b> Caso o (a) Segundo (a) Contraente não respeite os pré-avisos atrás assinalados, 
    ficará obrigado (a) pagará FERPITRA uma indemnização de valor igual á retribuição do período de 
    antecedência em falta, sem prejuízo da responsabilidade civil pelos danos causa inobservância do prazo de aviso prévio.'''

    texto18 = f'''<b>8.3</b> Durante os primeiros 15 dias de vigência do presente Contrato qualquer das partes poderá pôr-lhe 
    termo sem invocação de justa causa, não havendo lugar a qualquer compensação ou indemniza.'''

    texto19 = f'''<b>9.1</b> É da responsabilidade da Primeira Contraente proceder à marcação do Exame de Medicina de Trabalho 
    referente à admissão do (a) Segundo (a) Contraente assim como os demais necessários por força da Lei ou 
    necessidade profissional;'''

    texto20 = f'''<b>9.2</b> O (a) Segundo (a) Contraente obriga-se a comparecer aos respetivos exames 
    sob pena de o presente Contrato de Trabalho ser considerado nulo e compromete-se a cumprir as 
    regras vigentes em matéria de Saúde, Higiene e Segurança no Trabalho.'''

    texto21 = f'''<b>9.3</b> O (a) Segundo (a) Contraente está abrangido por um seguro de acidentes 
    de trabalho com a entidade seguradora.'''

    texto22 = f'''A presente relação de trabalho aplicar-se-á, nos termos e condições previstos no 
    Código do Trabalho, o CCT (Contrato Coletivo de Trabalho) vigente para o Utilizador para além 
    das disposições legais reguladoras do Contrato de Trabalho Temporário.'''

    paragrafo1 = Paragraph(texto1, estilo_centralizado)

    if pass_ou_res == 'Passaporte':
        paragrafo2 = Paragraph(texto2, estilo_centralizado)
    elif pass_ou_res == 'Título de Residência':
        paragrafo2 = Paragraph(texto2_1, estilo_centralizado)
    elif pass_ou_res == 'Ambos':
        paragrafo2 = Paragraph(texto2_2, estilo_centralizado)

    paragrafo3 = Paragraph(texto3, estilo_centralizado)
    paragrafo4 = Paragraph(texto4, estilo_centralizado)
    paragrafo5 = Paragraph(texto5, estilo_centralizado)
    paragrafo6 = Paragraph(texto6, estilo_centralizado)
    paragrafo7 = Paragraph(texto7, estilo_centralizado)

    if tele == 'Presencial':
        paragrafo8 = Paragraph(texto8_1, estilo_centralizado)
    else:
        paragrafo8 = Paragraph(texto8, estilo_centralizado)

    paragrafo9 = Paragraph(texto9, estilo_centralizado)
    paragrafo10 = Paragraph(texto10, estilo_centralizado)
    paragrafo11 = Paragraph(texto11, estilo_centralizado)
    paragrafo12 = Paragraph(texto12, estilo_centralizado)
    paragrafo13 = Paragraph(texto13, estilo_centralizado)
    paragrafo14 = Paragraph(texto14, estilo_centralizado)
    paragrafo15 = Paragraph(texto15, estilo_centralizado)
    paragrafo16 = Paragraph(texto16, estilo_centralizado)
    paragrafo17 = Paragraph(texto17, estilo_centralizado)
    paragrafo18 = Paragraph(texto18, estilo_centralizado)
    paragrafo19 = Paragraph(texto19, estilo_centralizado)
    paragrafo20 = Paragraph(texto20, estilo_centralizado)
    paragrafo21 = Paragraph(texto21, estilo_centralizado)
    paragrafo22 = Paragraph(texto22, estilo_centralizado)
    
    frame1 = Frame(66, 305, 451, 340, showBoundary=0)
    frame1.addFromList([paragrafo1, Spacer(1, 20), paragrafo2, Spacer(1, 20), paragrafo3], p)

    p.setFillColor(HexColor("#000000"))
    p.setFont("Helvetica-Bold", 11)
    p.drawString(145, 380, f"Cláusula 1ª (Motivo de Recurso ao Trabalho Temporário)")

    frame2 = Frame(66, 130, 451, 240, showBoundary=0)
    frame2.addFromList([paragrafo4], p)

    p.setFillColor(HexColor("#000000"))
    p.setFont("Helvetica-Bold", 11)
    p.drawString(200, 245, f"Cláusula 2ª (Categoria Profissional)")

    frame3 = Frame(66, 90, 451, 140, showBoundary=0)
    frame3.addFromList([paragrafo5], p)

    #rodape
    p.line(70, 50, 520, 50)
    p.setFillColor(HexColor("#000000"))

    p.setFont("Helvetica-Bold", 6)
    p.drawString(250, 30, f"ESCRITÓRIO +351 937 906 525")

    p.setFont("Helvetica-Bold", 6)
    p.drawString(230, 20, f"RUACIDADEMOÇAMEDES Nº 242, 1800-104")

    #pagina 2
    p.showPage()

    p.setFillColor(HexColor("#000000"))
    p.setFont("Helvetica-Bold", 11)
    p.drawString(190, 780, f"Cláusula 3ª (Período Normal de Trabalho)")

    frame4 = Frame(66, 415, 451, 340, showBoundary=0)
    frame4.addFromList([paragrafo6, Spacer(1, 20), paragrafo7], p)

    p.setFillColor(HexColor("#000000"))
    p.setFont("Helvetica-Bold", 11)
    p.drawString(210, 550, f"Cláusula 4ª (Local de Trabalho)")

    frame5 = Frame(66, 200, 451, 340, showBoundary=0)
    frame5.addFromList([paragrafo8], p)

    p.setFillColor(HexColor("#000000"))
    p.setFont("Helvetica-Bold", 11)
    p.drawString(170, 450, f"Cláusula 5ª (Vigência do Contrato de Trabalho)")

    frame5 = Frame(66, 100, 451, 340, showBoundary=0)
    frame5.addFromList([paragrafo9], p)

    p.setFillColor(HexColor("#000000"))
    p.setFont("Helvetica-Bold", 11)
    p.drawString(230, 320, f"Cláusula 6ª (Retribuição)")

    frame6 = Frame(66, 100, 451, 210, showBoundary=0)
    frame6.addFromList([paragrafo10, Spacer(1, 20), paragrafo11, Spacer(1, 20), paragrafo12, Spacer(1, 20), paragrafo13, Spacer(1, 20), paragrafo14], p)

    #rodape
    p.line(70, 50, 520, 50)
    p.setFillColor(HexColor("#000000"))

    p.setFont("Helvetica-Bold", 6)
    p.drawString(250, 30, f"ESCRITÓRIO +351 937 906 525")

    p.setFont("Helvetica-Bold", 6)
    p.drawString(230, 20, f"RUACIDADEMOÇAMEDES Nº 242, 1800-104")

    #pagina 3
    p.showPage()

    p.setFillColor(HexColor("#000000"))
    p.setFont("Helvetica-Bold", 11)
    p.drawString(240, 780, f"Cláusula 7ª (Férias)")

    frame7 = Frame(66, 425, 451, 340, showBoundary=0)
    frame7.addFromList([paragrafo15], p)

    p.setFillColor(HexColor("#000000"))
    p.setFont("Helvetica-Bold", 11)
    p.drawString(200, 685, f"Cláusula 8ª (Cessação de Contrato)")

    frame7 = Frame(66, 330, 451, 340, showBoundary=0)
    frame7.addFromList([paragrafo16, Spacer(1, 20), paragrafo17, Spacer(1, 20), paragrafo18], p)

    p.setFillColor(HexColor("#000000"))
    p.setFont("Helvetica-Bold", 11)
    p.drawString(145, 435, f"Cláusula 9ª (Saúde, Higiene e Segurança no Trabalho)")

    frame8 = Frame(66, 180, 451, 240, showBoundary=0)
    frame8.addFromList([paragrafo19, Spacer(1, 5), paragrafo20, Spacer(1, 5), paragrafo21], p)

    p.setFillColor(HexColor("#000000"))
    p.setFont("Helvetica-Bold", 11)
    p.drawString(145, 260, f"Cláusula 10º (Legislação aplicável e dever de informação)")

    frame9 = Frame(66, 100, 451, 150, showBoundary=0)
    frame9.addFromList([paragrafo22], p)

    p.setFillColor(HexColor("#000000"))
    p.setFont("Helvetica-Bold", 11)
    p.drawString(240, 170, f"1º Outorgante:")
    p.line(150, 140, 420, 140)
    p.setFillColor(HexColor("#000000"))

    p.setFillColor(HexColor("#000000"))
    p.setFont("Helvetica-Bold", 11)
    p.drawString(240, 110, f"2º Outorgante:")
    p.line(150, 80, 420, 80)
    p.setFillColor(HexColor("#000000"))

    #rodape
    p.line(70, 50, 520, 50)
    p.setFillColor(HexColor("#000000"))

    p.setFont("Helvetica-Bold", 6)
    p.drawString(250, 30, f"ESCRITÓRIO +351 937 906 525")

    p.setFont("Helvetica-Bold", 6)
    p.drawString(230, 20, f"RUACIDADEMOÇAMEDES Nº 242, 1800-104")

    p.save()

#criar_contrato()

#print("PDF gerado com sucesso!")

st.write("# Contrato de Trabalho")

st_nome = st.text_input("Nome")
st_nif = st.text_input("NIF")
st_morada = st.text_input("Endereço")
st_passaporte = st.text_input("Passaporte")
st_emitido = st.text_input("Data de Emissão do Passaporte")
st_valido = st.text_input("Data de Validade do Passaporte")
st_residencia = st.text_input("Título de Residência", "n")
st_emitido_r = st.text_input("Data de Emissão do Título", "n")
st_valido_r = st.text_input("Data de Validade do Título", "n")
st_funcao = st.text_input("Função")
st_salario = st.text_input("Salário", "870,00")
st_inicio = st.text_input("Data de Início do Contrato")
st_fim = st.text_input("Data de Término do Contrato")
st_tele = st.selectbox("Modalidade do trabalho ?",("Teletrabalho", "Presencial"))
st_pass_ou_res = st.selectbox("Qual documento ele tem ?",("Passaporte", "Título de Residência", "Ambos"))

if st.button('Criar Contrato'):
    criar_contrato(nome=st_nome, nif=st_nif, morada=st_morada, passaporte=st_passaporte, emitido=st_emitido, valido=st_valido, funcao=st_funcao, salario=st_salario, inicio=st_inicio, fim=st_fim, residencia=st_residencia, emitido_r=st_emitido_r, valido_r=st_valido_r, tele=st_tele, pass_ou_res=st_pass_ou_res)

    with open("contrato.pdf", "rb") as f:
        pdf_bytes = f.read()

    st.download_button(
        label="Baixar Contrato",
        file_name="contrato.pdf",
        data=pdf_bytes,
        mime="application/pdf",
        icon=":material/download:",
    )
