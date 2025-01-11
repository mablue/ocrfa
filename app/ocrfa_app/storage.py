from django.core.files.storage import FileSystemStorage

class CustomFileSystemStorage(FileSystemStorage):
    def _save(self, name, content):
        # Disable file locking
        return super()._save(name, content)
        
        
