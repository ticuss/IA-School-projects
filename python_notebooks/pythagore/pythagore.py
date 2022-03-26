import numpy as np
import errors

demande_a = True
maxNumber = 10
minNumber = 1e-20


def pythagore():
    hypotenuse = 0
    while demande_a:
        try:
            firstInput = int(input("\n Enter the value of firstInput: "))
            verifyNumber(firstInput)
            secondInput = int(input("\n Enter the value of secondInput: "))
            verifyNumber(secondInput)
            hypotenuse = np.sqrt(firstInput ** 2 + secondInput ** 2)

        except errors.NegativeValue:
            print("Please enter a positive number")
            continue

        except errors.ValueTooLargeError:
            print("Please enter a smaller number")
            continue

        except errors.ValueTooSmallError:
            print("Please enter a bigger number")
            continue

        except errors.ValueComplexError:
            print("Please enter a non-complex number")
            continue
        except errors.ValueStrError:
            print("Please enter a number")
            continue
        except ValueError:
            continue

        else:
            break

    return print("\n Hypotenuse = ", hypotenuse)


def verifyNumber(input):
    if type(input) != int and np.iscomplex(input) != False:
        raise ValueError("haha")
    elif input < 0:
        raise errors.NegativeValue
    elif input > maxNumber:
        raise errors.ValueTooLargeError
    elif input < minNumber:
        raise errors.ValueTooSmallError
    elif type(input) == str:
        raise errors.ValueStrError
    elif np.iscomplex(input):
        raise errors.ValueComplexError
    else:
        return input


pythagore()
