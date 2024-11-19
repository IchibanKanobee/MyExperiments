
def distribute_candies(candies, num_people):
    remaining_candies = candies
    candies_to_give = 0
    distr = [0] * num_people
    while(remaining_candies > 0):
        for i in range(num_people):
            candies_to_give +=1
            if candies_to_give > remaining_candies:
                given_candies = remaining_candies
                remaining_candies = 0
                distr[i] = distr[i] + given_candies
                break
            else:
                given_candies = candies_to_give
                remaining_candies -= given_candies
                distr[i] = distr[i] + given_candies
    return distr

distr = distribute_candies(10, 3)
print (distr)