# timestamp is three numbers: a number of hours, minutes and seconds.
# Given two timestamps, calculate how many seconds is between them. The
# moment of the first timestamp occurred before the moment of the second
# timestamp. (6, 1, 30, 6, 2, 10 result 40 sec.)

num_hours1 = int(input())
num_min1 = int(input())
num_sec1 = int(input())
num_hours2 = int(input())
num_min2 = int(input())
num_sec2 = int(input())

print(((num_hours2-num_hours1)*3600)+((num_min2-num_min1)*60)+(num_sec2-num_sec1))