import os
edited_folder = "C:/Users/Nathan/Desktop/Voice_AI/Files/Edited/06"


paths = (os.path.join(root, filename)
        for root, _, filenames in os.walk(edited_folder)
        for filename in filenames)

for path in paths:
    # the '#' in the example below will be replaced by the '-' in the filenames in the directory
    newname = path.replace('enhanced', 'edited')
    if newname != path:
        os.rename(path, newname)