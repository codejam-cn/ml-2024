class Round:

    def __init__(self, r):
        self.r = r

    def check(self, p, q):
        if p ** 2 + q ** 2 <= self.r ** 2:
            return True
        else:
            return False


round = Round(1)

CAPACITY = 100

total = 0
inCircle = 0

for x in range(-CAPACITY, CAPACITY):
    for y in range(-CAPACITY, CAPACITY):

        total = total + 1
        x1 = x / CAPACITY
        y1 = y / CAPACITY
        check = round.check(x1, y1)
        if True == check:
            inCircle = inCircle + 1
            #print("count =" + str(count) + "\t x1=" + str(x1) + "\t y1=" + str(y1) + "\t" + str(check))

        # print("count =" + str(count) + "\t x1=" + str(x1) + "\t y1=" + str(y1) + "\t" + str(check))

print("圆周率 = " + str(inCircle * 4 / (total)))
