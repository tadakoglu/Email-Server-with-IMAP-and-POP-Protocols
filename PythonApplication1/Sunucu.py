import socket               # Import socket module
def SunucufunctionIMAP(host, port): # IMAP SERVER FUNCTION
    s = socket.socket()         # Create a socket object 
    s.bind((host, port))        # Bind to the port
    s.listen(5)                 # Now wait for client connection.

    while True:
      print ("bekliyorum baglan, waiting you to connect me")
      c, addr = s.accept()     # Establish connection with client.
      print ('Got connection from', addr) # addr is client's ip and port couple
      #c.close()                # Close the connection
      #(conn, address) where conn is a new socket object usable to
      #send and receive data on the connection, and address is the address(ip+port)
      #bound to the socket on the other end of the connection.
    


#POP 3 FONKSİYONU

def SunucufunctionPOP3(host,port): # POP3 SERVER FUNCTION
    s = socket.socket()         # Create a socket object  
    s.bind((host, port))        # Bind to the port
    s.listen(5)                 # Now wait for client connection.

    while True:
      print ("bekliyorum baglan, waiting you to connect me")
      c, addr = s.accept()     # Establish connection with client.
      print ('Got connection from', addr)
      c.close()                # Close the connection

c=0;
addr=0;
def DNSDosyasinaYaz(ipAdresi, port): #WRITE OPENED CONNECTIONS TO DNS FILE,
    dosyamiz = open("mailSunucusu.dns", "w+")
    dosyamiz.write("%s:%s" % (ipAdresi, port))

def SunucudakiMailleriGetirVeGonder_POP3(): #BU SUNUCUDAN SİLER !! RetrieveMailsFromServerAndSendThemWithPOP THIS OPTION DELETES MAILS FROM SERVER WHEN RETRIEVING TO CLIENT, OTHER CLIENTS CAN'T REACH THESE MAILS LATER!!
    dosyamiz = open("sunucuMailKutusu.txt", "r+") #server mail box
    satir="bos";
    while True:
     satir = dosyamiz.readline()
     c.send(str.encode(satir))
     if not satir:
        dosyamiz.remove(); # POP3 PROTOCOL DELETES EMAILS FROM SERVER WHEN RETRIEVING THEM TO THE CLIENT !!
        dosyamiz.close();
        break
  
def SunucudakiMailleriGetirVeGonder_IMAP(): #BU SİLMEZ !! RetrieveMailsFromServerAndSendThemWithIMAP THIS OPTION DOESNT DELETE MAILS IN SERVER WHEN RETRIEVING TO CLIENT
    dosyamiz = open("sunucuMailKutusu.txt", "r+") #server mail box
    satir="bos";
    while True:
     satir = dosyamiz.readline()
     c.send(str.encode(satir)) #c and addr is defined at global scope and initialized by pop and imap functions
     if not satir: 
        dosyamiz.close();
        break

print ("Lütfen sunucu çalışma modu seçiniz, IMAP veya POP3, SELECT ONE")
secilen= input()

host = socket.gethostname() # Get local machine name"22.12.33.22"
port = 80                # Reserve a port for your service.

if (secilen == "IMAP"):
   #İŞLEM   
   SunucufunctionIMAP(host,port); #SUNUCU SOKETİ OLUŞTUR, CREATE SERVER SOCKET
   DNSDosyasinaYaz(host,port); #SUNUCU SOKETİ BİLGİLERİNİ(İP VE PORTU) DNS UZANTILI DOSYAYA YAZ, WRITE OPENED CONNECTION TO DNS FILE, OTHER CLIENT SOCKET MUST BE INCLUDED HERE TOO... I DIDNT..
   SunucudakiMailleriGetirVeGonder_IMAP(); #SUNUCU MAİL KUTUSUNDAKİ MAİLLERİ ÇEK VE İSTEMCİME GÖNDER RetrieveMailsFromServerAndSendThemToClientWithIMAP 

elif (secilen== "POP3"):
    #İŞLEM
    SunucufunctionIMAP(host,port); #SUNUCU SOKETİ OLUŞTUR, CREATE SERVER SOCKET
    DNSDosyasinaYaz(host,port); #SUNUCU SOKETİ VE BAĞLANTI BİLGİLERİNİ(İP VE PORTU) DNS UZANTILI DOSYAYA YAZ, WRITE OPENED CONNECTION TO DNS FILE, OTHER CLIENT SOCKET MUST BE INCLUDED HERE TOO... I DIDNT..
    SunucudakiMailleriGetirVeGonder_POP3();  #SUNUCU MAİL KUTUSUNDAKİ MAİLLERİ ÇEK VE İSTEMCİME GÖNDER, RetrieveMailsFromServerAndSendThemToClientWithPOP3 (POP3 DELETES FROM SERVER)








