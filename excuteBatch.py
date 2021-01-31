import sys
import os
import shutil

# Get prams
# fields
paramList = sys.argv 
categoryList = ['Commision', 'Original creation' , 'Seconde creation']
result = 1

# Using readlines 
routeTxt = open('route.txt', 'r')
lines = routeTxt.readlines()

ans = input('Do you want to new route? (Y/N)') 
if (ans == 'Y' or ans == 'y'):
    defaultRoute = input('Input new route') 
    defaultTemplate = input('Input new template route') 
    defaultPureref = input('Input new pureref route') 
    defaultClips = input('Input new clips route') 
else:
    defaultRoute = lines[0].strip()
    defaultTemplate = lines[1].strip()
    defaultPureref = lines[2].strip()
    defaultClips = lines[3].strip()

# Main proccess
try:
    if len(paramList) > 2: 
        if (paramList[2] not in categoryList):
            result = 0
    else:
        print('No parameter has benn included')

    if (result == 0 ):
        print('Please input correct category')
        sys.exit()
    else:
        # Make top-level folder
        route = defaultRoute + paramList[2] + '/' + paramList[1]
        print('top-level folder making complate')
        print('top-level folder route: '+ route)
        os.makedirs(route)

        # Make second-level folder
        if (os.path.exists(route)):
            folderNameSecond = ['Working files', 'Output', 'Document', 'Reference']
            for name in folderNameSecond:
                os.makedirs(route + '/' + name)

            print('second-level folder making complate')

            # Copy teplate files (document, pureref, clip)
            newTemplateName = route + '/' + 'Document/' + paramList[1] + '_template.xlsx'
            shutil.copy(defaultTemplate, newTemplateName)

            newSceneName = route + '/' + 'Reference/' + paramList[1] + '_pureref.pur'
            shutil.copy(defaultPureref, newSceneName)

            newClipName = route + '/' + 'Working files/' + paramList[1] + '_clip.clip'
            shutil.copy(defaultClips, newClipName)
            
            print('Copy files complate')
        else:
            print('file path not exist')

except Exception as err:
    # print errors
    print(str(err))

    # remove making tree
    if len(paramList) > 2:
        shutil.rmtree(defaultRoute + paramList[2] + '/' + paramList[1])
