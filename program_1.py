sentence = input("Enter a sentence:")
print(len(sentence))

file_name = input("Enter a file name:")
file_name = f"{file_name}.txt"
with open(file_name, "w") as f:
    f.write(sentence)
    f.close()

    print("You've written {sentence_length}")