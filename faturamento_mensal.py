sp = float(67.83643)
rj = float(36.67866)
mg = float(29.22988)
es = float(27.16548)
out = float(19.84953)

somatoria = float(sp + rj + mg + es + out)

percentualSP = ((sp/somatoria)*100)
percentualRJ = ((rj/somatoria)*100)
percentualMG = ((mg/somatoria)*100)
percentualES = ((es/somatoria)*100)
percentualOUT = ((out/somatoria)*100)

print('Porcentagem de SP {}'.format(percentualSP))
print('Porcentagem de RJ {}'.format(percentualRJ))
print('Porcentagem de MG {}'.format(percentualMG))
print('Porcentagem de ES {}'.format(percentualES))
print('Porcentagem de OUT {}'.format(percentualOUT))