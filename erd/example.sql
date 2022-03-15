INSERT INTO cust VALUES ('1','1','pwd01','James','seoul','id01@naver.com','2022-01-01');
INSERT INTO cust VALUES ('2','2','pwd02','Jason','busan','id02@naver.com','2001-02-02');
INSERT INTO cust VALUES ('3','3','pwd03','Wade','seoul','id03@gmail.com','2002-03-04');
INSERT INTO cust VALUES ('4','4','pwd04','Jennifer','busan','id04@naver.com','2005-05-06');
INSERT INTO cust VALUES ('5','5','pwd05','Emilio','seoul','id05@gmail.com','2009-07-08');
INSERT INTO cust VALUES ('6','6','pwd06','Wanda','busan','id06@gmail.com','2010-09-01');
INSERT INTO cust VALUES ('7','7','pwd07','John','seoul','id07@naver.com','2015-10-01');
INSERT INTO cust VALUES ('8','8','pwd08','Benjamin','incheon','id08@gmail.com','2017-11-01');
INSERT INTO cust VALUES ('9','9','pwd09','Wilma','incheon','id09@naver.com','2019-12-01');
INSERT INTO cust VALUES ('10','10','pwd10','Patricia','incheon','id10@gmail.com','2020-01-01');

INSERT INTO categori VALUES(1, '한식');
INSERT INTO categori VALUES(2, '일식');
INSERT INTO categori VALUES(3, '양식');
INSERT INTO categori VALUES(4, '패스트푸드');
INSERT INTO categori VALUES(5, '디저트');
INSERT INTO categori VALUES(6, '탕류');
INSERT INTO categori VALUES(7, '치킨류');
INSERT INTO categori VALUES(8, '베이커리');
INSERT INTO categori VALUES(9, '야채');
INSERT INTO categori VALUES(10, '피자');

INSERT INTO food VALUES ('1','Friedchicken','1000','2022-01-01');
INSERT INTO food VALUES ('2','seasonedchicken','2000','2022-01-02');
INSERT INTO food VALUES ('3','creampasta','3000','2022-01-03');
INSERT INTO food VALUES ('4','tomatopasta','4000','2022-01-04');
INSERT INTO food VALUES ('5','oilpasta','5000','2022-01-05');
INSERT INTO food VALUES ('6','chocolatecake','6000','2022-01-06');
INSERT INTO food VALUES ('7','strawberrycake','7000','2022-01-07');
INSERT INTO food VALUES ('8','coffee','8000','2022-01-08');
INSERT INTO food VALUES ('9','juice','9000','2022-01-09');
INSERT INTO food VALUES ('10','cookie','10000','2022-01-10');

INSERT INTO food VALUES ('11','Apple','1000','2021-03-11');
INSERT INTO food VALUES ('12','Banana','2000','2021-07-12');
INSERT INTO food VALUES ('13','Watermelon','3000','2021-08-13');
INSERT INTO food VALUES ('14','Melon','4000','2021-11-14');
INSERT INTO food VALUES ('15','Cherry','5000','2021-11-15');
INSERT INTO food VALUES ('16','Mango','6000','2021-01-16');
INSERT INTO food VALUES ('17','Grape','7000','2021-01-17');
INSERT INTO food VALUES ('18','Pear','8000','2021-01-18');
INSERT INTO food VALUES ('19','Strawberry','9000','2021-02-19');
INSERT INTO food VALUES ('20','Pineapple','10000','2021-12-20');

INSERT INTO food VALUES ('21','poundcake','1000','2020-03-01');
INSERT INTO food VALUES ('22','spongecake','2000','2020-05-02');
INSERT INTO food VALUES ('23','chiffoncake','3000','2020-08-03');
INSERT INTO food VALUES ('24','redvelvetcake','4000','2020-07-04');
INSERT INTO food VALUES ('25','carrotcake','5000','2020-04-05');
INSERT INTO food VALUES ('26','sushi','6000','2020-01-06');
INSERT INTO food VALUES ('27','tuna','7000','2020-02-07');
INSERT INTO food VALUES ('28','pudding','8000','2020-06-08');
INSERT INTO food VALUES ('29','pancake','9000','2020-09-09');
INSERT INTO food VALUES ('30','rolls','10000','2020-11-10');

INSERT INTO market VALUES (1,1,1,'음식점1','서초동','2022-03-04','09:00:00','18:00:00','2022-03-01',1);
INSERT INTO market VALUES (2,1,2,'음식점2','한남동','2022-03-04','08:00:00','19:00:00','2022-03-02',2);
INSERT INTO market VALUES (3,1,3,'음식점3','양재동','2022-03-04','04:00:00','20:00:00','2022-03-03',3);
INSERT INTO market VALUES (4,2,4,'음식점4','신원동','2022-03-04','08:00:00','21:00:00','2022-03-04',4);
INSERT INTO market VALUES (5,2,5,'음식점5','내곡동','2022-03-04','08:00:00','22:00:00','2022-03-05',5);
INSERT INTO market VALUES (6,2,6,'음식점6','방배동','2022-03-04','07:00:00','20:00:00','2022-03-06',6);
INSERT INTO market VALUES (7,2,7,'음식점7','반포동','2022-03-04','09:00:00','22:00:00','2022-03-07',7);
INSERT INTO market VALUES (8,3,8,'음식점8','잠원동','2022-03-04','10:00:00','23:00:00','2022-03-08',8);
INSERT INTO market VALUES (9,3,9,'음식점9','서초동','2022-03-04','10:00:00','21:00:00','2022-03-09',9);
INSERT INTO market VALUES (10,4,10,'음식점10','한남동','2022-03-04','10:00:00', '22:00:00','2022-03-10',10);

INSERT INTO ceo VALUES(1,1,'id1','pw1','kim');
INSERT INTO ceo VALUES(2,2,'id2','pw2','jinu');
INSERT INTO ceo VALUES(3,3,'id3','pw3','lee');
INSERT INTO ceo VALUES(4,4,'id4','pw4','no');
INSERT INTO ceo VALUES(5,5,'id5','pw5','oh');
INSERT INTO ceo VALUES(6,6,'id6','pw6','jin');
INSERT INTO ceo VALUES(7,7,'id7','pw7','dam');
INSERT INTO ceo VALUES(8,8,'id8','pw8','ujin');
INSERT INTO ceo VALUES(9,9,'id9','pw9','klove');
INSERT INTO ceo VALUES(10,10,'id10','pw10','good');

INSERT INTO review VALUES(1, 1, 1, 'good', 3.4, '2022-03-04');
INSERT INTO review VALUES(2, 2, 2, 'well', 2.4, '2021-05-05');
INSERT INTO review VALUES(3, 3, 3, 'bad', 1.1, '2018-11-22');
INSERT INTO review VALUES(4, 4, 4, 'great', 4.9, '2024-12-03');
INSERT INTO review VALUES(5, 5, 5, 'so so', 5.0, '2018-07-07');
INSERT INTO review VALUES(6, 6, 6, 'not bad', 3.7, '2020-11-22');
INSERT INTO review VALUES(7, 7, 7, 'good', 4.4, '2022-01-01');
INSERT INTO review VALUES(8, 8, 8, 'best', 3.3, '2022-01-14');
INSERT INTO review VALUES(9, 9, 9, 'good', 2.1, '2021-12-22');
INSERT INTO review VALUES(10, 10, 10, 'bad', 1.2, '2022-03-01');


INSERT INTO reply VALUES(1, 1, 1, 'good', '2022-03-04');
INSERT INTO reply VALUES(2, 2, 2, 'well', '2022-01-14');
INSERT INTO reply VALUES(3, 3, 3, 'bad', '2022-02-17');
INSERT INTO reply VALUES(4, 4, 4, 'so so', '2020-12-25');
INSERT INTO reply VALUES(5, 5, 5, 'good', '2019-07-24');
INSERT INTO reply VALUES(6, 6, 6, 'not bad', '2020-07-07');
INSERT INTO reply VALUES(7, 7, 7, 'great', '2018-11-08');
INSERT INTO reply VALUES(8, 8, 8, 'good', '2020-05-05');
INSERT INTO reply VALUES(9, 9, 9, 'great', '2020-03-20');
INSERT INTO reply VALUES(10, 10, 10, 'bad', '2022-03-04');
