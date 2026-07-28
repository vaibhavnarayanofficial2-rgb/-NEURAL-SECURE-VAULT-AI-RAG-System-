import os
from processor import ask_gemini
from auth import verify_user
from document_handler import process_vault_pdfs
from processor import ask_vault_ai

def main():
    print("--- AI SECURE VAULT ---")
    
    # FACE-ID CHECK 
    if verify_user():
        print("Access Granted!")
        
        # 1. PDFs scan vault 
        print("Scanning Vault Documents...")
        process_vault_pdfs()
        
        # 2. AI Chat starting
        while True:
            user_input = input("\nAsk anything about your documents (exit to lock): ")
            if user_input.lower() == 'exit':
                print("Vault Locked.")
                break
            
            answer = ask_vault_ai(user_input)
            print(f"\n VAULT AI: {answer}")
    else:
        print("Access Denied! Unauthorized Person Detected.")

if __name__ == "__main__":
    main()

def start_vault():
    print("\n" + "="*30)
    print("WELCOME TO AI SECURE VAULT")
    print("="*30 + "\n")

    # 1.Security Check
    print("Step 1: Authenticating User...")
    access_granted = verify_user()

    if access_granted:
        print("\n ACCESS GRANTED! Welcome back, User.")
        print("-" * 30)
        
        # 2. After Login AI Assistant starting
        while True:
            user_query = input("\n How can i help you? ( 'exit' ): ")
            
            if user_query.lower() == 'exit':
                print("Exit for vault. Bye!")
                break
            
            print("\n AI runinnig ...")
            response = ask_gemini(user_query)
            print(f"\nAI answer: {response}")
            print("-" * 30)
    else:
        print("\n ACCESS DENIED! Face match not found.")

if __name__ == "__main__":
    start_vault()

if verify_user(): # calling auth.py function 
    print("Login Success!")
