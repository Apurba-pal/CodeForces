# A. Word Capitalization
# time limit per test2 seconds
# memory limit per test256 megabytes
# Capitalization is writing a word with its first letter as a capital letter. Your task is to capitalize the given word.

# Note, that during capitalization all the letters except the first one remains unchanged.

# Input
# A single line contains a non-empty word. This word consists of lowercase and uppercase English letters. The length of the word will not exceed 103.

# Output
# Output the given word after capitalization.

# Examples
# InputCopy
# ApPLe
# OutputCopy
# ApPLe
# InputCopy
# konjac
# OutputCopy
# Konjac

# Codeforces (c) Copyright 2010-2026 Mike Mirzayanov
# The only programming contests Web 2.0 platform
# Server time: Sep/26/2026 22:07:33UTC+5.5 (h1).
# Desktop version, switch to mobile version.
# Privacy Policy | Terms and Conditions
# Supported by



word = input().strip()
print(word[0].upper() + word[1:])