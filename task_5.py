
def getDescentPeriods(prices):
        ans = dp = 1
        for i in range(1, len(prices)):
            if prices[i] == prices[i - 1] - 1:
                dp = dp + 1
            else:
                dp = 1
            ans = ans + dp
        return ans
