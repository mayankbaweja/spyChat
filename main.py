from spy_details import spy, Spy, ChatMessage, dhabi
from steganography.steganography import Steganography
from datetime import datetime
from termcolor import colored
print "Namaskar!"
print "Shuru Karein"
# Concatenation of strings using + sign
prashna = "Aap " + spy.salutation + " " + spy.naam + " hi ho kya (Y/N)? "
# Take an input as a string and save it to a variable 'existing'
existing = raw_input(prashna)
# List with some default status messages
STATUS_MESSAGES=["Katti Aakharr", "Latth sa gaad rakhya hai"]
EMERGENCY_MESSAGES=["SOS","SAVE ME"]


# Function to add status
def add_status():
    updated_status_message = None
    if spy.current_status_message != None:
        print "Apka status message hai " + spy.current_status_message + "\n"
    else:
        print "Koi status message nahi hai abhi \n"
    default = raw_input("Purane status mein se select karoge (y/n)? ")
    # upper is used to convert the input into upper case
    if default.upper() == "N":
        new_status_message = raw_input("Kya status message daalna hai?")
        if len(new_status_message) > 0:
            updated_status_message = new_status_message
            STATUS_MESSAGES.append(new_status_message)
    elif default.upper() == "Y":
        item_position = 1
        for message in STATUS_MESSAGES:
            print '%d. %s' % (item_position, message)
            item_position = item_position + 1
        message_selection = int(raw_input("\nInmein se choose karlo "))
        if len(STATUS_MESSAGES) >= message_selection:
            updated_status_message = STATUS_MESSAGES[message_selection - 1]

    return updated_status_message


# Function to add a friend
def add_dhabi():
    naya_dhabi = Spy('', '', 0, 0.0)
    naya_dhabi.naam=raw_input("Apne dhabi ka naam btao")
    gender = raw_input("chhora ya chhori?: ")
    if gender == "chhora":
        naya_dhabi.salutation = "Mr."
    elif gender == "chhori":
        naya_dhabi.salutation = "Ms."
    naya_dhabi.naam = naya_dhabi.salutation + " " + naya_dhabi.naam
    naya_dhabi.umra = int(raw_input("Umra batao?"))
    naya_dhabi.moolyankan = float(raw_input("Moolankan batao?"))
    if len(naya_dhabi.naam) > 0 and naya_dhabi.umra > 12 and naya_dhabi.moolyankan >= spy.moolyankan:
        dhabi.append(naya_dhabi)
        print "Friend Added!"
    else:
        print "Sorry! Invalid entry. We can\'t add spy with the details you provided"

    return len(dhabi)


# Function to select a friend
def select_friend():
    item_number = 0
    for friend in dhabi:
        print "%d. %s aged %d with rating %.2f is online" % (item_number + 1, friend.naam,
                                                             friend.umra,
                                                             friend.moolyankan)
        item_number = item_number + 1
    friend_choice = raw_input("Apne dosto mein se koi ek chunein")
    friend_choice_position = int(friend_choice) - 1

    return friend_choice_position


# Function to send a message
def send_a_message():
    choose_a_friend= select_friend()
    image=raw_input("Tasveer ka naam btao")
    output = "encoded.jpg"
    text = raw_input("Kya secret message daalna hai tasveer mein?")
    # 'Encode' function is used to encode a secret message in an image
    Steganography.encode(image, output, text)
    new_chat = ChatMessage(text, True)
    # Add the elements in the list
    dhabi[choose_a_friend].chats.append(new_chat)
    print "Secret message daal diya!"


# Function to read a message
def read_a_message():
    sender= select_friend()
    output=raw_input("Jis Tasveer mein message daalna hai uska naam bataiye?")
    secret_text = Steganography.decode(output)
    print secret_text
    if 0 < len(secret_text) < 100:
        new_chat = ChatMessage(secret_text, True)
        dhabi[sender].chats.append(new_chat)
    elif len(secret_text) > 100:
        print "Boht bol raha tha, Nikal diya G***u ko."
        del dhabi[sender]
    else:
        print "Koi message nahi hai iss image mein"
    for word in EMERGENCY_MESSAGES:
        if word == secret_text:
            print "dhabi musibat mein hai"
    print colored("Apka secret message save karr liya hai", "blue")


# Function to read chat history
def read_chat_history():
    read_for = select_friend()
    for chat in dhabi[read_for].chats:
        if chat.sent_by_me:
            print colored(chat.time.strftime("%d %B %Y"), "blue") + colored("you said:", "red") + chat.message
        else:
            print colored(chat.time.strftime("%d %B %Y"), "blue") ,
            (colored(dhabi[read_for].name),"red") + chat.message


# Function to define menu for spyChat
def start_chat(spy):
    print "Authentication complete. Welcome " + spy.naam + " age: " \
          + str(spy.umra) + " and rating of: " + str(spy.moolyankan) + " Proud to have you onboard"
    current_status_message=None
    show_menu = True

    while show_menu:
        menu_choices = "Kya karna chahte ho? \n 1. Status update karne ke liye 1 dabayein \n"\
                        "2. Dhabi daalne ke liye 2 dabayein \n"\
                        "3. Secret message bhejne ke liye 3 dabayein \n"\
                        "4. Secret message padhne ke liye 4 dabayein \n"\
                        "5. Kisi upyogkarta ki chat padhne ke liye 5 dabayein \n 6. Application band karein \n"
        menu_choice = raw_input(menu_choices)

        if len(menu_choice) > 0:
            menu_choice = int(menu_choice)

            if menu_choice == 1:
                spy.current_status_message = add_status()
            elif menu_choice == 2:
                number_of_friends = add_dhabi()
                print "You have %d friends" % (number_of_friends)
            elif menu_choice == 3:
                send_a_message()
            elif menu_choice == 4:
                read_a_message()
            elif menu_choice == 5:
                read_chat_history()
            else:
                show_menu = False


if existing == "Y":
    start_chat(spy)
elif existing == "N":
    spy.naam = raw_input("Apna naam batao?")
    if len(spy.naam) > 0:
        print "Welcome " + spy.naam + ". Glad to have you back with us."
        gender = raw_input("chhora ya chhori?: ")
        if gender == "chhora":
            spy.salutation = "Mr."
        elif gender == "chhori":
            spy.salutation = "Ms."
        spy.naam = spy.salutation + " " + spy.naam
        print "Alright " + spy.naam + ". I'd like to know a little bit more about you before we proceed..."
        spy.umra = 0
        spy.moolyankan = 0.0
        spy.is_online = False
        spy.umra = int(raw_input("Umra bata apni?"))
        if 12 < spy.umra < 50:
            spy.moolyankan = float(raw_input("Apna moolyankan batao?"))
            if spy.moolyankan > 4.5:
                print "Zabardast!"
            elif 3.5 < spy.moolyankan <= 4.5:
                print "Achha hai."
            elif 2.5 <= spy.moolyankan <= 3.5:
                print "Sahi hai par aur badhiya kar sakte ho"
            else:
                print "Ghatiya"
            spy.is_online = True
            start_chat(spy)

        else:
            print "Teri umra nhi hai iss application ko use karne ki"
    else:
        print "Khali na chhor. Naam bharde apna"
