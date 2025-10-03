def isPalindrome(n):
    reverse = 0

    temp = abs(n)
    while temp != 0:
        reverse = (reverse * 10) + (temp % 10)
        temp = temp // 10

    return (reverse == abs(n))
