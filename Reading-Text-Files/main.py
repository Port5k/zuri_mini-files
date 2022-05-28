# Read text from a file, and count the occurence of words in that text
# Example:
# count_words("The cake is done. It is a big cake!") 
# --> {"cake":2, "big":1, "is":2, "the":1, "a":1, "it":1}

def read_file_content(filename):
    file_content = open(filename,"r")
    return file_content



def count_words():
    file_content = read_file_content("./story.txt")
    text_dict = dict()

    # Loop through each line of the file
    for line in file_content:
            line = line.strip()
            line = line.lower()
            
            # Split the line into words
            words = line.split(" ")

            # Loop over each word in line
            for word in words:
                    # Check if the word is already in dictionary
                    if word in text_dict:
                            text_dict[word] = text_dict[word] + 1
                    else:
                            text_dict[word] = 1

    # Print dictionary content
    for key in list(text_dict.keys()):
            print(key, ":", text_dict[key])

count_words()
