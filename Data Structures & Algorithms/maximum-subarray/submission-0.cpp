class Solution {
public:
    int maxSubArray(vector<int>& nums) {
        int sum = nums[0];
        for (int i = 0; i < nums.size(); i++)
        {
            int currentSum = 0;
            for (int j = i; j < nums.size(); j++)
            {
                currentSum += nums[j];

                if (currentSum > sum)
                {
                    sum = currentSum;
                }

            }
            
        }

        return sum;

    }
};
