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

End[]

EndPackage[]



