class FileManager:
    def save(self, ascii_art):
        with open("ascii_art.txt", "w") as file:
            file.write(ascii_art)
