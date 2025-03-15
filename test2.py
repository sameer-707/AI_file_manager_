def up_dir(s):
    # Find the last occurrence of '/' using rindex()
    last_slash_index = s.rindex('/')
    # Return the substring from the start up to (but not including) the last slash
    return s[:last_slash_index]

# Test it
input_string = "1/23/44/55/90/100"
result = remove_after_last_slash(input_string)
print(result)  # Output: 1/23/44/55