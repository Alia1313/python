from pathlib import Path
import shutil
name=input()
files=list(Path(name).glob('*'))
if len(files)>0:
    cnt=0
    for i in range(len(files)):
        if not files[i].is_dir() and files[i].stat().st_size<2048:
            print(files[i].name)
            cnt+=1
    if cnt>0:
        Path('small').mkdir(exist_ok=True)
        for i in range(len(files)):
            if not files[i].is_dir() and files[i].stat().st_size < 2048:
                my_file = Path(name+'/'+files[i].name)
                to_file = Path('small')
                shutil.copy(my_file, to_file)

else:
    print('Файлов нет')
