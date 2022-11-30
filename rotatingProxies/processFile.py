with open("proxy-list.txt", "r") as f:
    with open("output.txt", "w") as fh:
        for line in f:
            l1 = line.split()
            fh.write(l1[0]+"\n")
    fh.close()
    f.close()
