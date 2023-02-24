def stopwatch():
    
    from time import sleep

    time = [0, 0, 0]

    for z in range(12):
        for i in range(60):
            for x in range(60):

                sleep(1)
                time[2] += 1

                if time[2] > 59:
                    time[2] = 0;
                    time[1] += 1

                if time[1] > 59:
                    time[1] = 0;
                    time[0] += 1

                if time[0] > 11:
                    time[0]=0

                display(time)

print("Stopwatch")

def display(time):
    text = ""
    count = 0
    for x in time:
        if x <= 9:
            text += "0" + str(x)
        else:
            text += str(x)

        count += 1

        if count <= 2:
            text += ":"

    print(text)
    
stopwatch()