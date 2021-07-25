import tarfile 
from tqdm import tqdm #pip install tqdm
def decompress(tar_file,path,members=None):
    tar = tarfile.open(tar_file,mode="r:gz")
    if members is None:
        members = tar.getmembers()

#with progress bar
#set progress bar
    progress = tqdm(members)
    for member in progress:
        tar.extract(member,path=path)
        #set the progress description of progress bar
        progress.set_description(f"Extracting {member.name}")
    tar.close()

decompress("compressed1.tar.gz","where to extract it")