from dataclasses import dataclass

@dataclass
class Message:
    Id: int
    SenderId: str
    ReceiverId: str
    Content: str
    IsRead: bool = False


    # Hydrates a Message entity using a pyrebase response value and returns it.
    def HydrateMessage(message):
        return Message(
            Id = MessageHydrator.HydrateProp(message, "Id"),
            SenderId = MessageHydrator.HydrateProp(message, "SenderId"),
            ReceiverId = MessageHydrator.HydrateProp(message, "ReceiverId"),
            Content = MessageHydrator.HydrateProp(message, "Content"),
            IsRead = MessageHydrator.HydrateProp(message, "IsRead")
        )

class MessageHydrator:

    # A dictionary to maintain the Message entity's property name (key) and its type (value).
    _messageAttributes: dict[str, str] = {
        "Id": "int",
        "SenderId": "str",
        "ReceiverId": "str",
        "Content": "str",
        "IsRead": "bool"
    }


    # Hydrates an individual property for the Message entity.
    def HydrateProp(message, prop: str):
        if prop not in MessageHydrator._messageAttributes.keys():
            raise Exception(f"Property {prop} not defined for entity: Message")
        
        propType: str = MessageHydrator._messageAttributes.get(prop)
        value = None
        
        try:
            value = MessageHydrator.Cast(message.val()[prop], propType)
        except:
            value = MessageHydrator.GetDefaultValue(prop)
        
        if value == None: raise Exception(f"Could not hydrate prop: {prop} for Message")
        
        return value


    # Handles conversion to a certain type.
    def Cast(pyreValue, propType):
        if propType == "bool":
            return eval(pyreValue)
        
        return pyreValue

    # Gets the default value for a property on the Message entity based on its type.
    def GetDefaultValue(prop: str):
        propType: str = MessageHydrator._messageAttributes.get(prop)

        if propType == "int": return 0
        if propType == "str": return ""
        elif propType == "bool": return False
        else: return None
