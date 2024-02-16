from time import sleep
print("goodbye world")
sleep (5)
goodbye = 1
answer = 2
timer = 2
while goodbye == 1:
    answer *= 2
    print(answer)
    sleep(timer)
    if timer >= 0:
        timer -= 0.1