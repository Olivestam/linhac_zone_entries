import csv

subset_data = []
subset_data_with_split = []
opposingteamid_index = 2
xg_index = 8
compiledgametime_index = 9
event_index = 10
type_index = 19
teamid_index = 5
outcome_index = 14
manpowersituation_index = 12
x_cord = 20
y_cord = 21
attacking_team = ''
sequence_id = -1
index = -1
cleaned_row = []
last_row = []
second_last_row = []
save_row = 0
entry = False
zone = ''

with open('Linhac_df_keyed_20_games.csv', 'r') as file:
    reader = csv.reader(file)
    append = False
    first_row = True
    for row in reader:
        index += 1
        if first_row:
            subset_data.append([row[opposingteamid_index], row[teamid_index], row[xg_index], row[compiledgametime_index], row[event_index], 
                           row[manpowersituation_index], row[outcome_index], row[type_index], 'zone', 'goal', 'sequence_id'])
            subset_data_with_split.append([row[opposingteamid_index], row[teamid_index], row[xg_index], row[compiledgametime_index], row[event_index], 
                           row[manpowersituation_index], row[outcome_index], row[type_index], 'zone', 'goal', 'sequence_id'])
            first_row = False
            continue
        if (row[teamid_index] == attacking_team) and ((float(row[x_cord]) <= 54)):
            if (float(row[y_cord]) >= 22) or  (float(row[y_cord]) <= -22):
                zone = 'upperWide'
            else:
                zone = 'upperMiddle'
        if (row[teamid_index] != attacking_team) and ((float(row[x_cord]) >= -54)):
            if (float(row[y_cord]) >= 22) or  (float(row[y_cord]) <= -22):
                zone = 'upperWide'
            else:
                zone = 'upperMiddle'
        if (row[teamid_index] == attacking_team) and ((float(row[x_cord]) > 54)) and ((float(row[x_cord]) < 89)):
            if (float(row[y_cord]) > 22) or  (float(row[y_cord]) < -22):
                zone = 'middleWide'
            else:
                zone = 'slot'
        if (row[teamid_index] != attacking_team) and ((float(row[x_cord]) < -54)) and ((float(row[x_cord]) > -89)):
            if (float(row[y_cord]) > 22) or  (float(row[y_cord]) < -22):
                zone = 'middleWide'
            else:
                zone = 'slot'
        if (row[teamid_index] == attacking_team) and ((float(row[x_cord]) >= 89)):
            zone = 'behindGoalCrease'
        if (row[teamid_index] != attacking_team) and ((float(row[x_cord]) <= -89)):
            zone = 'behindGoalCrease'
        if (row[teamid_index] == attacking_team) and (float(row[x_cord]) < 24.5) and (append == True):
            subset_data_with_split.append(['', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', ''])
            append = False
        if (row[teamid_index] != attacking_team) and (float(row[x_cord]) > -25.5) and (append == True):
            subset_data_with_split.append(['', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', ''])
            append = False
        if ((row[event_index] == 'controlledentry') or (row[event_index] == 'dumpin')) and (row[outcome_index] == 'successful') and (append == False):
            append = True
            entry = True
            y_coordinate = float(row[y_cord])
            attacking_team = row[teamid_index]
            sequence_id += 1
        if append:
            if entry:
                if (row[event_index] == 'controlledentry') and ('carry' in row[type_index]):
                    if (y_coordinate < 22 and y_coordinate > -22):
                        row[type_index] = 'middleCarry'
                    elif (y_coordinate >= 22):
                        row[type_index] = 'rightCarry'
                    else:
                        row[type_index] = 'leftCarry'
                elif (row[event_index] == 'controlledentry') and ('pass' in row[type_index]):
                    if abs(second_last_row - y_coordinate) > 42.5:
                        row[type_index] = 'widePass'
                    else:
                        row[type_index] = 'shortPass'
                elif (row[event_index] == 'dumpin'):
                    row[type_index] = 'dump'

                if row[xg_index] == '':
                    row[xg_index] = '0.0'
                """ cleaned_row = [row[opposingteamid_index], row[teamid_index], row[xg_index], row[compiledgametime_index], row[event_index], 
                            row[manpowersituation_index], row[outcome_index], row[type_index], row[x_cord], row[y_cord], 0, str(sequence_id)] """
                cleaned_row = [row[opposingteamid_index], row[teamid_index], row[xg_index], row[compiledgametime_index], row[event_index], 
                            row[manpowersituation_index], row[outcome_index], row[type_index], zone, 0, str(sequence_id), row[x_cord], row[y_cord]]
                subset_data.append(cleaned_row)
                subset_data_with_split.append(cleaned_row)
                entry = False
            else:  
                if row[xg_index] == '':
                    row[xg_index] = '0.0'
                if row[event_index] == 'goal':
                    """ cleaned_row = [row[opposingteamid_index], row[teamid_index], row[xg_index], row[compiledgametime_index], row[event_index], 
                            row[manpowersituation_index], row[outcome_index], row[type_index], row[x_cord], row[y_cord], 1, str(sequence_id)] """
                    cleaned_row = [row[opposingteamid_index], row[teamid_index], row[xg_index], row[compiledgametime_index], row[event_index], 
                            row[manpowersituation_index], row[outcome_index], row[type_index], zone, 0, str(sequence_id), row[x_cord], row[y_cord]]
                else:
                    """ cleaned_row = [row[opposingteamid_index], row[teamid_index], row[xg_index], row[compiledgametime_index], row[event_index], 
                                row[manpowersituation_index], row[outcome_index], row[type_index], row[x_cord], row[y_cord], 0, str(sequence_id)] """
                    cleaned_row = [row[opposingteamid_index], row[teamid_index], row[xg_index], row[compiledgametime_index], row[event_index], 
                            row[manpowersituation_index], row[outcome_index], row[type_index], zone, 0, str(sequence_id), row[x_cord], row[y_cord]]
                subset_data.append(cleaned_row)
                subset_data_with_split.append(cleaned_row)

        second_last_row = last_row
        last_row = float(row[y_cord])

file_path = "linhac_subset_data_new.csv"

with open(file_path, mode='w', newline='') as file:

    # Create a CSV writer object
    writer = csv.writer(file)

    # Write each list in the main list to a row in the CSV file
    for row in subset_data:
        writer.writerow(row)

file_path = "linhac_subset_data_split.csv"

with open(file_path, mode='w', newline='') as file:

    # Create a CSV writer object
    writer = csv.writer(file)

    # Write each list in the main list to a row in the CSV file
    for row in subset_data_with_split:
        writer.writerow(row)
