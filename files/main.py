__winc_id__ = "ae539110d03e49ea8738fd413ac44ba8"
__human_name__ = "files"


import os, shutil
from zipfile import ZipFile

current_directory = os.path.dirname(os.path.realpath(__file__)) 
cache_folder = os.path.join(current_directory, 'cache')
zip_file = os.path.abspath("files/data.zip") 

# 1 creeer folder cache, en als deze al bestaat, verwijder files.
def clean_cache():
    if os.path.exists(cache_folder):
        for filename in os.listdir(cache_folder):
            file_path = os.path.join(cache_folder, filename)
      
            try:
                if os.path.isfile(file_path) or os.path.islink(file_path): 
                    os.unlink(file_path) 
                elif os.path.isdir(file_path):
                    shutil.rmtree(file_path)
            except OSError:
                print("Failed to delete %s. Reason: %s" % (file_path))
    else:
        os.mkdir(cache_folder) 
        
clean_cache()

#2 extract zipfile to cache folder
def cache_zip(zipfile, cachefolder):
    clean_cache()
    with ZipFile(zipfile, 'r') as zipObject:
        zipObject.extractall(cachefolder)

cache_zip(zip_file, cache_folder)

#3 list unzipped files
def cached_files():
    return [entry.path for entry in os.scandir(cache_folder) if entry.is_file()]
cached_files()

#find password in unzipped files list
def find_password(cachedfiles):
    for file in cachedfiles:
        with open(file) as unzippedfile:
            for element in unzippedfile:
                if "password:" in element:
                    start_password = len("password:")+1
                    password = element.strip()[start_password:]
                    return password

print(find_password(cached_files()))

