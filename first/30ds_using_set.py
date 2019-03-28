bri = set(['brazail', 'russia', 'india'])
print('india' in bri)
print('usa' in bri)

bric = bri.copy()
bric.add('china')
print(bric.issuperset(bri))
print(bri)
print(bric)