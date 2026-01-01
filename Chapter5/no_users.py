usernames = []

if usernames:
    for username in usernames:
        if username == 'admin':
            print('Hello Admin, would you like to see a status report?')
        else:
            print(f'Welcome to the world of Tomorrow, {username}!')
else:
    print('We might need to find some users...')