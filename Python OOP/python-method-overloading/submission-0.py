class TextProcessor:
    # Implement method overloading for format_text method
    def format_text(self, str1: str, str2: str = "") -> str:
        if str2 == "":
            return str1.upper()
        else:
            return str1 + str2


# Don't modify the code below
processor = TextProcessor()
print(processor.format_text("hello"))
print(processor.format_text("hello", "world"))
