email= input('Please enter a email: ')

email_tuple= email.partition('@')

redacted_username= email_tuple[0][0] + '*' * (len(email_tuple[0]) - 2) + email_tuple[0][-1]

domain= email_tuple[-1].partition('.')

redacted_domain= domain[0][0] + '*' * (len(domain[0]) - 1) + domain[1] + domain[-1]

redacted_email= redacted_username + email_tuple[1] + redacted_domain

print(redacted_email)
