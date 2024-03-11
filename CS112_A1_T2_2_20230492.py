# File: CS112_A1_T2_2_20230492.py
# Purpose: Try to reach 15 first
# Author: Youssef Hassan Fahmy Ahmed
# ID: 20230492

def inputValid(num1, numm, num):
    # Validate input
    while not (num1 in numm):
        print("Enter a number from: ", end='')
        for i in numm:
            print(i, end=' ')
        print()
        num1 = int(input())

    num.append(num1)
    del nums[nums.index(num1)]


def displayNums(nums):
    for i in nums:
        print(i, end=' ')
    print()


def checkWinner(num1, num2):
    # Check if Player 1 or Player 2 has reached 15
    if len(num1) >= 3 or len(num2) >= 3:
        vl1 = False
        for x in range(len(num1)):
            for i in range(x + 1, len(num1)):
                for h in range(i + 1, len(num1)):
                    if num1[h] + num1[i] + num1[x] == 15:
                        vl1 = True

        vl2 = False
        for x in range(len(num2)):
            for i in range(x + 1, len(num2)):
                for h in range(i + 1, len(num2)):
                    if num2[h] + num2[i] + num2[x] == 15:
                        vl2 = True

        if vl1 or vl2:
            print("Numbers of player 1: ", end='')
            displayNums(num1)
            print("Numbers of player 2: ", end='')
            displayNums(num2)

        if vl1:
            print("Player 1 won", end='')
            exit()
        elif vl2:
            print("Player 2 won", end='')
            exit()


# Declaring an array of valid inputs
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
nums1 = []
nums2 = []

while len(nums) > 0:
    # Player 1's turn
    print("Player 1: Enter a number from: ", end='')
    displayNums(nums)
    inputValid(int(input()), nums, nums1)

    # Check if Player 1 or Player 2 has reached 15
    checkWinner(nums1, nums2)

    if len(nums) == 0:
        break

    # Player 2's turn
    print("Player 2: Enter a number from: ", end='')
    displayNums(nums)
    inputValid(int(input()), nums, nums2)

    # Check if Player 1 or Player 2 has reached 15
    checkWinner(nums1, nums2)

# Display results
displayNums(nums1)
displayNums(nums2)
print("Draw", end='')
