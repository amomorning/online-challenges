(* ::Package:: *)
(* :Title: ProjectEuler *)
(* :Context: ProjectEuler` *)
(* :Author: Yichen Mo *)
(* :Date: 2021/10/04 *)

(* :Package Version: 1.0 *)
(* :Keywords: Math *)

BeginPackage["ProjectEuler`"]

PE033::usage="The fraction 49/98 is a curious fraction, as an inexperienced mathematician in attempting to simplify it may incorrectly believe that 49/98 = 4/8, which is correct, is obtained by cancelling the 9s\nFind exactly four non-trivial examples of this type of fraction, less than one in value, and containing two digits in the numerator and denominator."

PE034::usage="145 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 = 145.  \nFind the sum of all numbers which are equal to the sum of the factorial of their digits.  \nNote: As 1! = 1 and 2! = 2 are not sums they are not included."

PE035::usage="usage:\nPE035[1000000]\n\nThe number, 197, is called a circular prime because all rotations of the digits: 197, 971, and 719, are themselves prime.\nThere are thirteen such primes below 100: 2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, and 97.\nHow many circular primes are there below one million?\n"

PE050::usage="The prime 41, can be written as the sum of six consecutive primes: \n41 = 2 + 3 + 5 + 7 + 11 + 13 \nThis is the longest sum of consecutive primes that adds to a prime below one-hundred.  \nThe longest sum of consecutive primes below one-thousand that adds to a prime, contains 21 terms, and is equal to 953.  \nWhich prime, below one-million, can be written as the sum of the most consecutive primes?"

PE052::usage="It can be seen that the number, 125874, and its double, 251748, contain exactly the same digits, but in a different order.  \nFind the smallest positive integer, x, such that 2x, 3x, 4x, 5x, and 6x, contain the same digits."

PE053::usage="There are exactly ten ways of selecting three from five, 12345: \n123, 124, 125, 134, 135, 145, 234, 235, 245, and 345\nIn combinatorics, we use the notation, (5 3)=10\nIt's not until n=23, that a value exceeds one-million (23 10)=1144066\nHow many, not necessarily distinct, values of (n r) for 1<=n<=100, are greater than one-million?"

PE055::usage="If we take 47, reverse and add, 47 + 74 = 121, which is palindromic.  \nNot all numbers produce palindromes so quickly. For example, \n \n349 + 943 = 1292, \n1292 + 2921 = 4213 \n4213 + 3124 = 7337 \n \nThat is, 349 took three iterations to arrive at a palindrome.  \nAlthough no one has proved it yet, it is thought that some numbers, like 196, never produce a palindrome. A number that never forms a palindrome through the reverse and add process is called a Lychrel number. Due to the theoretical nature of these numbers, and for the purpose of this problem, we shall assume that a number is Lychrel until proven otherwise. In addition you are given that for every number below ten-thousand, it will either (i) become a palindrome in less than fifty iterations, or, (ii) no one, with all the computing power that exists, has managed so far to map it to a palindrome. In fact, 10677 is the first number to be shown to require over fifty iterations before producing a palindrome: 4668731596684224866951378664 (53 iterations, 28-digits).  \nSurprisingly, there are palindromic numbers that are themselves Lychrel numbers; the first example is 4994.  \nHow many Lychrel numbers are there below ten-thousand?  \nNOTE: Wording was modified slightly on 24 April 2007 to emphasise the theoretical nature of Lychrel numbers."

PE056::usage="A googol (10100) is a massive number: one followed by one-hundred zeros; 100100 is almost unimaginably large: one followed by two-hundred zeros. Despite their size, the sum of the digits in each number is only 1.  \nConsidering natural numbers of the form, ab, where a, b < 100, what is the maximum digital sum?"

PE057::usage="https://projecteuler.net/problem=57"

PE058::usage="Starting with 1 and spiralling anticlockwise in the following way, a square spiral with side length 7 is formed.
\n37 36 35 34 33 32 31 \n38 17 16 15 14 13 30 \n39 18  5  4  3 12 29 \n40 19  6  1  2 11 28 \n41 20  7  8  9 10 27 \n42 21 22 23 24 25 26 \n43 44 45 46 47 48 49 \nIt is interesting to note that the odd squares lie along the bottom right diagonal, but what is more interesting is that 8 out of the 13 numbers lying along both diagonals are prime; that is, a ratio of 8/13 < 62%.  \nIf one complete new layer is wrapped around the spiral above, a square spiral with side length 9 will be formed. If this process is continued, what is the side length of the square spiral for which the ratio of primes along both diagonals first falls below 10%?" 

(* PE059::usage="https://projecteuler.net/problem=59" *)
PE059::usage="Each character on a computer is assigned a unique code and the preferred standard is ASCII (American Standard Code for Information Interchange). For example, uppercase A = 65, asterisk*= 42, and lowercase k = 107.  \nA modern encryption method is to take a text file, convert the bytes to ASCII, then XOR each byte with a given value, taken from a secret key. The advantage with the XOR function is that using the same encryption key on the cipher text, restores the plain text; for example, 65 XOR 42 = 107, then 107 XOR 42 = 65.  \nFor unbreakable encryption, the key is the same length as the plain text message, and the key is made up of random bytes. The user would keep the encrypted message and the encryption key in different locations, and without both halves, it is impossible to decrypt the message.  \nUnfortunately, this method is impractical for most users, so the modified method is to use a password as a key. If the password is shorter than the message, which is likely, the key is repeated cyclically throughout the message. The balance for this method is using a sufficiently long password key for security, but short enough to be memorable.  \nYour task has been made easy, as the encryption key consists of three lower case characters. Using p059_cipher.txt (right click and 'Save Link/Target As...'), a file containing the encrypted ASCII codes, and the knowledge that the plain text must contain common English words, decrypt the message and find the sum of the ASCII values in the original text."

PE060::usage="The primes 3, 7, 109, and 673, are quite remarkable. By taking any two primes and concatenating them in any order the result will always be prime. For example, taking 7 and 109, both 7109 and 1097 are prime. The sum of these four primes, 792, represents the lowest sum for a set of four primes with this property.  \nFind the lowest sum for a set of five primes for which any two primes concatenate to produce another prime."

PE061::usage="https://projecteuler.net/problem=61\nFind the sum of the only ordered set of six cyclic 4-digit numbers for which each polygonal type: triangle, square, pentagonal, hexagonal, heptagonal, and octagonal, is represented by a different number in the set."

Begin["`Private`"]

(* PE033 *)
cancelFractions[a_] := 
 Module[{arr = a, digits = IntegerDigits[a]}, 
  MemberQ[Rational @@ 
      Flatten[Replace[digits, {x___, #, y___} :> {x, y}, {1}]] & /@ 
    Select[Range[9], 
     MemberQ[digits[[1]], #] && MemberQ[digits[[2]], #] &], 
   Rational @@ arr]]

PE033[]:=Denominator[Times @@ Rational @@@ 
 Select[ReplaceList[Range[10, 99], {___, x_, ___, y_, ___} :> {x, y}],
   cancelFractions]]


(* PE034 *)
PE034[]:=Total@Select[Range[3, 100000], 
  Total[Factorial@IntegerDigits[#]] == # &]


(* PE035 *)
circularPrimeQ[x_Integer] := 
 Module[{digits = IntegerDigits[x]}, 
  And @@ PrimeQ@
    Map[FromDigits, 
     NestList[RotateLeft, digits, Length[digits] - 1], {1}]]

primes[n_Integer]:=Prime[Range[PrimePi[n]]]

PE035[n_Integer]:=Count[circularPrimeQ[#] & /@ primes[n], True]


(* PE050 *)
consecutivePrime[l_, r_] := {Total@Prime[Range[l, r]], r - l + 1}

lastPrime[start_] := 
 Last[Select[consecutivePrime[start, #] & /@ Range[1, 600], 
   PrimeQ[#[[1]]] && #[[1]] < 1000000 &]]

PE050[]:=Sort[lastPrime[#] & /@ Range[10], #1[[2]] < #2[[2]] &] // Last


(* PE052 *)
PE052[]:=Select[Range[200000], 
 Length[Union[
     FromDigits[Sort[IntegerDigits[#]]] & /@ (Range[6]*#)]] == 1 &]


(* PE053 *)
PE053[]:=Select[Binomial @@@ 
   Flatten[Outer[List, Range[100], Range[100]], 1], # > 
    1000000 &] // Length


(* PE055 *)
LychrelNumberList[num_Integer] := 
 NestWhileList[# + IntegerReverse[#] &, 
  If[PalindromeQ[num], 2 num, num], PalindromeQ[#] == False &, 1, 53]
LychrelQ[num_Integer]:=Length[LychrelNumberList[num]] == 54
PE055[]:=Select[Range[10000], LychrelQ] // Length


(* PE056 *)
PE056[]:=Max[Total@IntegerDigits[Power @@ #] & /@ 
  Flatten[Outer[List, Range[100], Range[100]], 1]]

(* PE057 *)
PE057[]:=Select[NumeratorDenominator[NestList[1/(2 + #) &, 0, 1000] + 1], 
  IntegerLength[#[[1]]] > IntegerLength[#[[2]]] &] // Length


(* PE058 *)
allSpiralNum = 
  Flatten[{1, Table[{x, x, x, x}, {x, 20000}]*2}] // Accumulate;
getPrimeNum[n_] := 
 With[{part = allSpiralNum[[1 ;; 4 n + 1]]}, {part[[-1]] - 
    part[[-2]] + 1, N[Length[Select[part, PrimeQ]]/Length[part]]}]
PE058:=Select[getPrimeNum[#] & /@ Range[13100, 13200], #[[2]] < 0.1 &][[1]]


(* PE059 *)
Begin["`PE059`"]
str = Import[
   "https://projecteuler.net/project/resources/p059_cipher.txt"];
strCode = StringSplit[str, ","];
key = Table[
   BitXor[Interpreter["Integer"][
     Last[Normal[Sort[Counts[strCode[[start ;; -1 ;; 3]]]]]][[1]]], 
    32], {start, 3}] // RotateRight;
strIndex = Table[{i, strCode[[i]]}, {i, Length[strCode]}];
decryCode = BitXor[Interpreter["Integer"][#[[2]]],
     key[[Mod[#[[1]], 3] + 1]]
     ] & /@ strIndex;
PE059:={Total[decryCode],FromCharacterCode[decryCode]}
End[]

(* PE060 *)
primePairQ[{x_Integer, y_Integer}] := 
 And[PrimeQ[x*Power[10, IntegerLength[y]] + y], 
  PrimeQ[y*Power[10, IntegerLength[x]] + x]]
primePairs = 
  Select[Subsets[ProjectEuler`Private`primes[10000], {2}], 
   primePairQ];
PE060[]:=Plus @@@ FindClique[Graph[UndirectedEdge @@@ primePairs], {5}]


(* PE061 *)
polygonalNumbers = 
  Select[#, 1000 <= # < 10000 && Mod[#, 100] > 10 &] & /@ 
   Table[PolygonalNumber[x, y], {x, 3, 8}, {y, 1, 200}];
cyclicalPairQ[list_, n_] := 
 Select[polygonalNumbers[[n]], MemberQ[Mod[list, 100], Floor[#/100]] &]
cyclicalPolygonalQ[list_] := 
 With[{fold = FoldList[cyclicalPairQ, polygonalNumbers[[1]], list]}, 
  Length@Last[fold] > 0
   && fold[[-1]] == fold[[-7]]]
PE061[]:=Total@FoldList[cyclicalPairQ, polygonalNumbers[[1]], 
   First[Select[Flatten[{#, 1, #}] & /@ Permutations[Range[2, 6]], 
     cyclicalPolygonalQ]]][[-6 ;; -1]]

End[]

EndPackage[]


