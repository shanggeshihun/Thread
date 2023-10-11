# coding:utf-

class ReadWriteFile():
    def __init__(self,file_path):
        self.file_path=file_path

    def clear_content(self):
        with open(self.file_path,'r+') as f:
            f.truncate()

    def add_write(self,str):
        with open(self.file_path, 'a') as f:
            f.write(str)
            f.write('\n')

    def add_writelines(self,lines):
        with open(self.file_path, 'a') as f:
            f.writelines(lines)
            f.write('\n')

    def re_write(self,str):
        with open(self.file_path, 'w') as f:
            f.write(str)
            f.write('\n')

    def re_writelines(self,lines):
        with open(self.file_path, 'w') as f:
            f.writelines(lines)
            f.writelines('\n')

if __name__ == '__main__':
    rw=ReadWriteFile(r'D:\learn\software_learn\NOTE\Python\Thread\9ht\write_info.txt')
    rw.add_write('bbb')
    rw.add_writelines(('a','b'))