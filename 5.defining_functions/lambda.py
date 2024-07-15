lambda_function = lambda x: x+1
def makeLambdaFunction():
    return lambda x: x+1

lambda_function2 = makeLambdaFunction()

print(lambda_function(1))
print(lambda_function2(1))