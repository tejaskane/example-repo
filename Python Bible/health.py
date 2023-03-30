import random
health = 50
difficulty = 1
# print("before portion {}".format(health))
portion_health=random.randint(25,50)/difficulty
health=health+portion_health
print("after portion in easy mode : {}".format(int(health)))
health = 50
difficulty = 2
portion_health=random.randint(25,50)/difficulty
health=health+portion_health
print("after portion in medium mode : {}".format(int(health)))
health = 50
difficulty = 3
portion_health=random.randint(25,50)/difficulty
health=health+portion_health
#here we use f string format
print(f"after portion in hard mode : {int(health)}")
