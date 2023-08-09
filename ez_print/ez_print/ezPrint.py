class clnArray(object):
  def __init__(self, array):
    for x in array: 
        print("•" + array.at[x] + "\n")

class println(object):
  def __init__(self, text):
        print(text + "\n")

class onwithln(object):
  def __init__(self, text):
        print("\n" + text + "\n")

class onln(object):
  def __init__(self, text):
        print("\n" + text)

class boolAsBin(object):
    def __init__(self, text):
      if text == True: 
        print(1)
      elif text == False:
         print(0)
      else:
         print("Recieved boolean is not True nor False.")

class boolAsBinwithln(object):
    def __init__(self, text):
      if text == True: 
        print("1\n")
      elif text == False:
         print("0\n")
      else:
         print("Recieved boolean is not True nor False.")

class boolAsBinonln(object):
    def __init__(self, text):
      if text == True: 
        print("\n1")
      elif text == False:
         print("\n0")
      else:
         print("Recieved boolean is not True nor False.")

class boolAsBinonwithln(object):
    def __init__(self, text):
      if text == True: 
        print("\n1\n")
      elif text == False:
         print("\n0\n")
      else:
         print("Recieved boolean is not True nor False.")