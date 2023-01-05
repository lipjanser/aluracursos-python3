endereco = "Rua Barão de Itamaracá 379, Apto 1101, Espinheiro, Recife, PE, 52020-070"

import re #Regular Expressions -- RegEx

padrao = re.compile("[0-9]{5}[-]{0,1}[0-9]{3}")
busca = padrao.search(endereco) #}Match

if busca:
    cep = busca.group()
    print(cep)
else:
    print("CEP não encontrado")