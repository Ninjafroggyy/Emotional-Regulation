from datalayer.datalayer_mysql import DataLayerRegulationBreak


def display_results(activities_for_zone):
    print("Here are your {} randomly generated activities:".format(len(activities_for_zone)))
    for x in activities_for_zone:
        print(x)
    print("---Thank you for using Regulation Break---")

if __name__ == "__main__":
    user1 = DataLayerRegulationBreak(5)
    zone = input("Choose a zone: blue, green, yellow, red:  ").upper()
    activities_for_zone = user1.all_activities_for_zone_colour(zone)
    if activities_for_zone:
        display_results(activities_for_zone)
    else:
        print("No activites found for {}".format(zone))