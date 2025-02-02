import string

def analyze_text(text):
    # Calculate the number of sentences
    sentences = text.split('.')
    num_sentences = len(sentences) - 1
    
    # Split words and calculate their frequencies
    words = text.split()
    word_freq = {}
    for word in words:
        word = word.strip(string.punctuation).lower()
        if word in word_freq:
            word_freq[word] += 1
        else:
            word_freq[word] = 1
    
    # Calculate the average word length
    total_word_length = sum(len(word) for word in words)
    avg_word_length = total_word_length / len(words)
    
    # Calculate the total number of characters (excluding spaces)
    total_characters = len(text.replace(" ", ""))
    
    return num_sentences, word_freq, avg_word_length, total_characters

def main():
    text = input("Please enter the text you want to analyze: ")
    num_sentences, word_freq, avg_word_length, total_characters = analyze_text(text)
    
    print(f"Number of Sentences: {num_sentences}")
    print(f"Average Word Length: {avg_word_length:.2f}")
    print(f"Total Number of Characters (excluding spaces): {total_characters}")
    print("Word Frequencies:")
    for word, freq in word_freq.items():
        print(f"{word}: {freq}")

if __name__ == "__main__":
    main()
