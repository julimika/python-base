#!/usr/bin/env python3
"""Hello World Multi Línguas.

Dependendo da língua configurada no ambiente, 
o programa exibe a mensagem correspondente.

Como usar:
tenha a variável LANG devidamente configurada. 
ex:
    export LANG=pt_BR

execução:

    python3 hello.py
    ou 
    ./hello.py

"""
__version__ = "0.0.1"
__author__ = "Mika"
__license__ = "unlicensed"

import os


current_language =  os.getenv("LANG")[:5]
print(current_language)

msg = "Hello, World!"

if current_language == "pt_BR":
    msg = "Olá, mundo!"
elif current_language == "it_IT":
    msg = "Ciao, Mondo!"






print(msg)

