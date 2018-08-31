print("This is the scratch program")


def tester(verbose=False):
    if verbose:
        print("Verbose is on")
    print("Verbose is", verbose, "\n")
    return True



if __name__ == "__main__":
    print("scratch is the the main file")
    tester(verbose=True)
    tester()
else:
    print("scratch.py is being called from another program")





