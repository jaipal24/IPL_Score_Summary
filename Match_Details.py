# This python program reads all the match outcomes and summarizes the information of all the matches.
# Example:
# Input:
# 6
# CSK;RR;loss
# RR;DD;draw
# MI;KKR;win
# KKR;RR;loss
# CSK;DD;draw
# MI;DD;draw
# Output:
# Team: RR, Matches Played: 3, Won: 2, Lost: 0, Draw: 1, Points: 7
# Team: MI, Matches Played: 2, Won: 1, Lost: 0, Draw: 1, Points: 4
# Team: DD, Matches Played: 3, Won: 0, Lost: 0, Draw: 3, Points: 3
# Team: CSK, Matches Played: 2, Won: 0, Lost: 1, Draw: 1, Points: 1
# Team: KKR, Matches Played: 2, Won: 0, Lost: 2, Draw: 0, Points: 0
if __name__ == "__main__":
    # Creating a dictionary to hold the summarized data of the IPL Match.
    summary = {
        "Team": [],
        "Matches Played": [],
        "Won": [],
        "Lost": [],
        "Draw": [],
        "Points": []
    }
    # Reading the number of matches have been played
    matches = int(input())
    # Reading the match results line by line
    for i in range(matches):
        lt = input().split(";")  # Splitting the given input as (Team1,Team2,result) and storing in a list
        if lt[2] == "win":  # If the match result is WIN
            # Team1 is won and Team2 is lost so updating or creating the data based on the result
            if lt[0] not in summary["Team"]:  # If this is the first match for Team1
                summary["Team"].append(lt[0])
                summary["Matches Played"].append(1)
                summary["Won"].append(1)
                summary["Lost"].append(0)
                summary["Draw"].append(0)
                summary["Points"].append(3)
            else:
                ind = summary["Team"].index(lt[0])  # If Team1 have already played matches before
                summary["Matches Played"][ind] += 1
                summary["Won"][ind] += 1
                summary["Points"][ind] += 3
            if lt[1] not in summary["Team"]:  # If this is the first match for Team2
                summary["Team"].append(lt[1])
                summary["Matches Played"].append(1)
                summary["Won"].append(0)
                summary["Lost"].append(1)
                summary["Draw"].append(0)
                summary["Points"].append(0)
            else:
                ind = summary["Team"].index(lt[1])  # If Team2 have already played matches before
                summary["Matches Played"][ind] += 1
                summary["Lost"][ind] += 1
        elif lt[2] == "loss":
            # Team1 is lost and Team2 have won so updating or creating the data based on the result
            if lt[0] not in summary["Team"]:  # If this is the first match for Team1
                summary["Team"].append(lt[0])
                summary["Matches Played"].append(1)
                summary["Won"].append(0)
                summary["Lost"].append(1)
                summary["Draw"].append(0)
                summary["Points"].append(0)
            else:
                ind = summary["Team"].index(lt[0])  # If Team1 have already played matches before
                summary["Matches Played"][ind] += 1
                summary["Lost"][ind] += 1
            if lt[1] not in summary["Team"]:  # If this is the first match for Team2
                summary["Team"].append(lt[1])
                summary["Matches Played"].append(1)
                summary["Won"].append(1)
                summary["Lost"].append(0)
                summary["Draw"].append(0)
                summary["Points"].append(3)
            else:
                ind = summary["Team"].index(lt[1])  # If Team2 have already played matches before
                summary["Matches Played"][ind] += 1
                summary["Won"][ind] += 1
                summary["Points"][ind] += 3
        elif lt[2] == "draw":
            # The match is draw so updating or creating the data based on the result
            if lt[0] not in summary["Team"]:  # If this is the first match for Team1
                summary["Team"].append(lt[0])
                summary["Matches Played"].append(1)
                summary["Won"].append(0)
                summary["Lost"].append(1)
                summary["Draw"].append(1)
                summary["Points"].append(1)
            else:
                ind = summary["Team"].index(lt[0])  # If Team1 have already played matches before
                summary["Matches Played"][ind] += 1
                summary["Draw"][ind] += 1
                summary["Points"][ind] += 1
            if lt[1] not in summary["Team"]:  # If this is the first match for Team2
                summary["Team"].append(lt[1])
                summary["Matches Played"].append(1)
                summary["Won"].append(0)
                summary["Lost"].append(0)
                summary["Draw"].append(1)
                summary["Points"].append(1)
            else:
                ind = summary["Team"].index(lt[1])  # If Team2 have already played matches before
                summary["Matches Played"][ind] += 1
                summary["Draw"][ind] += 1
                summary["Points"][ind] += 1
    # The summary of the matches have been prepared
    temp = []
    keys = list(summary.keys())
    for i in range(len(summary["Team"])):
        max_point = max(list(ele if ele not in temp else -1 for ele in summary["Points"]))
        temp.append(max_point)
        ind = summary["Points"].index(max_point)
        print("{0}: {1},".format(keys[0], summary[keys[0]][ind]), "{0}: {1},".format(keys[1], summary[keys[1]][ind]),
              "{0}: {1},".format(keys[2], summary[keys[2]][ind]), "{0}: {1},".format(keys[3], summary[keys[3]][ind]),
              "{0}: {1},".format(keys[4], summary[keys[4]][ind]), "{0}: {1}".format(keys[5], summary[keys[5]][ind]))
