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

End[]

EndPackage[]



