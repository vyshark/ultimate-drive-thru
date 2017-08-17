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
  PRIMARY KEY (`itemid`),
  KEY `typeid` (`typeid`),
  CONSTRAINT `Menu_ibfk_1` FOREIGN KEY (`typeid`) REFERENCES `type` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

INSERT INTO `Menu` (`itemid`, `typeid`, `item`, `price`) VALUES
(1,	1,	'chicken burger',	'80'),
(2,	1,	'veg burger',	'100'),
(3,	2,	'chicken sandwich',	'60'),
(4,	2,	'king sandwich',	'80'),
(5,	3,	'onion rings',	'40'),
(6,	3,	'hash brown',	'50'),
(7,	4,	'milkshake',	'40'),
(8,	4,	'cola',	'40'),
(9,	4,	'smoothie',	'40'),
(10,	5,	'lettuce',	''),
(11,	5,	'tomato',	''),
(12,	5,	'cheese',	''),
(13,	5,	'mayo',	''),
(14,	5,	'lettuce',	'');

DROP TABLE IF EXISTS `orders`;
CREATE TABLE `orders` (
  `Tid` int(11) NOT NULL,
  `qty` int(11) NOT NULL,
  `item` varchar(30) COLLATE utf8mb4_unicode_ci NOT NULL,
  `comments` varchar(100) COLLATE utf8mb4_unicode_ci NOT NULL,
  `price` int(7) NOT NULL,
  `is_served` tinyint(1) NOT NULL DEFAULT '0',
  `added_on` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

INSERT INTO `orders` (`Tid`, `qty`, `item`, `comments`, `price`, `is_served`, `added_on`) VALUES
(1,	1,	'chicken burger',	'normal',	80,	0,	'0000-00-00 00:00:00'),
(2,	2,	'veg burger',	'normal',	200,	0,	'0000-00-00 00:00:00'),
(4,	1,	'chicken sandwich',	'normal',	60,	0,	'0000-00-00 00:00:00'),
(3,	2,	'smooth',	'norl',	2,	0,	'2017-08-17 09:36:46'),
(5,	5,	'chicken burger',	'fgdg',	3,	0,	'2017-08-17 09:56:11'),
(6,	6,	'chicken sandwich',	'dsfsf',	2,	0,	'2017-08-17 09:56:28'),
(7,	6,	'chicken sandwich',	'dsfd',	3,	0,	'2017-08-17 09:57:01');

DROP TABLE IF EXISTS `transactions`;
CREATE TABLE `transactions` (
  `tid` int(11) NOT NULL AUTO_INCREMENT,
  `bname` varchar(100) COLLATE utf8mb4_unicode_ci NOT NULL,
  `amount` int(30) NOT NULL,
  PRIMARY KEY (`tid`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

INSERT INTO `transactions` (`tid`, `bname`, `amount`) VALUES
(1,	'far',	80),
(2,	'farhann',	200),
(3,	'mashup',	0),
(4,	'hello',	60);

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
(4,	'drinks'),
(5,	'extras');

-- 2017-08-17 12:43:45
