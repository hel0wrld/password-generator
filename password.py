import random
import string
l_letters = list(string.ascii_lowercase)
u_letters = list(string.ascii_uppercase)
spec_char = ['!','@', '#', '$', '%', '^', '&', '*']
num = [x for x in range(0,10)]
sizes = [0]*4
sizes[0] = 5 # number of lower case characters
sizes[1] = 1 # number of upper case characters 
sizes[2] = 5 # number of special characters
sizes[3] = 3 # number of digits 
passw = random.sample(l_letters, k=sizes[0]) + random.sample(u_letters, k=sizes[1])
passw = passw + random.sample(spec_char, k=sizes[2]) + random.sample(num, k=sizes[3])
random.shuffle(passw) # randomize the characters
passw = ''.join(map(str,passw))
print(passw)
