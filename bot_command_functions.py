

def check_for_gambler(name):
    name = name.lower()
    with open("gamblers.txt","r") as f:
        for line in f:
            if line.find(name,0,len(name) - 1):
                return True,line.split(":")
    return False

def create_gambler(name):
    name = name.lower() 
    if not check_for_gambler(name):
        with open("gamblers.txt","a") as f:
            f.write(f'\n{name}:1000')
            return
    print("already exists!")
    return get_gamblers_money(name)

def get_gamblers_money(name):
    name = name.lower()
    with open("gamblers.txt","r") as f:
        for line in f:
            if line.find(name,0,len(name) - 1):
                ls = line.split(":")
                return ls[1]
    return False

def change_gamblers_money(name):
    name = name.lower()
    gam_line = []
    with open("gamblers.txt","r") as f:
        for line in f:
             if line.find(name,0,len(name) - 1):
                gam_line = line.split(":")
                gam_line[1].replace("\n", "")
                print(gam_line)


print(create_gambler("lol"))

print(change_gamblers_money("lol"))
