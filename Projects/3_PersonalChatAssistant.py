import datetime

presentHour = datetime.datetime.now().hour

print("Hello , Welcome to your Chatbot")

name = input("Enter your name : ")

if presentHour >= 5 and presentHour <12:
    print(f"Good Morning , {name}")

elif presentHour >=12 and presentHour <17:
    print(f"Good Afternoon , {name}")

elif presentHour >=17 and presentHour <22:
    print(f"Good evening , {name}")     

else:
    print(f"Good Night , {name}")      




print("You can ask me basic questions , Type 'bye' to exit from the bot ")


responses = {
    "hello" : "Hii",
    "How are you" : "fine , how are you ",
    "who are you" : "I am AI chatbot",
    "happy": " Great to hear that"
}

def getResponseOfBot(userQuestion):
    userQuestion = userQuestion.lower()

    for eachKey in responses:
        if eachKey in userQuestion:
            return responses[eachKey]
    return "Abhi mujhe iske bare me nhi pta"   


while True:
    response = input("Ask anything : ")

    if response == "bye" or response == "Bye":
        print("Nice to talk you , Bye")
        break

    reply = getResponseOfBot(response)
    print(f"Bot reply : {reply}")

   

