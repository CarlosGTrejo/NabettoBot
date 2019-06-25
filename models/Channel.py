from models.Gate import sendMessage

def joinChannel(gate):
    buffer = ""
    Loading = True

    while Loading:
        buffer = buffer + gate.recv(1024).decode()
        tmp = buffer.split("\n")
        buffer = tmp.pop()

        for line in tmp:
            print(line)
            
            if ("End of /NAMES list" in line):
                Loading = False
    
    else: # ⬇️ When done loading ⬇️
        
        sendMessage(gate, "Successfully joined channel.")
        
