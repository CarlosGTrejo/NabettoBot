from models.Connection import sendMessage

def joinChannel(connection):
    buffer = ""
    Loading = True

    while Loading:
        buffer = buffer + connection.recv(1024).decode()
        tmp = buffer.split("\n")
        buffer = tmp.pop()

        for line in tmp:
            print(line)
            
            if ("End of /NAMES list" in line):
                Loading = False

    else: # ⬇️ When done loading ⬇️
        print("[+] Successfully joined channel.\n".ljust(60,'='))
        
        # sendMessage(gate, "Successfully joined channel.")
