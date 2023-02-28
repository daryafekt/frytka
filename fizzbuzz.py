y=0
for x in range(1,101):
  if int(x)%3==0:
     print("Fizz")
     y=y+1
  elif x%5==0:
    print("Buzz")
  else: print(x)
  if x%15==0:
    print("FizzBuzz")
print(x)
print(y, "liczby podzilne przez 3")

