s_antigo = float(input('Qual o salário do funcionário? R$ '));
aumento = s_antigo * (15/100);
s_atual = s_antigo + aumento;

print('O funcionário que recebia R$ {:0.2f} reais, com 15% de aumento salarial, deve passar a receber R$ {:0.2f} reais.'.format(s_antigo, s_atual));