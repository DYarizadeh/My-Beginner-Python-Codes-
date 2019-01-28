Class = {}
while True:
    name = input("Enter Students name and press Enter to stop: ")
    if name == '':
        break
    score = int(input("Enter student's score (0-10): "))
    if name in Class:
        Class[name] += (score,)
    else:
        Class[name] = (score,)
for name in sorted(Class.keys()):
    sum=0
    cnt=0
    for score in Class[name]:
        sum += score
        cnt += 1
    print(name, ":", sum/cnt)
