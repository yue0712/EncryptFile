from gui import GUI
from password_data import PasswordData
from file_handler import FileHandler
from options import Options
import os

class Manager():
    def __init__(self, data_path) -> None:
        super().__init__()
        self.options = Options()
        program_path = os.path.abspath(__file__)
        (folder, _) = os.path.split(program_path)
        self.options.encrypt_path = f"{folder}/data/files"
        self.options.export_path = f"{folder}/data/export"
        self.db = PasswordData(data_path)
        self.file_handler = FileHandler(
                            self.options, 
                            self.encrypt_complete
                        )
        self.gui = GUI( self.options,
                        encrypt_file = self.encrypt_file,
                        decrypt_archive = self.decrypt_archive,
                        find_files = self.find_files
                    )
        self.find_files()
    
    # 掃描資料夾，找尋需要加密的檔案
    def find_files(self):
        if(self.options.encrypt_path):
            files = self.file_handler.get_files(self.options.encrypt_path)
            self.db.add_files(files)
        self.set_files()

    # 掃描資料夾，找尋需要加密的檔案
    def set_files(self) -> list:
        files = self.db.get_files()
        self.gui.set_file_list(files)
        return files
    
    # 一個檔案完成加密
    def encrypt_complete(self, file, archive):
        self.db.write(file, archive)
        self.gui.set_file_list_item_state(file["file_path"], "archived")

    # --------------------------------------------------------------------------------------------------------------------------------------

    # 加密
    def encrypt_file(self, file):
        self.file_handler.encrypt_file(file)

    # 解密
    def decrypt_archive(self, file):
        archive = self.db.find(file["file_path"])
        self.file_handler.decrypt_file(file, archive)


    def run(self):
        self.gui.run()


if __name__ == "__main__":
	Manager("data").run()



