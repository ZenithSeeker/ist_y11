

def main():
    nameList = ["Andsf", "Royal","Lillia","Jaymie","Jinne", "kelly"]
    createFileFromArray(nameList)
    print("Processing complete")
def createFileFromArray(items):
    with open("name.txt","a") as f:
        for item in items:
            f.writelines(item + "\n")


main()