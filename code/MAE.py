from code.main import slope , intercept , X , Y
Error = 0
for i in range(len(Y)):
    predicted_y = slope*X + intercept
    Error = Error + abs(predicted_y - Y[0])
    
Error = Error / Y.size()



