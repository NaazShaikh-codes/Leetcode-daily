class Solution(object):
    def minimumCost(self, cost1, cost2, costBoth, need1, need2):
        cost_a = (need1 * cost1) + (need2 * cost2) 
        common = min(need1, need2)
        cost_b = (common * costBoth) + ((need1 - common) * cost1) + ((need2 - common) * cost2) 
        cost_c = max(need1, need2) * costBoth
        return min(cost_a, cost_b, cost_c)