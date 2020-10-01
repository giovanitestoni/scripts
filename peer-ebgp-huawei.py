print("Gerador de script peer bgp VRP Huawei")
print()
input("Pressione Enter para iniciar: \n")

asn_local = input('Qual o número do ASN local? ')
asn_remote = input('Qual o número do ASN remoto? ')
group = input('Qual o nome do seu peer group? ')
peer = input('Qual o endereco do peer? ')
print()
print('#')
print('route-policy IN-IPv4-'+group +' deny node 1') #Cria filtro negando tudo
print('route-policy OUT-IPv4-'+group +' deny node 1') #Cria filtro negando tudo
print('#')
print("bgp "+asn_local)
print('group '+group+' external')
print('peer '+group+' as-number '+asn_remote)
print('peer '+group+' advertise-community')
print('peer '+peer+' group '+group)
print('peer '+group+' route-policy IN-IPv4-'+group+' import')
print('peer '+group+' route-policy OUT-IPv4-'+group+' export')
print('#')
print()
retorno = input('Deseja gerar gerar outro peer? 1-SIM 2-NAO ')
sim = "1"
não = "2"
if retorno == sim:
    asn_remote = input('Qual o número do ASN remoto? ')
    group = input('Qual o nome do seu peer group? ')
    peer = input('Qual o endereco do peer? ')
    print()
    print('#')
    print('route-policy IN-IPv4-'+group +' deny node 1') #Cria filtro negando tudo
    print('route-policy OUT-IPv4-'+group +' deny node 1') #Cria filtro negando tudo
    print('#')
    print("bgp "+asn_local)
    print('group '+group+' external')
    print('peer '+group+' as-number '+asn_remote)
    print('peer '+group+' advertise-community')
    print('peer '+peer+' group '+group)
    print('peer '+group+' route-policy IN-IPv4-'+group+' import')
    print('peer '+group+' route-policy OUT-IPv4-'+group+' export')
    print('#')
    print()
    pass
if retorno == não:
    exit()
    pass
    