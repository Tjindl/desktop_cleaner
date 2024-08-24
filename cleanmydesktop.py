import os
dir = input('Enter the directory folder after root user: ')

directory = '/Users/tusharjindal/' + dir
os.makedirs(directory + '/Images', exist_ok=True)
os.makedirs(directory + '/Docs', exist_ok=True)
os.makedirs(directory + '/Videos', exist_ok=True)

for name in os.listdir(directory):
    if name.endswith('.png'):
        os.rename(os.path.join(directory, name), os.path.join(directory, 'Images', name))
    elif name.endswith('.jpg'):
        os.rename(os.path.join(directory, name), os.path.join(directory, 'Images', name))
    elif name.endswith('.jpeg'):
        os.rename(os.path.join(directory, name), os.path.join(directory, 'Images', name))
    elif name.endswith('.docx'):
        os.rename(os.path.join(directory, name), os.path.join(directory, 'Docs', name))
    elif name.endswith('.pdf'):
        os.rename(os.path.join(directory, name), os.path.join(directory, 'Docs', name))
    elif name.endswith('.txt'):
        os.rename(os.path.join(directory, name), os.path.join(directory, 'Docs', name))
    elif name.endswith('.pptx'):
        os.rename(os.path.join(directory, name), os.path.join(directory, 'Docs', name))
    elif name.endswith('.xlsx'):
        os.rename(os.path.join(directory, name), os.path.join(directory, 'Docs', name))
    elif name.endswith('.csv'):
        os.rename(os.path.join(directory, name), os.path.join(directory, 'Docs', name))
    elif name.endswith('.doc'):
        os.rename(os.path.join(directory, name), os.path.join(directory, 'Docs', name))
    elif name.endswith('.xls'):
        os.rename(os.path.join(directory, name), os.path.join(directory, 'Docs', name))
    elif name.endswith('.ppt'):
        os.rename(os.path.join(directory, name), os.path.join(directory, 'Docs', name))
    elif name.endswith('.zip'):
        os.rename(os.path.join(directory, name), os.path.join(directory, 'Docs', name))
    elif name.endswith('.rar'):
        os.rename(os.path.join(directory, name), os.path.join(directory, 'Docs', name))
    elif name.endswith('.7z'):
        os.rename(os.path.join(directory, name), os.path.join(directory, 'Docs', name))
    elif name.endswith('.tar'):
        os.rename(os.path.join(directory, name), os.path.join(directory, 'Docs', name))
    elif name.endswith('.gz'):
        os.rename(os.path.join(directory, name), os.path.join(directory, 'Docs', name))
    elif name.endswith('.txt'):
        os.rename(os.path.join(directory, name), os.path.join(directory, 'Docs', name))
    elif name.endswith('.html'):
        os.rename
    elif name.endswith('.mov'):
        os.rename(os.path.join(directory, name), os.path.join(directory, 'Videos', name))
# for name in os.listdir(directory):
#     if name.endswith('.png'):
        

        # os.remove(os.path.join(directory, filename))