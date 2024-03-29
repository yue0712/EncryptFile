from encrypter import Encrypter
from randcode_gen import RandcodeGen
from options import Options
import time
import os

class FileHandler():
    def __init__(self, options:Options, encrypt_complete) -> None:
        self.encrypter = Encrypter()
        self.options = options
        self.id_gen = RandcodeGen.Base36()
        self.encrypt_complete = encrypt_complete

    def _get_file_data(self, dir, path, name) -> None:
        file_path = os.path.join(dir, path, name)
        if(not os.path.isfile(file_path)):
            return None
        stat = os.stat(file_path)
        return {
            "file_path": os.path.join(path, name),
            "size": stat.st_size,
            "mtime": stat.st_mtime
        }
    
    def get_files(self, dir) -> list:
        o_files = []
        for (path, folders, files) in os.walk(dir):
            _path = path[len(dir)+1:]
            o_files.extend([
                self._get_file_data(dir, _path, file)
                for file in files if(not file.startswith("."))
            ])
        return o_files
    
    
    def _get_id(self) -> str:
        return (self.id_gen.int2str(int(time.time()*1000)) + self.id_gen.random(5))

    def encrypt_file(self, file):
        fp = os.path.join(self.options.encrypt_path, file['file_path'])
        name = self._get_id()
        password = self.encrypter.generate_key()
        self.encrypter.encrypt_file(fp, f"{self.options.export_path}/{name}", password)
        print(f"完成加密檔案: {name} 密碼: {password}")
        self.encrypt_complete(file, {
            "name": name,
            "password": password,
        })


    def decrypt_file(self, file, archive):
        (path, name) = os.path.split(file["file_path"])
        self.encrypter.decrypt_file(f"{self.options.export_path}/{archive['name']}", f"data/export/{name}", archive["password"])
        print(f"完成解密檔案: {name}")








