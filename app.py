import os
from flask import Flask
app=Flask(__name__)

@app.route("/")
def main():
  return "Wlecome!"

@app.route("/How are you")
def hello():
  return"I am okay, how about you?"

if __name__ == "__main__":
  app.run()
