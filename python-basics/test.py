try:
    i = 0
    while(i<10):
        print(i)
        if i == 5:
            # break
            raise Exception("Value is equal to 5")
        i = i + 1
except Exception as e:
    print("Something went wrong : ", e)
else:
    print("No exception, no error")
finally:
    print("Code execution complete")
