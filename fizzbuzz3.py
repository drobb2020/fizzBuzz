for i in range(1, 101):

  output = 'Fizz' if i%3 == 0 else ""
  output += "Buzz" if i%5 == 0 else ""

  print(i) if output == "" else print(output)

  