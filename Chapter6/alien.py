aliens = []

for new in range(5):
    alien = {'color':'yellow','points':10, 'speed':'medium'}
    aliens.append(alien)

for new in range(25):
    alien = {'color':'green','points':5, 'speed':'slow'}
    aliens.append(alien)

print('Current aliens list:')
for alien in aliens[:20]:
    print(alien)

for alien in aliens[:10]:
    if alien['color'] == 'green':
        alien['color'] = 'yellow'
        alien['points'] = 10
        alien['speed'] = 'medium'
    
    elif alien['color'] == 'yellow':
        alien['color'] = 'red'
        alien['points'] = 15
        alien['speed'] = 'fast'

print('\nNew aliens list:')
for alien in aliens[:20]:
    print(alien)