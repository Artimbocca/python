t = ('Othello', 'Iago')
print (t)         # ('Othello', 'Iago')

hero, villain = t

print (hero)     # 'Othello'
print (villain)  # 'Iago'

hero, villain = villain, hero
print (hero)     # 'Iago'
print (villain)  # 'Othello'
