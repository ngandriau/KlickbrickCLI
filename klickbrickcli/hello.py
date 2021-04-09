import argparse

def main():
  parser = argparse.ArgumentParser()
  parser.add_argument('hello',
                    type=str,
                    help="Friendly command that says hello")

  print("HELLO TAYLOR")
