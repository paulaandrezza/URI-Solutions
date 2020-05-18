while True:
  try:

    linha1 = input().split()

    a, b = linha1

    print(abs(int(b)-int(a)))

  except EOFError:
    break