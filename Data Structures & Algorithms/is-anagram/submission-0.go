func isAnagram(s string, t string) bool {
    if len(s) == 0 {
        return false
    }
    if len(s) != len(t) {
        return false
    }

    letters := make(map[rune]int)
    for _, l := range s {
        if _, ok := letters[l]; ok {
            letters[l]++
        } else {
            letters[l] = 1
        }
    }

    for _, l := range t {
        if _, ok := letters[l]; !ok {
            return false
        }
        letters[l]--
    }

    for _, n := range letters {
        if n != 0 {
            return false
        }
    }
    return true
}
