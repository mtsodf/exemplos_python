# Eu vou pular de paraquedas caso tenha coragem e meu médico permitir
tenho_coragem = True
meu_medico_permitiu = True
vou_pular_de_paraquedas = tenho_coragem and meu_medico_permitiu
print("vou_pular_de_paraquedas =", vou_pular_de_paraquedas)


# Eu vou viajar se eu tiver dinheiro e a passagem não esteja cara
tenho_dinheiro = True
passagem_cara = False
vou_viajar = tenho_dinheiro and (not passagem_cara)
print("vou_viajar = ", vou_viajar)


# Eu vou viajar se eu tiver dinheiro e a passagem esteja barata
tenho_dinheiro = True
passagem_barata = True
vou_viajar = tenho_dinheiro and passagem_barata
print("vou_viajar = ", vou_viajar)
