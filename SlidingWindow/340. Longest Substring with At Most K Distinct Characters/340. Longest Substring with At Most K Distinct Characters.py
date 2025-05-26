def lengthOfLongestSubstringKDistinct(s, k):
    """
    Find the length of the longest substring with at most k distinct characters.
    
    Args:
        s: Input string
        k: Maximum number of distinct characters allowed
    
    Returns:
        Length of the longest valid substring
    """
    if k == 0:
        return 0
    
    char_count = {}  # HashMap to track character frequencies
    left = 0
    max_length = 0
    
    for right in range(len(s)):
        # Extend window: add current character
        char_count[s[right]] = char_count.get(s[right], 0) + 1
        
        # Shrink window when constraint violated
        while len(char_count) > k:
            char_count[s[left]] -= 1
            if char_count[s[left]] == 0:
                del char_count[s[left]]
            left += 1
        
        # Update max length for current valid window
        max_length = max(max_length, right - left + 1)
    
    return max_length

# Test cases
def test_solution():
    solution = lengthOfLongestSubstringKDistinct
    
    # Test case 1
    assert solution("eceba", 2) == 3, "Test case 1 failed"
    print("✅ Test case 1 passed: 'eceba' with k=2 -> 3")
    
    # Test case 2
    assert solution("aa", 1) == 2, "Test case 2 failed"
    print("✅ Test case 2 passed: 'aa' with k=1 -> 2")
    
    # Additional test cases
    assert solution("", 2) == 0, "Empty string test failed"
    assert solution("abcdef", 0) == 0, "k=0 test failed"
    assert solution("abcabcbb", 2) == 3, "Complex test failed"
    
    print("🎉 All test cases passed!")

if __name__ == "__main__":
    test_solution()