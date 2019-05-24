CREATE TABLE BPS_USERS
-- ����� �������� ������ ��������� ������ KOPO2019. �� ����. �׷��� ���� �ش� �������� ���ͼ� �Ƚᵵ ��.
(
    username VARCHAR2(20),
    userkey VARCHAR2(20),
    balance number,
    constraint pk_BPS_USER primary key(userkey)
);

-- drop table bps_user;


CREATE TABLE BPS_BLOCK
-- ����� �������� ������ ��������� ������ KOPO2019. �� ����. �׷��� ���� �ش� �������� ���ͼ� �Ƚᵵ ��.
(
    blockIndex VARCHAR2(20),
    previousHash VARCHAR2(20), 
    blockTimestamp VARCHAR2(20),
    blockdata VARCHAR2(20),
    currentHash VARCHAR2(20),
    proof VARCHAR2(20)
);

CREATE TABLE BPS_TxData
-- ����� �������� ������ ��������� ������ KOPO2019. �� ����. �׷��� ���� �ش� �������� ���ͼ� �Ƚᵵ ��.
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
-- ����Ŭ������ ���ڴ� Ȭ����ǥ

INSERT INTO BPS_BLOCK
--(REGIONID', 'PRODUCTGROUP', YEARWEEK, VOLUME)
VALUES('1', 'prehash', 'timestamp', 'blockdata', 'currentHash', 'proof');
-- ����Ŭ������ ���ڴ� Ȭ����ǥ

INSERT INTO BPS_TxData
--(REGIONID', 'PRODUCTGROUP', YEARWEEK, VOLUME)
VALUES('commitYN', 'AA', 25500, 'CC', 12345, null);
-- ����Ŭ������ ���ڴ� Ȭ����ǥ


DROP TABLE BPS_TxData;

create table kopo_product_volume_���¿�(
regionid varchar2(20),
productgroup varchar2(20),
yearweek varchar2(8),
volume number not null, -- VOLUME ������ ���ڰ��� NULL���� ������� �ʴ´�.
constraint pk_kopo_product_volume_���¿� primary key(regionid,productgroup, yearweek));

insert into kopo_product_volume_���¿�
VALUES('A01', 'ST0001', '201701', 23);