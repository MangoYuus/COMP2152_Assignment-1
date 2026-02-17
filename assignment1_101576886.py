"""
Author: <YuQing Lin>
Assignment: #1
"""
# -------------------------------------
# Step b: Create 4 variables
#gym_member: string
gym_member = "Alex Alliton"

#preferred_weight_kg: float
preferred_weight_kg = 20.5

#highest_reps: int
highest_reps = 25

#membership_active: bool
membership_active = True
# -------------------------------------
# Step c: Create a dictionary named workout_stats
#dictionary -> key(str) : value(tuple of 3 int)
workout_stats = {
    "Alex":(30,45,20),
    "Roy":(20,80,40),
    "Simon":(20,60,80),
}
# -------------------------------------
# Step d: Calculate total workout minutes using a loop and add to dictionary
print("\n" + "=" * 60)
print("Step D: Add total workout time to the dictionary")
print("=" * 60)

for friend, minutes in list(workout_stats.items()):
    total_time = (minutes[0]+minutes[1]+minutes[2])
    workout_stats[friend + "_Total"] = total_time
print(workout_stats)

# -------------------------------------
# Step e: Create a 2D nested list called workout_list
print("\n" + "=" * 60)
print("Step E: Create a 2D nested list called workout_list")
print("=" * 60)

# =======================================================
# 本部分添加活动的名字用以美观输出，同样作用后续step：
# =======================================================
workout_list = []
names = []
for friend, minutes in list(workout_stats.items()):
    if "_Total" not in friend:
        workout_list.append(list(minutes))
        names.append(friend)


activity_name = ["Yoga", "Running", "Weightlifting"]
for i in range(len(workout_list)):
    print(names[i] + ": (mins)")
    for j in range(len(workout_list[i])):
        print(activity_name[j] , "-", (workout_list[i][j]))
    print("\n")
print(workout_list)
# -------------------------------------

# Step f:Slice the workout_list
print("\n" + "=" * 60)
print("Step F: Slice the workout_list")
print("=" * 60)
#Slice 1
print("\n" + "-" * 55)
print(" Slice 1 - All workout time for yoga and running (min): ")
print("-" * 55)

for i in range(len(workout_list)):
    print(names[i] + ":", "Yoga =", workout_list[i][0], "Running =", workout_list[i][1])

#Slice 2
print("\n" + "-" * 55)
print(" Slice 2 - The weightlifting for the last two friends(min):")
print("-" * 55)

for i in range(-2,0):
    print(names[i]+":", "Weightlifting =", workout_list[i][2])
# -------------------------------------

# Step g: Check if any friend's total >= 120
print("\n" + "=" * 60)
print("Step G: SCheck if friend's Total Workout Time enough (2h)")
print("=" * 60)

for friend, total_time in list(workout_stats.items()):
    if "_Total" in friend:
        if total_time >= 120:
            friend_name = friend.split("_Total")[0]
            print(f"Great job staying active, <{friend_name}> !")
# -------------------------------------
# Step h: User input to look up a friend
print("\n" + "=" * 60)
print("Step H:Look Up Your Friend")
print("=" * 60)

name = input("Your Friend's name? (Case sensitive) \n")
if name in names:
    i = names.index(name)
    print(f"Here are your friend, <{name}>'s workout data: \n")
    print("-" * 25 )
    for j in range (3):
        print(activity_name[j] + ":", workout_list[i][j])
    print ("Total Workout Time: ", workout_stats[name + "_Total"])
    print("-" * 25 + "\n")
else:
    print("-" * 40)
    print(f"Friend <{name}> not found in the records.")
    print("-" * 40)
# -------------------------------------
# Step i: Friend with highest and lowest total workout minutes
print("\n" + "=" * 60)
print("Step I: Friend with highest/lowest total workout minutes")
print("=" * 60)

total_time = {}
for friend, minutes in list(workout_stats.items()):
    if "_Total" in friend:
        friend_name = friend.split("_Total")[0]
        total_time[friend_name] = minutes
max_friend = max(total_time, key=total_time.get)
min_friend = min(total_time, key=total_time.get)
print(f"Longest total Workout time: <{max_friend}> Well Done!")
print(f"Shortest total workout time: <{min_friend}> Keep it Up !!")