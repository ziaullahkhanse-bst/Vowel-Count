def get_count(sentence):
    vowels = "aeiou"
    count = 0
    
    for char in sentence:
        if char in vowels:
            count = count + 1
    
    return count


print(get_count("hello"))        
print(get_count("aeiou"))        
print(get_count("abcde"))        
print(get_count("my name"))      
print(get_count("python"))       
