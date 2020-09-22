from stegano import lsb

def help() :
    print("welcome to help")
    print("Enter 'encode' to encode a message in an image")
    print("Enter decode to decode a message from your image")

while True :
    choice = input("Enter what you want to do : ")

    if choice == "encode" :
        image = input("path/to/your/image.png : ")
        message = input("Enter the message to encode : ")
        msg = lsb.hide(image, message)
        msg.save(image)
        print("Encoded successfully")

    elif choice == "decode" :
        image2 = input("path/to/your/image.png : ")
        act_msg = lsb.reveal(image2)
        print(f"The decode message is : {act_msg}")
    elif choice == "quit" :
        break
    else:
        print("Sorry i don't recognise your command")


