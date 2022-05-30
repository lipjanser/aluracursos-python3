import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import random as rd
from random import shuffle as sff
import copy as cp

def enviar_email(amigos_secretos, sorteados):
    username = "SEU_EMAIL"
    password = "SUA_SENHA_CRIPTOGRAFADA"
    mail_from = "SEU_EMAIL"
    mail_subject = "[AGORA VAI PAPAAAI]] Rolê do HotDog - Amigo Secreto"
    

    for i in range(len(amigos_secretos)):
        mimemsg = MIMEMultipart()
        mimemsg['From']=mail_from
        mimemsg['To']=amigos_secretos[i]
        mimemsg['Subject']=mail_subject
        mail_body = "Saudações caro terráqueo, seu amigo secreto é {} !!! Quero reforçar que eu NÃO SEI quem tirou quem. Escrevi um programinha em Python para SORTEAR nossos amigos secretos. Me confirma lá no grupo se ninguém tirou a si mesmo kkkkk!!".format(sorteados[i])
        mimemsg.attach(MIMEText(mail_body, 'plain'))

        connection = smtplib.SMTP(host='smtp.gmail.com', port=587)
        connection.starttls()
        connection.login(username,password)
        connection.send_message(mimemsg)
        connection.quit()
    print('Mensagens enviadas!')

def abrir_arquivo_amigo_secreto():
    with open("amigo_secreto.txt","r") as arquivo:  
        amigos_secretos = arquivo.readlines()
    return amigos_secretos


def sortear_amigo_secreto(amigos_secretos):
    ordem = cp.copy(amigos_secretos)
    index = 0
    while index < len(amigos_secretos):
        sff(ordem)
        if amigos_secretos[index] == ordem[index]:
            index=0
            continue
        else:
            index+=1
    print('Ordem: {}'.format(ordem))
    print('Amigos secretos: {}'.format(amigos_secretos))
    
    return ordem

amigos_secretos = abrir_arquivo_amigo_secreto()
sorteados = sortear_amigo_secreto(amigos_secretos)
enviar_email(amigos_secretos, sorteados)