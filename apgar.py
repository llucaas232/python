print("Bem-vindo ao programa de escala de APGAR.")
musc=int(input("Defina a pontuação da musculatura\n"
"0 - Músculos flácidos;\n"
"1 - Dobra os dedos e movimenta os braços e pernas;\n"
"2 - Se movimenta ativamente.\n"
"Digite a pontuação: "))
card=int(input("Defina a pontuação do batimento cardíaco:\n"
"0 - Sem batimento cardíaco;\n"
"1 - Inferior a 100 BPM;\n"
"2 - Superior a 100 BPM.\n"
"Digite a pontuação:"))
refl=int(input("Defina a pontuação dos reflexos:\n"
"0 - Não responde a estímulos;\n"
"1 - Faz caretas quando estimulado;\n"
"2 - Chora, tosse ou espirra.\n"
"Digite a pontuação:"))
cor=int(input("Defina a pontuação da cor:\n"
"0 - Coloração pálida ou azul-acinzentada\n" 
"1 - Coloração rosada no corpo, mas azulada nos pés ou mãos;\n"
"2 - Coloração rosada no corpo inteiro.\n"
"Digite a pontuação:"))
resp=int(input("Defina a pontuação da respiração:\n"
"0 - Não há respiração;\n"
"1 - Choro fraco com respiração irregular;\n"
"2 - Choro forte com respiração regular.\n"
"Digite a pontuação:"))
pont=(musc+card+refl+cor+resp)
print("A pontuação final da escala de APGAR é",pont)
print("Classificações de pontuação final:\n"
"Sem asfixia: 8-10\n"
"Asfixia moderada: 4-7\n"
"Asfixia grave: 0-3")
if pont>=8:
    print("O bebê nasceu com boa vitalidade.")
elif pont>=4:
    print("O bebê sofreu uma asfixia moderada.")
elif pont>=0:
    print("O bebê sofreu uma asfixia grave.")