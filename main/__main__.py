import requests


def selectProgram():
    res = requests.get(url= BASE_URL + '/programs')
    programs = res.json()['result']['data']
    
    i = 0
    for program in programs :
        print(str(i+1) + " - " + program['name'])
        i = i + 1
        
    print('')
    progSelection = input('Please select a program (1 - ' + str(i) + ') : ')
    while not testInput(progSelection, i):
        progSelection = input('Invalid selection. Try again (1 - ' + str(i) + ') : ')
    
    return programs[int(progSelection) - 1]

def selectTrial(programDbId):
    res = requests.get(url= BASE_URL + '/trials', params= {'programDbId': programDbId})
    trials = res.json()['result']['data']

    if len(trials) == 0 :
        return None
    elif len(trials) == 1 :
        return trials[0]
    else:
        i = 0
        for trial in trials :
            if trial['active'] : 
                activeStr = 'Active' 
            else : 
                activeStr = 'Inactive'
            print(str(i+1) + " - (" + activeStr + ') ' + trial['trialName'] )
            i = i + 1
            
        print('')
        trialSelection = input('Please select a trial (1 - ' + str(i) + ') : ')
        while not testInput(trialSelection, i):
            trialSelection = input('Invalid selection. Try again (1 - ' + str(i) + ') : ')
            
        return trials[int(trialSelection) - 1]
        
def printStudies(trial):
    if trial is None :
        print('Sorry, no studies found')
    elif 'studies' not in trial :
        print('Sorry, no studies found')
    elif len(trial['studies']) == 0:
        print('Sorry, no studies found')
    else:
        studies = trial['studies']
        print('')
        print('Here are your available studies')
        print('')
        print('ID\t|\tName')
        for study in studies :
            print(study['studyDbId'] + "\t|\t" + study['studyName'] )
        print('')
            
def testInput(strVal, maxVal):
    try:
        intVal = int(strVal)
    except:
        return False
    return intVal > 0 and intVal <= maxVal
    
def run():
    print('Welcome to the BrAPI Hackathon Demo Client App!!')
    program = selectProgram()
    trial = selectTrial(program['programDbId'])
    printStudies(trial)

##BASE_URL = 'https://test-server.brapi.org/brapi/v1'
BASE_URL = 'https://test-server.brapi.org/brapi/v1'
again = 'y'
while again == 'y':
    run()
    again = input('Again? (y/n) : ')
