# A Very Simple Flask API | Proof of Concept

### This API is supposed to be very simplistic, so it doesn't do much, how much simpler could it be? It just gives a series of random text data, a random number, and a random date

Usage

1. /healthcheck

	Check if the API is down


2. /words

	Takes the following queries
		a. n (integer, number of words)

3. /num

	Takes the following queries
		a. s (starting range, optional, defaults to 0)
		b. e (starting range, optional, defaults to 2^32)
		c. o (oct, hex or bin, optional, defaults to decimal)

Requirement

1. python>=3.8.7
2. flask>=1.1.2
3. werkzeug>=1.0.1

Routes


	Endpoint    Methods  Rule
	----------  -------  -----------------------
	health      GET      /healthcheck/
	home        GET      /
	randomnum   GET      /num
	randomword  GET      /words
