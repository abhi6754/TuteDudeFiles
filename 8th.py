txt1=input("Enter text to write to file:")
with open("output.txt","w") as fh:
    fh.write(txt1 + "\n")
print("Data successfully written to output.txt")

txt2=input("Enter additional text to append:")
with open("output.txt","a") as fh:
    fh.write(txt2 + "\n")
print("File successfully appended to output.txt")

print("Final content of output.txt")
with open("output.txt","r") as fh:
    print(fh.read())