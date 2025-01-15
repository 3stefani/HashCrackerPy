# HashCrackerPy
This project is a Python program that attempts to decode a SHA-256 hash key using a dictionary attack. The program compares hashes generated from words in a dictionary file with a target hash specified in the code.

## Features

- Supported Algorithm: SHA-256.

- Input: A text file containing possible passwords (dictionary).

- Output: The original password if found in the dictionary.

- Automatically verifies each dictionary word against the target hash.

## How to Use

1. Clone this repository or copy the code into a Python file.

2. Create a text file containing a list of possible passwords, one per line.

3. Ensure the target hash is specified in the hash_file variable in the code.

4. Run the program and provide the path to the dictionary file when prompted.

## Execution

  python decoder.py

### Example

Dictionary file (dictionary.txt):

  test
  password
  123456
  test123
  admin

Target hash:

  ff960cb55673958c594d0daaab1e368651c75c02f9687192a1811e7b180336a7

Output:

  Enter the dictionary file path: dictionary.txt
  The original password is: test123

## Requirements

Python 3.6 or higher.

## How It Works

The program prompts the user to input the location of a text file containing possible passwords.

Each line of the file is used to generate a SHA-256 hash.

The calculated hash is compared to the target hash.

If the hashes match, the program prints the original password and exits.

If no match is found, it informs the user that the password is not in the dictionary.

## Limitations

Works only with SHA-256 hashes.

Requires a pre-prepared dictionary file.

Does not support brute force attacks without a dictionary.

#Disclaimer

This program is provided for educational purposes only. Misusing password cracking tools can be illegal. Use this software only on systems where you have explicit permission.
