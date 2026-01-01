current_users = ['Hitomi_Honda', 'IzanagI', 'ganso', 'pato', 'ELIAS']

new_users = ['sakura_miyawaki', 'joker', 'Ganso', 'joao_guilherme', 'gabriel']

current_users_lower = []
for user in current_users:
    current_users_lower.append(user.lower())

for new_user in new_users:
    if new_user.lower() in current_users_lower:
        print(f'Sorry, {new_user} is already in use! You will need to enter a new username.')
    else:
        print(f'The username {new_user} is available.')