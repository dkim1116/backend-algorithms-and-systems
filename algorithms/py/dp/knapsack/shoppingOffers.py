# In LeetCode Store, there are n items to sell. Each item has a price. 
# However, there are some special offers, and a special offer consists of one or more different kinds of items with a sale price.
# You are given an integer array price where price[i] is the price of the ith item, 
# and an integer array needs where needs[i] is the number of pieces of the ith item you want to buy.
# You are also given an array special where special[i] is of size n + 1 
# where special[i][j] is the number of pieces of the jth item in the ith offer and special[i][n] 
# (i.e., the last integer in the array) is the price of the ith offer.
# Return the lowest price you have to pay for exactly certain items as given, where you could make optimal use of the special offers. 
# You are not allowed to buy more items than you want, even if that would lower the overall price. 
# You could use any of the special offers as many times as you want.

# Example 1:

# Input: price = [2,5], special = [[3,0,5],[1,2,10]], needs = [3,2]
# Output: 14
# Explanation: There are two kinds of items, A and B. Their prices are $2 and $5 respectively. 
# In special offer 1, you can pay $5 for 3A and 0B
# In special offer 2, you can pay $10 for 1A and 2B. 
# You need to buy 3A and 2B, so you may pay $10 for 1A and 2B (special offer #2), and $4 for 2A.

class Solution:
    def shoppingOffers(self, price: List[int], special: List[List[int]], needs: List[int]) -> int:
        # price = [2,5]
        # needs = [3,2]
        # special = [
                # [3,0,5],
                # [1,2,10]]
        memo = {}
        def dfs(currNeeds, memo):
            # Keep track of already computed needs to optimize for computing different branches of needed options
            if tuple(currNeeds) in memo:
                return memo[tuple(currNeeds)]
            minCost = 0

            # Try paying for each item individually without offer
            for i in range(len(currNeeds)):
                minCost += price[i] * currNeeds[i]

            # Try using specials
            for offer in special:
                newNeeds = []
                valid = True

                # When current offer usage exceeds the count of any menu items, skip
                for i in range(len(currNeeds)):
                    if offer[i] > currNeeds[i]:
                        valid = False
                        break
                    newNeeds.append(currNeeds[i] - offer[i])
                
                # If its valid, then with remaining needed items, recurse
                if valid:
                    minCost = min(minCost, offer[-1] + dfs(newNeeds, memo))
            memo[tuple(currNeeds)] = minCost
            return minCost
        return dfs(needs, memo)