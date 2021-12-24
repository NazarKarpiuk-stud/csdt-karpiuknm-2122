with open("proj_logs.log", "r") as fin:
    print("[LAST FIVE LOG RECORDS]")
    for line in fin.readlines()[-6:]:
        print(line, end="")
