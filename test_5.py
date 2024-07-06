import sys

def main():
    # Print the number of arguments passed (excluding the script name itself)
    print(f"Number of arguments: {len(sys.argv) - 1}")

    # Print all arguments passed
    if len(sys.argv) > 1:
        print("Arguments:")
        for i, arg in enumerate(sys.argv[1:], start=1):
            print(f"  {i}. {arg}")
    else:
        print("No arguments provided.")

if __name__ == "__main__":
    main()



'''
to test code write in terminal python test_5.py arg_1 arg_2 .....    +enter

'''