import re
# Using jaccard similarity on two set of strings


def get_jaccard_sim(arg1, arg2):
    a = set(arg1.split())
    b = set(arg2.split())
    c = a.intersection(b)
    return round(float(len(c)) / (len(a) + len(b) - len(c)), 3)


if __name__ == "__main__":
    str1 = "Hello how are you?"
    str2 = "hello I am fine, how are you!"
    # In this case we compare two strings while considering case sensitivity
    print(f"Case-sensitive Jaccard Similarity is: {get_jaccard_sim(str1, str2)}\n")
    # In this case we compare two strings case insensitive
    low_str1 = str1.lower()
    low_str2 = str2.lower()
    print(f"Case-insensitive Jaccard Similarity is: {get_jaccard_sim(low_str1, low_str2)}\n")
    # Comparing two case-insensitive strings by removing all the punctuations and special characters
    reg_str1 = re.sub('\W+', ' ', low_str1)
    reg_str2 = re.sub('\W+', ' ', low_str2)
    print(f"Case-insensitive string without punctuations and special characters Jaccard Similarity is: {get_jaccard_sim(reg_str1, reg_str2)}\n")

