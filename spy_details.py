from datetime import datetime
class Spy:

    def __init__(self, naam, salutation, umra, moolyankan):
        self.naam = naam
        self.salutation = salutation
        self.umra = umra
        self.moolyankan = moolyankan
        self.is_online = True
        self.chats = []
        self.current_status_message = None
class ChatMessage:

    def __init__(self,message,sent_by_me):
        self.message = message
        self.time = datetime.now()
        self.sent_by_me = sent_by_me

spy = Spy('Mayank', 'Mr.', 24, 4.2)

friend_one = Spy('Neeraj', 'Mr.', 4.9, 20)
friend_two = Spy('Saurabh', 'Mr.', 4.39, 21)
friend_three = Spy('Vivek', 'Mr.', 4.95, 23)

dhabi= [friend_one, friend_two, friend_three]