# 5천원 이하의 음식점 이름과 음식과 음식의 가격  조회
SELECT m.marketname, f.price, f.name 
FROM market m
INNER JOIN food f
ON m.foodid = f.foodid
WHERE f.price <= 5000;

# 서초동에 위치한 가게 이름과 음식이름, 음식가격  조회
SELECT m.marketname , f.price, f.name 
FROM market m
INNER JOIN food f
ON m.foodid = f.foodid
WHERE marketaddress = '서초동';
 
#음식점 이름이' 음식점 1'인 음식점 가게 이름과 음식이름, 음식가격 조회
SELECT m.marketname, f.price, f.name
FROM market m
INNER JOIN food f
ON m.foodid = f.foodid
WHERE marketname = '음식점1';

#마감 시간이 22시 이후인 음식점 이름 검색
SELECT marketname
FROM market
WHERE DATE_FORMAT(close, '%H'  ) > 22;

# 휴무일이 이번주  금요일인  가게 이름 조회
SELECT marketname
FROM market
WHERE DATE_FORMAT(holiday,'%Y%m%d') = DATE_FORMAT(CURDATE()- (WEEKDAY(CURDATE()) + 5), '%Y%m%d');

# 휴무일이 오늘인 가게 조회 
SELECT marketname ,holiday 
FROM market
WHERE DATE_FORMAT(holiday,'%Y%m%d')  = DATE_FORMAT(CURDATE(),'%Y%m%d');

# 평균 리뷰가 높은 가게와 평균 리뷰 점수를  순서대로 9개 조회

SELECT marketname ,avg(r.star) 
FROM review r
INNER JOIN market m
ON m.marketno = r.marketno
INNER JOIN reply s
ON r.reviewno = s.replyid
GROUP BY m.marketno
ORDER BY avg(r.star) 
DESC LIMIT 9;

# 양식인 음식점을 조회하시오
SELECT * FROM market m
INNER JOIN categori c
ON m.cid = c.cid
WHERE categoriname = '양식';
