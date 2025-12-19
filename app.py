import os
from processor import ask_gemini
from auth import verify_user
from document_handler import process_vault_pdfs
from processor import ask_vault_ai

def main():
    print("--- 🔐 AI SECURE VAULT ---")
    
    # PEHLE FACE-ID CHECK HOGA
    if verify_user():
        print("✅ Access Granted!")
        
        # 1. PDFs ko scan karke vault taiyar karna
        print("🔄 Scanning Vault Documents...")
        process_vault_pdfs()
        
        # 2. AI Chat shuru karna
        while True:
            user_input = input("\nAsk anything about your documents (exit to lock): ")
            if user_input.lower() == 'exit':
                print("🔒 Vault Locked.")
                break
            
            answer = ask_vault_ai(user_input)
            print(f"\n🤖 VAULT AI: {answer}")
    else:
        print("❌ Access Denied! Unauthorized Person Detected.")

if __name__ == "__main__":
    main()

def start_vault():
    print("\n" + "="*30)
    print("🔒 WELCOME TO AI SECURE VAULT")
    print("="*30 + "\n")

    # 1. Sabse pehle Security Check
    print("Step 1: Authenticating User...")
    access_granted = verify_user()

    if access_granted:
        print("\n✅ ACCESS GRANTED! Welcome back, User.")
        print("-" * 30)
        
        # 2. Login hone ke baad AI Assistant chalu hoga
        while True:
            user_query = input("\nAap kya puchna chahte hain? (Band karne ke liye 'exit' likhein): ")
            
            if user_query.lower() == 'exit':
                print("Vault se bahar nikal rahe hain. Bye!")
                break
            
            print("\n🤖 AI Soch raha hai...")
            response = ask_gemini(user_query)
            print(f"\nAI Ka Jawab: {response}")
            print("-" * 30)
    else:
        print("\n❌ ACCESS DENIED! Face match nahi hua.")

if __name__ == "__main__":
    start_vault()

if verify_user(): # Yeh auth.py ke function ko bulayega
    print("Login Success!")