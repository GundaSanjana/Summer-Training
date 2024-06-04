'''Take a number.Add the digits of it until u get a single digit number.
Check whether that single digit is prime or not. If it is prime print
it.Else check for next number and so on until u get a single digit
prime number.
Ex1:538=5+3+8=16=>1+6=7 7 is prime.
Ex2:537=5+3+7=15=>1+5=6,
    538=5+3+8=16=>1+6=7 7 is prime.(go to next number)'''

'''class AddDigitsPrime:
    def addDigitsUntilSingleDigit(self, num: int) -> int:
        while num >= 10:
            sum_digits = 0
            while num > 0:
                sum_digits += num % 10
                num //= 10
            num = sum_digits
        return num
    
    def isPrime(self, num: int) -> bool:
        if num < 2:
            return False
        for i in range(2, num):
            if num % i == 0:
                return False
        return True
    
    def findSingleDigitPrime(self, num: int) -> (int, int):
        while True:
            single_digit = self.addDigitsUntilSingleDigit(num)
            if self.isPrime(single_digit):
                return num, single_digit
            num += 1

if __name__ == "__main__":
    adp = AddDigitsPrime()
    num = int(input("Enter a number: "))
    result_num, single_digit_prime = adp.findSingleDigitPrime(num)
    print(f"The number {result_num} gives the single-digit prime number {single_digit_prime}")'''



def add(n):
    s=0
    while(n):
      s=s+(n%10)
      n=n//10
    return s
def pnp(x):
    if(n in [2,3,5,7]):
        return m
    else:
        return m+1
while():
    if(n<10):
        m=pnp(n)
    else:
        while(1):
            n=add(n)
            if(n<10):
                break
        print(pnp(n))
n=int(input())
m=n
print(result(pnp(n)))
    
#m=sum(list(map(int,list(n)))) code for sum of digits




