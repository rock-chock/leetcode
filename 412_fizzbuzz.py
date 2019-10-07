"""
https://leetcode.com/problems/fizz-buzz/
Write a program that outputs the string representation of numbers from 1 to n.
But for multiples of three it should output “Fizz” instead of the number and
for the multiples of five output “Buzz”. For numbers which are multiples of
both three and five output “FizzBuzz”.
"""

def main():
    n = 30
    res = fizzbuzz(n)
    for i in res:
        print(i)

def fizzbuzz(n):

    r =[]

    for i in range(1, n+1):

        div_by_3 = (i % 3 == 0)
        div_by_5 = (i % 5 == 0)

        if div_by_3 and div_by_5:
            r.append('FizzBuzz')
        elif div_by_3:
            r.append('Fizz')
        elif div_by_5:
            r.append('Buzz')
        else:
            r.append(str(i))
    return r


if __name__ == "__main__":
    main()
