from preprocessing import PreProcessor
from paragraph import Paragraph

def main():
    print("SUMMARIZING")

    with open('test.txt', 'r') as text:
        paragraph = Paragraph(text.read())

if __name__ == "__main__":
    main() 