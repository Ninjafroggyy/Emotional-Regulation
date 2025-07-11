# This file contains queries used in SQL

# all activities that are in each zone

queryblue = "SELECT regulation_toolbox.activityName FROM activity_zone INNER JOIN activity_type ON activity_zone.act_type_ID=activity_type.act_type_ID INNER JOIN regulation_toolbox ON regulation_toolbox.act_type_ID=activity_type.act_type_ID WHERE zone_ID = 1"

querygreen = "SELECT regulation_toolbox.activityName FROM activity_zone INNER JOIN activity_type ON activity_zone.act_type_ID=activity_type.act_type_ID INNER JOIN regulation_toolbox ON regulation_toolbox.act_type_ID=activity_type.act_type_ID WHERE zone_ID = 2"

queryyellow = "SELECT regulation_toolbox.activityName FROM activity_zone INNER JOIN activity_type ON activity_zone.act_type_ID=activity_type.act_type_ID INNER JOIN regulation_toolbox ON regulation_toolbox.act_type_ID=activity_type.act_type_ID WHERE zone_ID = 3"

queryred = "SELECT regulation_toolbox.activityName FROM activity_zone INNER JOIN activity_type ON activity_zone.act_type_ID=activity_type.act_type_ID INNER JOIN regulation_toolbox ON regulation_toolbox.act_type_ID=activity_type.act_type_ID WHERE zone_ID = 4"


#  number of activites in each zone

countblue = "SELECT COUNT(regulation_toolbox.activityName) FROM activity_zone INNER JOIN activity_type ON activity_zone.act_type_ID=activity_type.act_type_ID INNER JOIN regulation_toolbox ON regulation_toolbox.act_type_ID=activity_type.act_type_ID WHERE zone_ID = 1"