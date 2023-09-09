import time

# Function to check if a word is compounded
def is_compounded(word, word_set):
    if not word:
        return False
    
    n = len(word)
    dp = [False] * (n + 1)
    dp[0] = True
    
    for i in range(1, n + 1):
        for j in range(i):
            if dp[j] and word[j:i] in word_set:
                dp[i] = True
                break
    
    return dp[n]

# Function to find the longest and second-longest compounded words
def find_longest_and_second_longest_compounded_words(word_list):
    word_set = set(word_list)
    word_list.sort(key=lambda x: (-len(x), x))
    
    longest_compounded_word = ""
    second_longest_compounded_word = ""
    
    for word in word_list:
        word_set.remove(word)
        if is_compounded(word, word_set):
            if not longest_compounded_word:
                longest_compounded_word = word
            else:
                second_longest_compounded_word = word
                break
    
    return longest_compounded_word, second_longest_compounded_word

if __name__ == "__main__":
    start_time = time.time()
    
    with open("Input_02.txt", "r") as file:
        word_list = [line.strip() for line in file]

    longest_compounded_word, second_longest_compounded_word = find_longest_and_second_longest_compounded_words(word_list)
    
    end_time = time.time()
    processing_time = int((end_time - start_time) * 1000)

    print(f"Longest Compound Word {longest_compounded_word}")
    print(f"Second Longest Compound Word {second_longest_compounded_word}")
    print(f"Time taken to process file Input_02.txt {processing_time} milli seconds")
