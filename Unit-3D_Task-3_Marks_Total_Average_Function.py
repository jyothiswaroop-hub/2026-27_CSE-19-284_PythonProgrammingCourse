def total_and_average(Subject_1,Subject_2,Subject_3):
    tot = Subject_1+Subject_2+Subject_3
    avg = tot / 3
    return tot,avg

m1, m2, m3 = 70,25,60
total, average = total_and_average(m1, m2, m3)
print("Total:", total)
print("Average:", average)
