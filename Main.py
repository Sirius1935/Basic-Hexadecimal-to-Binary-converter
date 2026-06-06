#Setup Section
Mode = "Not Set"

#Main Code
print("Welcome to the Hexadecimal and Binary Converter!")
print("Would you like to convert Hexadecimal values to Binary values or Binary values to Hexadecimal values?")
print(' Type "1", "One", "Mode 1", "Mode One", "Hexadecimal to Binary", "Hex to Bin", "Hexadecimal to Bin" or "Hex to Binary" to convert Hexadecimal to Binary.')
print(' Type "2", "Two", "Mode 2", "Mode Two", "Binary to Hexadecimal", "Bin to Hex", "Binary to Hex" or "Bin to Hexadecimal" to convert Binary to Hexadecimal.')
Mode = input("")
while True:
 if Mode.lower() in ["1", "one", "mode 1", "mode one", "hexadecimal to binary", "hex to bin", "hexadecimal to bin", "hex to binary"]:
  print("Please, enter the Hexadecimal value you want to convert to Binary.")
  HexadecimalValue = input("").upper()
  BinaryValue = bin(int(HexadecimalValue, 16))[2:]
  print(f"The inputted Hexadecimal value is 0x{HexadecimalValue}")
  print(f"The Binary value is {BinaryValue}")
 elif Mode.lower() in ["2", "two", "mode 2", "mode two", "binary to hexadecimal", "bin to hex", "binary to hex", "bin to hexadecimal"]:
  print("Please, enter the Binary value you want to convert to Hexadecimal.")
  BinaryValue = input("")
  HexadecimalValue = hex(int(BinaryValue, 2))[2:].upper()
  print(f"The inputted Binary value is {BinaryValue}")
  print(f"The Hexadecimal value is 0x{HexadecimalValue}")
 else:
  print("Invalid Mode, Please Try Again")
  Mode = input("Enter Mode: ")