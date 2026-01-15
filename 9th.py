dic={"Alice":85,"Mukesh":72,"Rakesh":82,"Ridhima":86}

name=input("Enter teh student's name:")

if name in dic:
    print(dic[name])
else:
    print("Student not found.")