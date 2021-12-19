import socket
import msvcrt

#Metodos predefinidos para encontrar la Direccion ip & nombre
hostname = socket.gethostname()
ip = socket.gethostbyname(hostname)

print("======================================")
print("             ¡WELCOME!                ")
print("====================================== \n")

print("El nombre de tu ordenador es: "+ hostname)
print("La IP de tu ordenador es: " + ip)
print("\n")
print("       ¡BYE!      \n")
print(""" 
                 .:::::::::::::.  
                .::'  '''''  '::. 
                :::           ::: 
                :::           ::: 
                :::           ::: 
                ::'           ':: 
                : : /~~~' '~~~\ : :
                :(:  <o> | <o>  :):
                '.:     / \     :.'
                 ':    (. .)    :' 
                  '.  .:::::.  .'
                   :  <----->  :   
                   '.  ~:::~  .'
                     '.  '  .'     
                      ''''' 	""")

msvcrt.getch()