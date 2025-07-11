CREATE DATABASE regulationtoolbox;

USE regulationtoolbox;

CREATE TABLE zones (
zone_ID int NOT NULL,
zone_name varchar(255),
PRIMARY KEY (zone_ID)
);


INSERT INTO zones
VALUES
(1, 'blue'),
(2, 'green'),
(3, 'yellow'),
(4, 'red');

CREATE TABLE activity_type (
act_type_ID int NOT NULL,
act_type_name varchar(255) DEFAULT NULL,
PRIMARY KEY (act_type_ID)
);
  
INSERT INTO activity_type
VALUES 
(1,'breathing'),
(2,'music'),
(3,'dancing'),
(4,'art'),
(5,'games'),
(6,'grounding'),
(7,'movement'),
(8, 'yoga'),
(9, 'talking activities');

CREATE TABLE activity_zone (
act_type_ID int NOT NULL,
zone_ID int,
FOREIGN KEY (act_type_ID) REFERENCES activity_type(act_type_ID),
FOREIGN  KEY (zone_ID) REFERENCES zones(zone_ID)
);

INSERT INTO activity_zone
VALUES
(1, 1),
(1, 2),
(1, 3),
(2, 1),
(2, 4),
(3, 1),
(3, 3),
(3, 4),
(4, 3),
(4, 4),
(5, 3),
(5, 4),
(6, 1),
(6, 2),
(7, 3),
(7, 4),
(7, 2),
(7, 1),
(8, 2),
(8, 3),
(8, 4), 
(9, 1),
(8, 2),
(8, 3)
;




CREATE TABLE regulation_toolbox (
activityID int,
activityName varchar(255) DEFAULT NULL,
act_type_ID int,
PRIMARY KEY (activityID),
FOREIGN KEY (act_type_ID) REFERENCES activity_type(act_type_ID)
);
  
INSERT INTO regulation_toolbox 
VALUES 
(1,'starjumps', 7),
(2,'blow out candle', 1),
(3,'square breathing', 1),
(4,'downward dog pose', 8),
(5, 'tree pose', 8),
(6, 'follow the yoga cards', 8),
(7, 'movement break activities', 7),
(8, 'brain break breathing choice', 1),
(9, 'nature colouring', 4),
(10, 'make a worry box', 4),
(11, 'Emotions board game', 5),
(12, 'Play uno', 5),
(13, 'How would you feel if?', 9),
(14, 'What if scenarios?', 9),
(15, 'Should I say it or not?', 9),
(16, 'Make a worry doll', 4),
(17, 'Make a bag of worries', 4),
(18, 'Make some flash cards', 4),
(19, 'Mindfulness colouring', 4),
(20, 'Self care bingo', 5),
(21, 'Bullet Journal Page', 4),
(22, 'Movement break choices', 7)
;

CREATE TABLE resources
(
resources_ID int,
resources_loc varchar(255),
activityID int,
PRIMARY KEY (resources_ID),
CONSTRAINT fk_activityID
FOREIGN KEY (activityID) REFERENCES regulation_toolbox(activityID)
);

INSERT INTO resources
VALUES
(1, '\Database\Regulation toolbox\Resources\7_Movement\star-jumps-challenge-.pdf', 1),
(2, '\Database\Regulation toolbox\Resources\1_Breathing\SmellTheFlowerBlowOutTheCandles.pdf', 2),
(3, '\Database\Regulation toolbox\Resources\1_Breathing\Square Breathing.pdf', 3),
(4, '\Database\Regulation toolbox\Resources\8_yoga\downward_dog.pdf', 4),
(5, '\Database\Regulation toolbox\Resources\8_yoga\tree pose.pdf', 5),
(6, '\Database\Regulation toolbox\Resources\8_yoga\Yoga Activity Cards.pdf', 6),
(7, '\Database\Regulation toolbox\Resources\7_Movement\movementbreakactivities.pdf', 7),
(8, '\Database\Regulation toolbox\Resources\1_Breathing\brainbreakbreathing.pdf', 8),
(9, '\Database\Regulation toolbox\Resources\4_art\Plant and Nature Colouring.pdf', 9),
(10, '\Database\Regulation toolbox\Resources\4_art\Worry Box.pdf', 10),
(11, '\Database\Regulation toolbox\Resources\5_games\emotionsboardgame.pdf', 11),
(12, '\Database\Regulation toolbox\Resources\5_games\uno.pdf', 12),
(13, '\Database\Regulation toolbox\Resources\9_talking\How would you feel if.pdf', 13),
(14, '\Database\Regulation toolbox\Resources\9_talking\What if scenarios.pdf', 14),
(15, '\Database\Regulation toolbox\Resources\9_talking\should I say it or not.pdf', 15),
(16, '\Database\Regulation toolbox\Resources\4_art\How to Make Your Own Worry Doll.pdf', 16),
(17, '\Database\Regulation toolbox\Resources\4_art\My Bag of Worry and Sadness.pdf', 17),
(18, '\Database\Regulation toolbox\Resources\4_art\Anxiety and Worry Flash Cards.pdf', 18),
(19, '\Database\Regulation toolbox\Resources\4_art\Mindfulness Colouring Sheets.pdf', 19),
(20, '\Database\Regulation toolbox\Resources\5_games\Self-care Bingo.pdf', 20),
(21, '\Database\Regulation toolbox\Resources\4_art\Bullet journal page.pdf', 21),
(22, '\Database\Regulation toolbox\Resources\7_Movement\movementchoice.pdf', 22);

