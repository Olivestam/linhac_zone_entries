import csv

index = {
'opposingteamid' : 0,
'teamid' : 1,
'xg' : 2,
'compiledgametime' : 3,
'eventname' : 4,
'manpowersituation' : 5,
'outcome' : 6,
'type' : 7,
'xadjcoord' : 8,
'yadjcoord' : 9,
'goal' : 10,
'sequence_id' : 11
}

total = {
    'entries' : 0,
    'goals' : 0,
    'shots' : 0
}
carryLeft = {
    'entries' : 0,
    'shots' : 0,
    'goals' : 0,
    'xg' : []
}
carryRight = {
    'entries' : 0,
    'shots' : 0,
    'goals' : 0,
    'xg' : []
}
carryMiddle = {
    'entries' : 0,
    'shots' : 0,
    'goals' : 0,
    'xg' : []
}
widePass = {
    'entries' : 0,
    'shots' : 0,
    'goals' : 0,
    'xg' : []
}
shortPass = {
    'entries' : 0,
    'shots' : 0,
    'goals' : 0,
    'xg' : []
}
dumpIn = {
    'entries' : 0,
    'shots' : 0,
    'goals' : 0,
    'xg' : []
}
currentEntry = ''

with open('linhac_subset_data_new.csv', 'r') as file:
    reader = csv.reader(file)
    append = False
    first_row = True
    for row in reader:
        if first_row:
            first_row = False
            continue
        if ((row[index['eventname']] == 'controlledentry') or (row[index['eventname']] == 'dumpin')) and (row[index['outcome']] == 'successful'):
            if row[index['type']] == 'leftCarry':
                currentEntry = row[index['type']]
                carryLeft['entries'] += 1
                total['entries'] += 1
            elif row[index['type']] == 'middleCarry':
                currentEntry = row[index['type']]
                carryMiddle['entries'] += 1
                total['entries'] += 1
            elif row[index['type']] == 'rightCarry':
                currentEntry = row[index['type']]
                carryRight['entries'] += 1
                total['entries'] += 1
            elif row[index['type']] == 'widePass':
                currentEntry = row[index['type']]
                widePass['entries'] += 1
                total['entries'] += 1
            elif row[index['type']] == 'shortPass':
                currentEntry = row[index['type']]
                shortPass['entries'] += 1
                total['entries'] += 1
            elif row[index['type']] == 'dump':
                currentEntry = row[index['type']]
                dumpIn['entries'] += 1
                total['entries'] += 1
        else:
            if currentEntry == 'leftCarry':
                if (row[index['eventname']] == 'shot') and (row[index['outcome']] == 'successful'):
                    carryLeft['shots'] += 1
                    carryLeft['xg'].append(float(row[index['xg']]))
                    total['shots'] += 1
                if (row[index['eventname']] == 'goal') and (row[index['outcome']] == 'successful'):
                    carryLeft['goals'] += 1
                    total['goals'] += 1
            elif currentEntry == 'middleCarry':
                if (row[index['eventname']] == 'shot') and (row[index['outcome']] == 'successful'):
                    carryMiddle['shots'] += 1
                    carryMiddle['xg'].append(float(row[index['xg']]))
                    total['shots'] += 1
                if (row[index['eventname']] == 'goal') and (row[index['outcome']] == 'successful'):
                    carryMiddle['goals'] += 1
                    total['goals'] += 1
            elif currentEntry == 'rightCarry':
                if (row[index['eventname']] == 'shot') and (row[index['outcome']] == 'successful'):
                    carryRight['shots'] += 1
                    carryRight['xg'].append(float(row[index['xg']]))
                    total['shots'] += 1
                if (row[index['eventname']] == 'goal') and (row[index['outcome']] == 'successful'):
                    carryRight['goals'] += 1
                    total['goals'] += 1
            elif currentEntry == 'widePass':
                if (row[index['eventname']] == 'shot') and (row[index['outcome']] == 'successful'):
                    widePass['shots'] += 1
                    widePass['xg'].append(float(row[index['xg']]))
                    total['shots'] += 1
                if (row[index['eventname']] == 'goal') and (row[index['outcome']] == 'successful'):
                    widePass['goals'] += 1
                    total['goals'] += 1
            elif currentEntry == 'shortPass':
                if (row[index['eventname']] == 'shot') and (row[index['outcome']] == 'successful'):
                    shortPass['shots'] += 1
                    shortPass['xg'].append(float(row[index['xg']]))
                    total['shots'] += 1
                if (row[index['eventname']] == 'goal') and (row[index['outcome']] == 'successful'):
                    shortPass['goals'] += 1
                    total['goals'] += 1
            elif currentEntry == 'dump':
                if (row[index['eventname']] == 'shot') and (row[index['outcome']] == 'successful'):
                    dumpIn['shots'] += 1
                    dumpIn['xg'].append(float(row[index['xg']]))
                    total['shots'] += 1
                if (row[index['eventname']] == 'goal') and (row[index['outcome']] == 'successful'):
                    dumpIn['goals'] += 1
                    total['goals'] += 1
    print('PROCENTAGE OF ALL ENTRIES:')
    print('Procentage of carryWide entries:', ((carryLeft['entries']+carryRight['entries'])/total['entries']))
    print('Procentage of carryMiddle entries:', (carryMiddle['entries']/total['entries']))
    print('Procentage of carryRight entries:', (carryRight['entries']/total['entries']))
    print('Procentage of widePass entries:', (widePass['entries']/total['entries']))
    print('Procentage of shortPass entries:', (shortPass['entries']/total['entries']))
    print('Procentage of dumpIn entries:', (dumpIn['entries']/total['entries']))

    print('')

    print('PROCENTAGE OF SHOTS:')
    print('CarryWide:', ((carryLeft['shots']+carryRight['shots'])/(carryLeft['entries']+carryRight['entries'])))
    print('CarryMiddle:', (carryMiddle['shots']/carryMiddle['entries']))
    print('CarryRight:', (carryRight['shots']/carryRight['entries']))
    print('WidePass:', (widePass['shots']/widePass['entries']))
    print('ShortPass:', (shortPass['shots']/shortPass['entries']))
    print('DumpIn:', (dumpIn['shots']/dumpIn['entries']))


    print('')

    print('AVARAGE XG:')
    print('CarryWide:', ((sum(carryLeft['xg'])+sum(carryRight['xg']))/(len(carryLeft['xg'])+len(carryRight['xg']))))
    print('CarryMiddle:', (sum(carryMiddle['xg'])/len(carryMiddle['xg'])))
    print('CarryRight:', (sum(carryRight['xg'])/len(carryRight['xg'])))
    print('WidePass:', (sum(widePass['xg'])/len(widePass['xg'])))
    print('ShortPass:', (sum(shortPass['xg'])/len(shortPass['xg'])))
    print('DumpIn:', (sum(dumpIn['xg'])/len(dumpIn['xg'])))

    print('')

    print('PROCENTAGE OF GOALS:')
    print('CarryWide:', ((carryLeft['goals']+carryRight['goals'])/(carryLeft['entries']+carryRight['entries'])))
    print('CarryMiddle:', (carryMiddle['goals']/carryMiddle['entries']))
    print('CarryRight:', (carryRight['goals']/carryRight['entries']))
    print('WidePass:', (widePass['goals']/widePass['entries']))
    print('ShortPass:', (shortPass['goals']/shortPass['entries']))
    print('DumpIn:', (dumpIn['goals']/dumpIn['entries']))

print(total['goals'], total['shots'])