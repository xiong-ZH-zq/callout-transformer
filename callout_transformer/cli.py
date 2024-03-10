import argparse

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("source_style", help="The source style of markdown callouts")

    parser.parse_args()
