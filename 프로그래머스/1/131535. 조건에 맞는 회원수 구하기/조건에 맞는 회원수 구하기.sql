-- 코드를 입력하세요
SELECT COUNT(USER_ID) AS USERS FROM USER_INFO WHERE YEAR(joined) = '2021' AND age >= 20 and age <= 29;