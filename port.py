import socket
import sys
#import threading


print(" >>>  by: t4ucci")
print("Basic-Scanner-Iniciative: BSI \n\n     version: 1.1")

print("""

....................../´¯/) 
....................,/¯../ 
.................../..../ 
............./´¯/'...'/´¯¯`·¸ 
........../'/.../..../......./¨¯\ 
........('(...´...´.... ¯~/'...') 
.........\.................'...../ 
..........''...\.......... _.·´ 
............\..............( 
..............\.............\...

""")

def portscanner():
    url = input("\n   Internet Protocol[IP]: ")
 #   th = int(input("\n   Quantidade de Threads[VEL]: "))
    try:
        for port in range(1,1000+1):
            tcp_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            pt1 = (url, port)
            dados = tcp_server.connect_ex(pt1)
            if dados == 0:
                print("  \n[♤] Porta ABERTA: {}:::{}\n".format(port, socket.getservbyport(port)))
            else:
                print("  \n[♧] Porta FECHADA: {}:::{}\n".format(port, socket.getservbyport(port)))
    except socket.error:
        print("\n[♧] Erro durante a rede...!")
        tcp_server.close()
        exit()
def one_port():
    try:
        url2 = str(input("\nIP/URL: "))
        port2 = int(input("Porta: "))
    #th2 = int(input("Threads[VEL]: "))
        tcp_server2 = socket.socket(socket.AF_INET,         socket.SOCK_STREAM)
        pt = (url2, port2)
        dados2 = tcp_server2.connect_ex(pt)
        if dados2 == 0:
            print(f"  \n>>> A porta: {port2} está aberta!\n ")
            print("""\n ░░░░░▄▄▄▄▀▀▀▀▀▀▀▀▄▄▄▄▄▄░░░░░░░
░░░░░█░░░░▒▒▒▒▒▒▒▒▒▒▒▒░░▀▀▄░░░░
░░░░█░░░▒▒▒▒▒▒░░░░░░░░▒▒▒░░█░░░
░░░█░░░░░░▄██▀▄▄░░░░░▄▄▄░░░░█░░
░▄▀▒▄▄▄▒░█▀▀▀▀▄▄█░░░██▄▄█░░░░█░
█░▒█▒▄░▀▄▄▄▀░░░░░░░░█░░░▒▒▒▒▒░█
█░▒█░█▀▄▄░░░░░█▀░░░░▀▄░░▄▀▀▀▄▒█
░█░▀▄░█▄░█▀▄▄░▀░▀▀░▄▄▀░░░░█░░█░
░░█░░░▀▄▀█▄▄░█▀▀▀▄▄▄▄▀▀█▀██░█░░
░░░█░░░░██░░▀█▄▄▄█▄▄█▄████░█░░░
░░░░█░░░░▀▀▄░█░░░█░█▀██████░█░░
░░░░░▀▄░░░░░▀▀▄▄▄█▄█▄█▄█▄▀░░█░░
░░░░░░░▀▄▄░▒▒▒▒░░░░░░░░░░▒░░░█░
░░░░░░░░░░▀▀▄▄░▒▒▒▒▒▒▒▒▒▒░░░░█░
░░░░░░░░░░░░░░▀▄▄▄▄▄░░░░░░░░█░░\n""")
        else:
            print(f"\n   >>> A porta {port2} está fechada...")
    except socket.error:
        print("[♧] Erro durante a rede...!")
                
opc = input("1] Ver ambas portas \n2] Ver uma porta \n3] Sair\n\n>>> ")

if opc == '1':
    portscanner()
elif opc == '2':
    one_port()
elif opc == '3':
    print("\n   Saindo...!")
    exit()
else:
    print("\n>>> Opção errada! Tente de novo.")
    exit()

#for i in range(th):
    #thred = threading.Thread(target=portscanner)
    #thred.start()
#for j in range(th2):
  #  thred2 = threading.Thread(target=one_port)
    #thred2.start()
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    