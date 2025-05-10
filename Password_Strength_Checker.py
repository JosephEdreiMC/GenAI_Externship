def password_strength():
    unsafe=True
    while unsafe:
        password = input('Enter a password: ')
        password_issues={'length':True, 'upper':True, 'lower':True, 'digit':True, 'special':True}
        if len(password)>=8: password_issues['length']=False
        # Counters for assigning a score to the password
        upper_counter, lower_counter, digit_counter, special_counter=0,0,0,0
        for char in password:
            if char.isupper():
                password_issues['upper']=False
                upper_counter +=1
            if char.islower():
                password_issues['lower'] = False
                lower_counter +=1
            if char.isdigit():
                password_issues['digit']=False
                digit_counter +=1
            if not char.isupper() and not char.islower() and not char.isdigit() and char!=' ':
                password_issues['special'] = False
                special_counter+=1
        # Get values in dictionary
        issues=list(password_issues.values())
        issues_couter=0
        for i in issues: issues_couter += i
        # Check if the password is valid
        if issues_couter==0:
            print('Your password is strong!')
            unsafe=False
            # Giving a score to the password
            extra_score=(len(password)>8)+(upper_counter>1)+(lower_counter>1)+(digit_counter>1)+(special_counter>1)
            print(f'Password Strength: {5+extra_score}/10')
        # If not, explain errors and ask for a new password
        else:
            print('Your password is lacking the following: '+
                  password_issues['length']*'Your password must be at least 8 characters long.  '+
                  password_issues['upper']*'Your password must contain at least one uppercase letter.   '+
                  password_issues['lower']*'Your password must contain at least one lowercase letter.   '+
                password_issues['digit']*'Your password must contain at least one digit.    '+
                password_issues['special'] * 'Your password must contain at least one special character.')
            print(f'Password Strength: {5-issues_couter}/10')
password_strength()

