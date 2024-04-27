import random
import spacy
users = {}
hos={}
name_hos=[]
def med():
# Load the spaCy NLP model
  nlp = spacy.load('en_core_web_sm')

  # Define some rules for the chatbot
  rules = {
      "fever": {
          "keywords": ["fever", "high temperature", "hot"],
          "responses": ["You may have a fever. It's important to monitor your temperature and rest. If your fever persists or is very high, you should seek medical attention. Over-the-counter medications like ibuprofen or acetaminophen can help reduce fever symptoms."],
          "medications": ["ibuprofen", "acetaminophen"]
      },
      "cough": {
          "keywords": ["cough", "coughing"],
          "responses": ["A persistent cough can be a symptom of many different conditions, including the common cold, flu, or COVID-19. It's important to monitor your symptoms and seek medical attention if your cough persists or is accompanied by other symptoms like chest pain or difficulty breathing. Over-the-counter medications like cough suppressants or throat lozenges can help relieve cough symptoms."],
          "medications": ["cough suppressants", "throat lozenges"]
      },
      "headache": {
          "keywords": ["headache", "head pain"],
          "responses": ["A headache can be caused by many different things, including stress, dehydration, or more serious conditions like migraines or meningitis. It's important to monitor your symptoms and seek medical attention if your headache is severe or accompanied by other symptoms like vomiting or vision changes. Over-the-counter medications like ibuprofen or acetaminophen can help relieve headache symptoms."],
          "medications": ["ibuprofen", "acetaminophen"]
      },
      "flu": {
          "keywords": ["flu", "influenza"],
          "responses": ["The flu is a viral infection that affects the respiratory system. Symptoms can include fever, chills, body aches, and respiratory symptoms like a cough or runny nose. It's important to rest, stay hydrated, and seek medical attention if your symptoms are severe or persist for more than a few days. Over-the-counter medications like acetaminophen or ibuprofen can help relieve flu symptoms."],
          "medications": ["acetaminophen", "ibuprofen"]
      },
      "covid": {
          "keywords": ["covid", "coronavirus"],
          "responses": ["COVID-19 is a viral infection that primarily affects the respiratory system. Symptoms can include fever, cough, and difficulty breathing. It's important to monitor your symptoms, practice social distancing, and seek medical attention if your symptoms are severe or persist for more than a few days. There is currently no FDA-approved medication for COVID-19, but over-the-counter medications like acetaminophen or ibuprofen can help relieve symptoms."],
          "medications": ["acetaminophen", "ibuprofen"]
      }
  }

  # Define a function to match user input to rules
  def match_rule(user_input):
      # Use the spaCy NLP model to extract named entities from the user input
      doc = nlp(user_input)
      entities = [(X.text, X.label_) for X in doc.ents]
      
      for rule in rules.values():
          for keyword in rule["keywords"]:
              if keyword.lower() in user_input.lower() or any(entity[0].lower() == keyword.lower() for entity in entities):
                  return rule
      return None

  # Define a function to generate a response based on the matched rule
  def generate_response(matched_rule):
      if matched_rule is not None:
          response = random.choice(matched_rule["responses"])
      else:
          response = "I'm not sure how to help you with that. Can you please try asking something else?"
      return response

  # Define the main chatbot function
  def chatbot():
      print("Hi, I'm a medical chatbot.How can I help you today?")
      while True:
          user_input = input("You: ")
          if user_input.lower() == "hi" or user_input.lower() == "hello":
              print("Chatbot: Hi there! How can I help you with your medical concerns?")
          elif user_input.lower() in {"quit", "exit"}:
              break
          else:
              matched_rule = match_rule(user_input)
              response = generate_response(matched_rule)
              print("Chatbot: " + response)

  # Run the chatbot function
  chatbot()
#(blood donation)
def blood_donation():
    bd_name=input("Enter your name:")
    bd_group=input("Enter your Blood Group:")
    print(name_hos)
    name_don=input("Enter hospital name:")
    empty=0
    loyal=0
    if name_hos is empty:
        print("no hos available")
    else:
        if name_don in name_hos:
            print("Appointment scheduled")
            print("donation done")
            print(bd_name+" "+"certificate generated")
            loyal=loyal+1000
            print("loyal points:",loyal)
            rup=0
            rup=loyal/5
        else:
            print("select another hospital")
#(blood request)
def blood_request():
    br_group=input("Enter blood group")
    
def details():
    #enter no of members of family
    n=int(input('enter number of members living in family: '))
    for i in range(n):
        print("person:"+str(i+1))
        print("Name"+"="+input("Enter person name:"))
        print("DOB"+"="+input("Enter your DOB:"))
        print("Gender"+"="+input("Enter your Gender:"))
        print("Blood Group"+"="+input("Enter your Blood Group:"))
    while True:
        print("\noption:")
        print("1.Blood donation")
        print("2.Request")
        print("3.Basic Med Chatbot")
        print("4.Quit")
    
        choice = input("Enter your choice (1/2/3): ")
    
        if choice == "1":
            blood_donation()
        elif choice == "2":
            blood_request()
        elif choice == "3":
            med()
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please select a valid option (1/2/3).")   
def signup():
    print("Signup")
    username = input("Enter your username: ")
    password = input("Enter your password: ")
   
    
    if username in users:
        print("Username already exists. Please choose a different username.")
    else:
        users[username] = password
        print("Signup successful. You can now log in.")
def hosp():
    print("HOS Signup")
    hos_name=input("Enter your hospital name: ")
    user = input("Enter your username: ")
    pas = input("Enter your password: ")
    if user in hos:
        print("Username already exists. Please choose a different username.")
    else:
        hos[user] = pas
        print("Signup successful. You can now log in.")
    name_hos.append(hos_name)
    print(name_hos)
def hos_sign():
    print("Login")
    user = input("Enter your username: ")
    pas = input("Enter your password: ")
    
    
    if user in hos and hos[user] == pas:
        print("Login successful. Welcome, " + user + "!")
        
        
    else:
        print("Invalid username or password. Please try again.")

def login():
    print("Login")
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    
    
    if username in users and users[username] == password:
        print("Login successful. Welcome, " + username + "!")
        details()
        
    else:
        print("Invalid username or password. Please try again.")

# Main program loop
print("WELCOME TO HCMS")
while True:
    print("\nSIGNUP/LOGIN:")
    print("1. Signup")
    print("2. Login")
    print("3. Hospital SIGNUP")
    print("4. HS LOGIN")
    print("5. Quit")
    choice = input("Enter your choice (1/2/3/4): ")
    if choice =="1":
        signup()
    elif choice =="2":
        login()
    elif choice =="3":
        hosp()
    elif choice =="4":
        hos_sign()
    elif choice =="5":
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please select a valid option (1/2/3/4).")
