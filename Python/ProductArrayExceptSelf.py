    """
    Given an array nums of n integers where n > 1,  
    return an array output such that output[i] is equal to the product of all the elements of nums except nums[i].
    """
    def productExceptSelf(nums):
        
        output = [0] * len(nums)
        # if the array has more than one zero, all the products = zero
        total_zeros = 0
        for num in nums:
            if num == 0:
                total_zeros += 1
        if total_zeros > 1:
            return output
        
        # calculate the product of all the numbers
        product_all = 1        
        for num in nums:
            if num != 0:
                product_all *= num

        # divide the product by each element, if there is one zero in the array the output is zero for all the elements except zero.
        for i in range(len(nums)):
            if nums[i] != 0:
                if total_zeros == 0:
                    output[i] = product_all/nums[i]
                elif total_zeros == 1:
                    output[i] = 0
            else:
                output[i] = product_all
                
        return output
