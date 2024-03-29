#IMPORTING MODULES
import random
import numpy as np
import math as m
random.seed(42)

#TO CONSTRUCT A MATRIX FOR GIVIN STRING
def chr_to_mat(key):
	k = 0
	for i in range(1):
		for j in range(l):
			mat[i][j] = ord(key[k]) % 65
			k += 1
	return mat
#TAKING INPUT
msg=input("Enter a string ").upper()
l=len(msg)

#GENERATING KEY MATRIX FOR ENCODING
keyMatrix = np.array([[random.randint(0,25) for x in range (l)] for y in range(l)])
#IT IS A AUXILIARY MATRIX FOR CHR TO MAT FUNCTION
mat= np.array([[random.randint(0,0) for x in range (l)] for y in range(1)])
# CALLING FUN TO GENERATE A MATRIX TO USER ENTERED MSG 
chr_to_mat(msg)
#IT IS A AXULLARY MATRIX TO STORE 
output = np.array([[random.randint(0,0) for x in range (l)] for y in range(1)])
deout=np.array([[random.randint(0,0) for x in range (l)] for y in range(1)])
#MUL OF KEY MATRIX AND MSG MATRIX
output=mat*keyMatrix
# CONVERTING NUMPY ARRAY TO NORMAL LIST
output=output.tolist()
# APPLYING MOD OPERATION AND AND CONVERTING TO STANDERD NUMBERS WHICH HELPS IN CONVERTING INT TO CHAR BASED ON ASCII
lis=[]
mod=[]
for i in range(l):
  lis.append((sum(output[i])))
lis=np.array(lis)
for i in range(l):
  mod.append(((lis[i])%26)+65)

char=[]
for i in range(l):
  char.append(chr(mod[i]) )
s=""
key2=s.join(char)
#PRINTING ENCODED MSG
print("Encoded",s.join(char))


# CALLING FUN TO GENERATE A MATRIX TO ENCODED MSG 
chr_to_mat(key2)
#FINDING INVERSE 
keyMatrix=np.linalg.inv(keyMatrix)
#MUL OF INVERSE WITH MATRIX TO DECODE
deout=keyMatrix*lis
deout=deout.tolist()

# APPLYING MOD OPERATION AND AND CONVERTING TO STANDERD NUMBERS WHICH HELPS IN CONVERTING INT TO CHAR BASED ON ASCII

fin=[]
for i in range(l):
	fin.append(sum(deout[i]))
 
fin1=[]
for i in range(l):
  fin1.append(m.ceil(round((fin[i]+65),3)))

outmsg=[]
for i in range(l):
  outmsg.append(chr(fin1[i]) )
s=""

#FINALLY PRINTING DECODED MSG
print("Decoded",s.join(outmsg))
