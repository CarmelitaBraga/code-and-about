func kidsWithCandies(candies []int, extraCandies int) []bool {
    biggest := -1
    for _, numCandies := range candies {
        if numCandies > biggest {
            biggest = numCandies
        }
    }

    var result []bool

    for _, numCandies := range candies {
        if (numCandies + extraCandies) >= biggest {
            result = append(result, true)
        } else {
            result = append(result, false)
        }
    } 

    return result
}