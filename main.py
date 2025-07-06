import yagmail
txt = r"""
__________                    __________              ___.                 
\_   _____/____    ____    ____\______   \ ____   _____\_ |__   ___________ 
 |    __) \__  \  /    \  / ___\|    |  _//  _ \ /     \| __ \_/ __ \_  __ \
 |     \   / __ \|   |  \/ /_/  >    |   (  <_> )  Y Y  \ \_\ \  ___/|  | \/
 \___  /  (____  /___|  /\___  /|______  /\____/|__|_|  /___  /\___  >__|   
     \/        \/     \//_____/        \/             \/    \/     \/       
"""

def print_banner():
    GREEN = "\033[92m"
    RESET = "\033[0m"
    print(f"{GREEN}{txt}{RESET}")
def main():
    print_banner()
    LIGHT_GREEN = "\033[96m"
    RESET = "\033[0m"
    print(f"{LIGHT_GREEN}Welcome to the FangBomber!\nThis is a simple bomber that can be used to send a lot of messages to a user.\t\t\tby Rai from ByteFang🐉\nPlease use it responsibly and ethically.\n-----------------------------------------------------------------------------{RESET}")
    print(f"{LIGHT_GREEN}Type 'help' for a list of commands.{RESET}")
    while True:
        inp = input(f"{LIGHT_GREEN}> {RESET}")
        if inp == "q":
            print(f"{LIGHT_GREEN}Exiting FangBomber... Good Bye!{RESET}")
            break
        elif inp == "help":
            print(f"""{LIGHT_GREEN}
            help   : Display this help message.
            q      : Quit the FangBomber application.
            sbombs : Send SMS messages (Not available yet).
            gbombl : Send Gmail messages.
            cbombl : Call Bombing (Not available yet).
            {RESET}""")
        elif inp == "gbombl":
            print(f"{LIGHT_GREEN}You have selected Gmail Bombing.{RESET}")
            sender_email = input(f"{LIGHT_GREEN}Enter your Gmail address: {RESET}")
            app_password = input(f"{LIGHT_GREEN}Enter your app password: {RESET}")
            recipient_email = input(f"{LIGHT_GREEN}Enter the recipient's email address: {RESET}")
            subject = input(f"{LIGHT_GREEN}Enter the subject of the email: {RESET}")
            message = input(f"{LIGHT_GREEN}Enter the message to send: {RESET}")
            num_emails = int(input(f"{LIGHT_GREEN}Enter the number of emails to send: {RESET}"))
            try:
                yag = yagmail.SMTP(sender_email, app_password)
                for i in range(num_emails):
                    yag.send(to=recipient_email, subject=subject, contents=message)
                    print(f"{LIGHT_GREEN}Email {i+1} sent successfully!{RESET}")
            except Exception as e:
                print(f"{LIGHT_GREEN}An error occurred while sending emails: {e}{RESET}")
        else:
            print(f"{LIGHT_GREEN}Unknown command: {inp}. Type 'help' for a list of commands.{RESET}")
            
        
if __name__ == "__main__":
    main()