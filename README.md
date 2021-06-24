# primes_and_keys
Experiment to try to generate large prime numbers, and build intentionally weak RSA keys that can be exploited

## DO NOT USE THIS TO CREATE KEYS FOR THE REAL WORLD

## Purpose
This is an exploratory project to build RSA keys that are subject to attack with various methods.

The primary goal is to use this code as a framework to create CTF type challenges, but also so that I can learn stuff.

## Fermat Attack
Create a key using prime numbers that are close together - then use the public key and cipher text to derive the private key, and decode the text
```
doesitwork.py
```


