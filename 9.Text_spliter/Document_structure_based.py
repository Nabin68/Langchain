from langchain_text_splitters import RecursiveCharacterTextSplitter,Language

text="""
class Calculator:
    def __init__(self):
        print("Calculator initialized")

    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

def main():
    calc = Calculator()

    num1 = 10
    num2 = 5

    print("Addition:", calc.add(num1, num2))
    print("Subtraction:", calc.subtract(num1, num2))


if __name__ == "__main__":
    main()
"""
#we tried dividing the whole text into 3 chunks


splitter=RecursiveCharacterTextSplitter.from_language(
    language=Language.PYTHON,
    chunk_size=200,
    chunk_overlap=0,
)

chunks=splitter.split_text(text=text)


print(chunks)

print(len(chunks))
