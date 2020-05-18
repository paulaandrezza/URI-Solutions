while True:
  try:

    v, t = input().split()

    s = 2 * int(v) * int(t)

    print("%d" %s)

  except EOFError:
    break