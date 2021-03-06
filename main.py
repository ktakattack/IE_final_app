from peer import Peer
from message import Message
from resolution import Resolution

AS1=Peer("AS1")
AS2=Peer("AS2")
Client=Peer("Client")
RS=Peer("RS")

def main():
    print("main is running")

#Client (Request C1) -> 
    M1 = Message("request", "Client", "RS", list(RS.ResourceVault.keys())[0], list(Client.PolicyVault.keys())[0])

    Client.Send_Message(M1, RS)
    RS.Receive_Message(M1, Client)

# RS (Request C2, C3) -> 
# Client (Request C2) -> 
# AS1 (Offer C2 Resource) -> 
# Client (Request C3) -> 
# AS2 (Request C4) -> 
# Client (Offer C4 Resource) -> 
# AS2 (Offer C3 Resource) -> 
# Client (Offer C2/C3 Resources) ->
# RS (Offer C1 Resource) -> 
# Client (Received Requested C1 Resource, done)

if __name__ == '__main__':
    main()
