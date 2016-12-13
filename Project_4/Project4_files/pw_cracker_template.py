# Passwords are in the format found in /etc/shadow: $[hash_algorithm_id]$[hash_salt]$[hash_data]
#
# This format optionally allows changing the number of rounds each hash function is applied:
# $[hash_algorithm_id]$rounds=[# of rounds]$[hash_salt]$[hash_data]
#
# For this homework exercise, the salt is prepended to the password and is only applied in the
# first round. The input to the next round of hashing is a hex string of the previous hash digest.
#
# Hash algorithm IDs and default rounds:
# 1 MD5 (1000 rounds)
# 2 Blowfish (64 rounds)
# 5 SHA256 (5000 rounds)
# 6 SHA512 (5000 rounds)
#
# To verify your password hash function works correctly, you can use the following test vectors:
#
# # pw = 'ECE 4802 rocks!'
# $6$rounds=1$ESw6=oECkdYnvX=y$c86eb8420756e3dd900f142f106b798427456546a08b596888d6a15ec484aab153795832ceef34282fb50fe4c68ca0f39ba13c1458135abccefd83d96c0e2632
# $6$rounds=42$gfqTrX3hUUNjldVu$7ef910c021ad14c5c8f0b195384af61abf520635ad5efb136b0bd9f48849867a59eac5236c607ccc323ea259963752de7c994ca67c096a447921417bd05d6aa6
#
# Using the given wordlist and template code, write code to crack the given passwords, i.e.,
# implement crack_passwords(). Code will be graded on readability, correctness and efficiency.
#
# In your final code, the ONLY thing that ought to be printed to STDOUT is the list of plaintext
# passwords, nedictline separated, in their original order.
# Points will be docked for failure to adhere to this.

# return list of plaintext passwords in the same order as `passwords_from_file`

from Crypto.Hash import SHA512

def crack_passwords(passwords_from_file):
    with open('dictionary.txt', 'r') as fh:
        dictionary = [line.rstrip('\r\n') for line in fh.readlines()]

        dictl = len(dictionary) - 1
        pt = []

        for i in range (0,len(passwords_from_file),1):
            #start = timer() #can be used to measure how long it takes to crack each password
            vec = passwords_from_file[i].split('$') #Separates each line into its individual parts

            if i < 15:

                for j in range(0, dictl, 1):
                    Hash = SHA512.new(vec[2].encode('utf-8') + dictionary[j].encode('utf-8'))

                    for k in range(0,4999,1): #All are SHA512 and default to 5000 rounds
                        Hash = SHA512.new(Hash.hexdigest().encode('utf-8'))

                    if (Hash.hexdigest() == vec[3]):
                        pt.append(dictionary[j])
                        print(dictionary[j]) #Print dictionary word on successful crack
                        break

            else:
                for j in range(0, dictl,1):
                    Hash = SHA512.new(vec[3].encode('utf-8')+dictionary[j].encode('utf-8'))

                    for k in range(0,24999,1):
                        Hash =SHA512.new(Hash.hexdigest().encode('utf-8'))

                    if (Hash.hexdigest() == vec[4]):
                        pt.append(dictionary[j])
                        end = timer()
                        print(dictionary[j]) #Print dictionary word on successful crack
                        break
    return pt # return list of plaintexts

with open('passwords.txt', 'r') as fh:
    plaintexts = crack_passwords([line.rstrip('\r\n') for line in fh.readlines()])
    # for i in fh:
    #     print i
    # Can use this notation to print the final list of plaintexts after all calculations finish
    # Instead I print the words as they are found withing the crack_passwords function.
