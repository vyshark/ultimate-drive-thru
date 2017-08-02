-- Adminer 4.3.1 MySQL dump

SET NAMES utf8;
SET time_zone = '+00:00';
SET foreign_key_checks = 0;
SET sql_mode = 'NO_AUTO_VALUE_ON_ZERO';

SET NAMES utf8mb4;

CREATE DATABASE `ultimate_drive_thru` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci */;
USE `ultimate_drive_thru`;

DROP TABLE IF EXISTS `Menu`;
CREATE TABLE `Menu` (
  `itemid` int(11) NOT NULL AUTO_INCREMENT,
  `typeid` int(11) NOT NULL,
  `item` varchar(100) COLLATE utf8mb4_unicode_ci NOT NULL,
  `price` varchar(50) COLLATE utf8mb4_unicode_ci NOT NULL,
  `lettuce` tinyint(1) NOT NULL DEFAULT '0',
  `tomato` tinyint(1) NOT NULL DEFAULT '0',
  `cheese` tinyint(1) NOT NULL DEFAULT '0',
  `chicken` tinyint(1) NOT NULL DEFAULT '0',
  `mayo` tinyint(1) NOT NULL DEFAULT '0',
  `pickle` tinyint(1) NOT NULL DEFAULT '0',
  PRIMARY KEY (`itemid`),
  KEY `typeid` (`typeid`),
  CONSTRAINT `Menu_ibfk_1` FOREIGN KEY (`typeid`) REFERENCES `type` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

INSERT INTO `Menu` (`itemid`, `typeid`, `item`, `price`, `lettuce`, `tomato`, `cheese`, `chicken`, `mayo`, `pickle`) VALUES
(1,	1,	'chicken burger',	'80',	1,	1,	0,	1,	0,	0),
(2,	1,	'veg burger',	'100',	1,	1,	1,	0,	1,	1),
(3,	2,	'chicken sandwich',	'60',	0,	1,	0,	1,	1,	0),
(4,	2,	'king sandwich',	'80',	1,	1,	1,	1,	1,	1),
(5,	3,	'onion rings',	'40',	0,	0,	0,	0,	0,	0),
(6,	3,	'hash brown',	'50',	0,	0,	0,	0,	0,	0),
(7,	4,	'milkshake',	'40',	0,	0,	0,	0,	0,	0),
(8,	4,	'cola',	'40',	0,	0,	0,	0,	0,	0),
(9,	4,	'smoothie',	'40',	0,	0,	0,	0,	0,	0);

DROP TABLE IF EXISTS `Orders`;
CREATE TABLE `Orders` (
  `orderid` int(11) NOT NULL AUTO_INCREMENT,
  `itemid` int(11) NOT NULL,
  `quantity` int(11) NOT NULL,
  `size` varchar(1) COLLATE utf8mb4_unicode_ci NOT NULL,
  `comment` varchar(100) COLLATE utf8mb4_unicode_ci NOT NULL,
  PRIMARY KEY (`orderid`),
  KEY `itemid` (`itemid`),
  CONSTRAINT `Orders_ibfk_1` FOREIGN KEY (`itemid`) REFERENCES `Menu` (`itemid`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;


DROP TABLE IF EXISTS `Transactions`;
CREATE TABLE `Transactions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `orderid` int(11) NOT NULL,
  `total` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `orderid` (`orderid`),
  CONSTRAINT `Transactions_ibfk_1` FOREIGN KEY (`id`) REFERENCES `type` (`id`),
  CONSTRAINT `Transactions_ibfk_2` FOREIGN KEY (`orderid`) REFERENCES `Orders` (`orderid`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;


DROP TABLE IF EXISTS `type`;
CREATE TABLE `type` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `Category` varchar(50) COLLATE utf8mb4_unicode_ci NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

INSERT INTO `type` (`id`, `Category`) VALUES
(1,	'burger'),
(2,	'sandwich'),
(3,	'fries'),
(4,	'drinks');

-- 2017-08-02 14:07:04
