from spellchecker import SpellChecker


class SpellCheckerApp:
    def __init__(self):
        self.spell = SpellChecker()

    def correctText(self,text):
        words = text.split()
        correctedwords = []

        for word in words:
            correctedWord = self.spell.correction(word)
            if correctedWord != word.lower():
                print(f"Correcting {word} to {correctedWord}")    
                correctedwords.append(correctedWord)


        return " ".join(correctedwords)


    def run(self):
        print("\n---Spell Checker---")

        while True:
            text = input("Enter text to check or type exit to quit : ")

            if text.lower() == "exit":
                print("Closing the Program....")

            corrected_Text = self.correctText(text)
            print(f"Corrected Text : {corrected_Text}")


if __name__ == "__main__":
    SpellCheckerApp().run()                        