"""
Crie um programa que verifica a hora atual (em horas) e 
exibe uma mensagem que diz 'Bom dia' se estiver de 1 às 12, 
'Boa tarde' entre 13 às 18 e 'Boa noite' para as horas restantes
"""

from datetime import datetime

hora = datetime.now().hour

# Forma 1
if hora >= 1 and hora <= 12:
    print("Bom dia")
elif hora >= 13 and hora <= 18:
    print("Boa tarde")
else:
    print("Boa noite")

# Forma 2
if 1 <= hora <= 12:
    print("Bom dia")
elif 13 <= hora <= 18:
    print("Boa tarde")
else:
    print("Boa noite")
