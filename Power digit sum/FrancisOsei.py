def powerDigitSum(power):
    sum = 0
    result_power = pow(2, power)
    for x in str(result_power):
        sum += int(x)
    return sum


if __name__ == '__main__':
    print(powerDigitSum(15))  # This is the output of 26
    print(powerDigitSum(1000))  # Output for 1000

