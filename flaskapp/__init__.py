#!/usr/bin/env python3
# -*- coding: utf-8 -*-


# Start Imports
from configparser import ConfigParser
from flask import Flask, jsonify, request
import os
from datetime import datetime
from random import choices, randint, getrandbits
from .english_words import english_words_set
# End imports

# The english_words file is taken from
# https://raw.githubusercontent.com/mwiens91/english-words-py/master/english_words/__init__.py

# Defining the directories
filepath = os.path.dirname(os.path.abspath(__file__))
basedir = os.path.dirname(filepath)

# Reading configurations
config = ConfigParser()

config.read(os.path.join(basedir, "config.ini"))

app = Flask(__name__)

app.config["SECRET_KEY"] = config.get("CONFIGURATION", "flask_key",
                                      fallback=getrandbits(2 ^ 63))

NUM_WORDS = 100
START_NUM = 0
END_NUM = 2**32


# Home page


@app.route("/")
def home():
    return jsonify(
        message="Welcome to the API",
        datetime=datetime.now().strftime("%c")
    )

# Health check


@app.route("/healthcheck/")
def health():
    return jsonify(
        message="doin' ok",
        datetime=datetime.now().strftime("%c")
    )

# Get n random words


@app.route("/words/")
def randomword():
    if "n" in request.args:
        if request.args["n"].isnumeric():
            n = int(request.args["n"])
        else:
            n = NUM_WORDS
    else:
        n = NUM_WORDS
    words = choices(english_words_set, k=n)
    return jsonify(
        datetime=datetime.now().strftime("%c"),
        num_words=n,
        words=words
    )

# Get a num between s and e, in the o format


@app.route("/num/")
def randomnum():
    if "s" in request.args:
        if request.args["s"].isnumeric():
            s = int(request.args["s"])
        else:
            s = START_NUM
    else:
        s = START_NUM
    if "e" in request.args:
        if request.args["e"].isnumeric():
            e = int(request.args["e"])
        else:
            e = END_NUM
    else:
        e = END_NUM

    n = randint(min(s, e), max(s, e))

    if "o" in request.args:
        if request.args["o"] == "hex":
            n = hex(n)
        elif request.args["o"] == "bin":
            n = bin(n)
        elif request.args["o"] == "oct":
            n = oct(n)

    return jsonify(
        datetime=datetime.now().strftime("%c"),
        num=n
    )
