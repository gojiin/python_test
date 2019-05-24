CREATE TABLE BPS_USERS
-- 사용자 계정별로 파일이 만들어지기 때문에 KOPO2019. 을 붙임. 그런데 지금 해당 계정으로 들어와서 안써도 됨.
(
    username VARCHAR2(20),
    userkey VARCHAR2(20),
    balance number,
    constraint pk_BPS_USER primary key(userkey)
);

-- drop table bps_user;


CREATE TABLE BPS_BLOCK
-- 사용자 계정별로 파일이 만들어지기 때문에 KOPO2019. 을 붙임. 그런데 지금 해당 계정으로 들어와서 안써도 됨.
(
    blockIndex VARCHAR2(20),
    previousHash VARCHAR2(20), 
    blockTimestamp VARCHAR2(20),
    blockdata VARCHAR2(20),
    currentHash VARCHAR2(20),
    proof VARCHAR2(20)
);

CREATE TABLE BPS_TxData
-- 사용자 계정별로 파일이 만들어지기 때문에 KOPO2019. 을 붙임. 그런데 지금 해당 계정으로 들어와서 안써도 됨.
(
    commitYN VARCHAR2(20),
    sender VARCHAR2(20),
    amount number, 
    receiver VARCHAR2(20),
    uuid number,
    txValidity number
);

SELECT * FROM BPS_USERS;
SELECT * FROM BPS_BLOCK;
SELECT * FROM BPS_TxData;

UPDATE BPS_USERS SET BALANCE = BALANCE-500 WHERE USERNAME = 'AA';

INSERT INTO BPS_USERS
--(REGIONID', 'PRODUCTGROUP', YEARWEEK, VOLUME)
VALUES('BB', 'BB', 10000);
-- 오라클에서는 문자는 홑따옴표

INSERT INTO BPS_BLOCK
--(REGIONID', 'PRODUCTGROUP', YEARWEEK, VOLUME)
VALUES('1', 'prehash', 'timestamp', 'blockdata', 'currentHash', 'proof');
-- 오라클에서는 문자는 홑따옴표

INSERT INTO BPS_TxData
--(REGIONID', 'PRODUCTGROUP', YEARWEEK, VOLUME)
VALUES('commitYN', 'AA', 25500, 'CC', 12345, null);
-- 오라클에서는 문자는 홑따옴표


DROP TABLE BPS_TxData;

create table kopo_product_volume_조태엽(
regionid varchar2(20),
productgroup varchar2(20),
yearweek varchar2(8),
volume number not null, -- VOLUME 열에서 숫자값은 NULL값을 허용하지 않는다.
constraint pk_kopo_product_volume_조태엽 primary key(regionid,productgroup, yearweek));

insert into kopo_product_volume_조태엽
VALUES('A01', 'ST0001', '201701', 23);