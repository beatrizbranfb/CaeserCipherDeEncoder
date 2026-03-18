#Base
code = input(str("Your encripted code: "))
letters = "abcdefghijklmnopqrstuvwxyz"

pos = []
for i in range(26):
    trying = ""
    for char in code.lower():
        if char in letters:
            pos_used = letters.find(char)
            new_pos = (pos_used - i) % 26
            trying += letters[new_pos]
        else:
            trying += char
            
    pos.append(f"Possibility{i}: {trying}")

for p in pos:
    print(p)
        

            
    
        
    