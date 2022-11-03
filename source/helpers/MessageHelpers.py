from helpers.UserHelpers import UserHelpers
from model.Message import Message
from firebaseSetup.Firebase import database
from model.User import User

class MessageHelpers:
    
    # Converts a message entity into a dictionary.
    def MessageToDict(message: Message) -> dict:
        return {
            'Id': str(message.Id),
            'SenderId': str(message.SenderId),
            'ReceiverId': str(message.ReceiverId),
            'Content': str(message.Content),
            'IsRead': str(message.IsRead)
        }


    # Checks if the specified message exists in the DB using the provided ID.
    def MessageExists(messageId: int, collection = "Messages") -> bool:
        return False if MessageHelpers.GetMessageById(
            messageId, collection) == None else True


    # Creates a message id which is essentially its index.
    # Example: If total messages => 4 then messageId => 5.
    def CreateMessageId(collection = "Messages") -> int:
        allMessages: list[Message] = MessageHelpers.GetAllMessages(collection)
        if allMessages == None: return 0

        return len(allMessages)


    # Gets a PyreResponse of all messages from the DB and returns
    # a list of message entities after constructing it.
    def GetAllMessages(collection = "Messages") -> list[Message]:
        try:
            messagesResponse = database.child(collection).get()
            if messagesResponse == None: return None

            messagesResponseList: list = messagesResponse.each()
            if (messagesResponseList == None): return None

            messages: list[Message] = []
            for message in messagesResponseList:
                if message == None: continue
                else: messages.append(Message.HydrateMessage(message))

            return messages

        except:
            return None


    # Gets a specific Message from the database based on the Message ID provided.
    def GetMessageById(messageId: int, collection = "Messages") -> Message:
        try:
            message: Message = Message.HydrateMessage(
                database.child(collection).child(messageId).get())
            
            if message == None: raise Exception()

            return message

        except Exception as e:
            print(f"Could not get the specified message with ID: {messageId}\n{e}")
    

    # Deletes a specific Message from the database based on the Message ID provided.
    def DeleteMessageById(messageId: int, collection = "Messages") -> bool:
        try:
            if not MessageHelpers.MessageExists(messageId, collection):
                return False
            
            database.child(collection).child(messageId).remove()
            return True

        except:
            return False


    # Creates or updates the specified message in the DB.
    # Returns true if update was successful else false.
    def UpdateMessage(message: Message, collection: str = "Messages") -> bool:
        try:

            # Sanity check.
            receiverExists: bool = UserHelpers.UserExists(message.ReceiverId)
            if not receiverExists:
                print("\nCould not send a message to the specified user because"
                    + "the user no longer exists.")
                return False

            database.child(collection).child(message.Id).set(
                MessageHelpers.MessageToDict(message))
            
            return True

        except Exception as e:
            print(f"Could not update message with ID: {message.Id}\n{e}")
            return False
    

    # Gets all the received messages of the specified user.
    def GetAllReceivedMessages(
        userId: str,
        onlyUnread: bool = False,
        userCollection = "Users",
        messageCollection = "Messages") -> list[Message]:

        if not UserHelpers.UserExists(userId, userCollection):
            print(f"Specified user does not exist in collection: {userCollection}")
            return None
        
        allMessages: list[Message] = MessageHelpers.GetAllMessages(messageCollection)
        if allMessages == None: return None

        # Filter all messages where the receiver id is equal to the specified user id.
        allMessagesReceived: list[Message] = list(filter(
            lambda m: m.ReceiverId == userId, allMessages))
        
        if onlyUnread:
            allMessagesReceived = list(filter(
                lambda m: m.ReceiverId == userId and not m.IsRead, allMessages))

        return allMessagesReceived


    # Displays a message and updates its status to read.
    def DisplayMessage(
        message: Message,
        userCollection = "Users",
        messageCollection = "Messages"):
        
        sender: User = UserHelpers.GetUserById(message.SenderId, userCollection)
        receiver: User = UserHelpers.GetUserById(message.ReceiverId, userCollection)

        print("===============================================")

        print(f"\nFrom: {sender.FirstName} {sender.LastName}"
            + f"\nTo: {receiver.FirstName} {receiver.LastName}"
            + f"\n\nContent:\n{message.Content}\n")

        print("===============================================")
        
        message.IsRead = True
        MessageHelpers.UpdateMessage(message, messageCollection)
