def kilo_to_pounds(kilos):
    # This statement intentionally has an error. 
# Main part of the program starts here. Do not remove the line below.
    return kilos * 2.204
if __name__ == '__main__':
    kilos = float(input())
    pounds = kilo_to_pounds(kilos)
    print(f'{pounds:.3f} lbs')