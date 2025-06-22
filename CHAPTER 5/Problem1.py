# Write a program to create a dictionary of hindi words with values as their english translation. provide user with an option to look it up!

words = {
    "नमस्ते": "Hello",
    "धन्यवाद": "Thank you",
    "कृपया": "Please",
    "शुभकामनाएँ": "Best wishes",
    "सुप्रभात": "Good morning",
    "शुभ रात्रि": "Good night",
    "कैसे हो?": "How are you?",
    "मुझे माफ करें": "Excuse me",
    "आपका नाम क्या है?": "What is your name?",
    "मुझे समझ में नहीं आया": "I did not understand"
}

word = input("Enter a Hindi word to translate to English: ")
print("The English translation is:", words.get(word, "Word not found in dictionary."))