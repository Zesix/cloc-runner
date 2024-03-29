import subprocess
import smtplib
import ssl
import sys

is_windows = sys.platform.startswith('win')

# check if git is installed
try:
    subprocess.run(['git', '--version'], stdout=subprocess.PIPE, check=True)
except Exception as e:
    print(e)
    print('Error! Git is not installed. Please install git to use this script.')
    input('Press Enter to exit!')
    exit()

# check if perl is installed
try:
    subprocess.run(['perl', '-v'], stdout=subprocess.PIPE, check=True)
except Exception as e:
    print(e)
    print('Error! Perl is not installed. Please install perl to use this script.')
    input('Press Enter to exit!')
    exit()

# check if openssl is installed
try:
    subprocess.run(['openssl', 'version'], stdout=subprocess.PIPE, check=True)
except Exception as e:
    print(e)
    print('Error! OpenSSL is not installed. Please install OpenSSL to use this script.')
    input('Press Enter to exit!')
    exit()

try:
    repo = input('Enter git repo link: ').strip()  # removes spaces from corners
    dir_name = repo.split('/')[-1].replace('.git', '')
    # print('dir name: ', dir_name)

    # shallow clone the repo
    subprocess.run(['git', 'clone', '--depth', '1', repo], stdout=subprocess.PIPE, check=True, shell=True)
    print('Cloned successfully.')
except Exception as e:
    print(e)
    input('Press Enter to exit!')
    exit()

try:
    cloc_output = subprocess.run(['cloc', dir_name], stdout=subprocess.PIPE, check=True, shell=True )
    print('CLOC operation performed successfully.')
    # print(b.check_returncode())
    cloc_output = str(cloc_output.stdout, 'utf-8')
except Exception as e:
    print(e)
    input('Press Enter to exit!')
    exit()

try:
    # delete cloned directory
    if is_windows:
        subprocess.run(['rd', '/Q', '/S', dir_name], stdout=subprocess.PIPE, check=True, shell=True)
    else:
        subprocess.run(['rm', '-rf', dir_name], stdout=subprocess.PIPE, check=True)
    print('Deleted cloned repo successfully.')
except Exception as e:
    print(e)
    input('Press Enter to exit!')
    exit()

# sender_email, password = open('sender.txt').read().split(':')
sender_email = 'clocoutput@gmail.com'
password = 'WSync8VM!'
# print(sender_email)
# print(password)

# receiver prompt
receiver = open('receiver.txt').read().strip('\n')
# print(receiver)
check = input(f'Do you want to send the results to {receiver}?[Y/N] ')
if check in ['Y', 'y']:
    pass
else:
    receiver = input('Enter email to send results: ')

# setting up smtp server and entering credentials
port = 587  # For starttls
smtp_server = "smtp.gmail.com"
receiver_email = receiver

# generate email
subject = dir_name
message = f'Subject: CLOC output for: {subject}\n\n{cloc_output}'
context = ssl.create_default_context()

# send email
try:
    context = ssl.create_default_context()
    with smtplib.SMTP(smtp_server, port) as server:
        server.starttls(context=context)
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, message)
        server.quit()
        print('Email sent successfully.')
except Exception as e:
    print(e)

input('Press Enter to exit!')
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  
