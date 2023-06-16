## Note
The following tasks may require you to research certain subjects on your own. You will apply your current understanding of the Python programming languages, but certain tasks (such as certain algorithms, mathematical equations etc) will be done via researching maybe through online sources, documentation or books. Part of what makes software engineering, or engineering as a whole is to continously learn about new topics frequently. As technologies evolve, you will be required to learn more and more as a software/cybersecurity engineer.

If you are having troubles with some of the questions, it's fine to skip some of them and work on another question then come back to it when you feel ready.

# Task 1
## XOR cipher
### In this question you will have to investigate and research about the XOR cipher.
Create a function called `xor_cipher` that uses the XOR cipher algorithm to encode a string (using XOR operation). To make this task simpler, the key size will just be of size 1.

Example of what it would look like using the function:
```py
plaintext = "Hello, world!" #Message
key = "K"  #Single-character key

#Encoding the cipertext
ciphertext = xor_cipher(plaintext, key)
print("Ciphertext:", ciphertext) #Message is now encoded

#Decoding the ciphertext
decrypted_message = xor_cipher(ciphertext, key)
print("Decrypted message:", decrypted_message) #Message is now decoded
```

For extension, try make the `xor_cipher` function support any size key.

# Task 2
## HTTP Requests
### In this question you will have to investigate and research about HTTP requests, what HTTP and a HTTP header is. As part of the task you have to investigate how to "send a HTTP request and get a response" in Python.
Use Python's `requests` module (if you by chance don't have it working or installed try `pip install requests`) to send an HTTP request to the following URI `https://ifconfig.me/all` and print the response. The response should give you a string representing the HTTP headers which you can print to the terminal. Explain what the `ip_addr`, `user_agent` and `method` headers mean.

An example output from the program (Note: Its better off not showing the output from your program to anyone else, this task just requires you to explain what these headers mean):
```
ip_addr: 112.134.65.21
remote_host:
user_agent: python-requests/2.25.0
port: 22344
language:
referer:
connection:
keep_alive:
method: GET
encoding: gzip, deflate
mime: */*
charset:
via:
forwarded: 1.1 google
```

# Task 3
## Hangman game
Make a hangman game that runs under the terminal where the computer chooses the word and the user has to guess it. 
There should be a user input where it can only take one character (the letter) and if the user inputs a letter that resides within the word make sure to display it. You can make the computer randomly pick a word from a set of words that you defined (maybe from a list, set, dictionary etc), but make the words have character length greater or equal to 4. If the user guesses wrong 6 times, it's game over, if the user gets the entire word its a win.

Here is an example of what the game could look like:
```
WORD:
_ _ _ _ _
Guess letter> E

WORD:
_ E _ _ _
Guess letter> L

WORD:
_ E L L _
Guess letter> L
Letter has already been guessed!

WORD:
_ E L L _
Guess letter> O

WORD:
_ E L L O
Guess letter> C
Incorrect guess (Guesses left: 1/6)

WORD:
_ E L L O
Guess letter> ASD
You can only input singular characters!

WORD:
_ E L L O
Guess letter> H

You win! The word was 'HELLO'
```

If you want you can draw the hangman every time the user gets an input wrong, but that is optional.
