func gcdOfStrings(str1 string, str2 string) string {
    runes1 := []rune(str1)
    runes2 := []rune(str2)
    greatest := []rune{}
    for i := 0; i < len(str2); i++ {
        if runes1[i] == runes2[i] {
            greatest = append(greatest, runes1[i])
        } else {
            break
        }
    }

    return string(greatest)
}