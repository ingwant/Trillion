/*
 Navicat Premium Data Transfer

 Source Server         : localhost
 Source Server Type    : MySQL
 Source Server Version : 50726
 Source Host           : localhost:3306
 Source Schema         : trillion

 Target Server Type    : MySQL
 Target Server Version : 50726
 File Encoding         : 65001

 Date: 26/01/2021 14:47:38
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for changeline
-- ----------------------------
DROP TABLE IF EXISTS `changeline`;
CREATE TABLE `changeline`  (
  `IEMI` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `changetime` timestamp(0) NULL DEFAULT NULL ON UPDATE CURRENT_TIMESTAMP(0),
  `bool` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `id` int(11) NOT NULL AUTO_INCREMENT,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 25 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Table structure for forinventory
-- ----------------------------
DROP TABLE IF EXISTS `forinventory`;
CREATE TABLE `forinventory`  (
  `id` int(11) NOT NULL,
  `inflag` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  INDEX `inflag`(`inflag`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Table structure for incompany
-- ----------------------------
DROP TABLE IF EXISTS `incompany`;
CREATE TABLE `incompany`  (
  `idcompany` int(10) UNSIGNED NOT NULL,
  `incompany` varchar(45) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  PRIMARY KEY (`idcompany`) USING BTREE,
  INDEX `incompany`(`incompany`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of incompany
-- ----------------------------
INSERT INTO `incompany` VALUES (1, 'AT&T');
INSERT INTO `incompany` VALUES (3, 'Other');
INSERT INTO `incompany` VALUES (2, 'T-Mobile');

-- ----------------------------
-- Table structure for infotemplate
-- ----------------------------
DROP TABLE IF EXISTS `infotemplate`;
CREATE TABLE `infotemplate`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `IEMI` varchar(45) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `istorage` varchar(45) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `color` varchar(45) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `company` varchar(45) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `intime` varchar(45) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `outtime` varchar(45) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `grade` varchar(45) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `selller` varchar(45) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `bstorage` varchar(45) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `tocompany` varchar(45) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `tracknumber` varchar(45) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `salenumber` varchar(45) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `remarks` varchar(45) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `productlines` varchar(45) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `forinventory` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE INDEX `id_UNIQUE`(`id`) USING BTREE,
  UNIQUE INDEX `IEMI_UNIQUE`(`IEMI`) USING BTREE,
  INDEX `iphonestorage`(`istorage`) USING BTREE,
  INDEX `iphonecolor`(`color`) USING BTREE,
  INDEX `incompany`(`company`) USING BTREE,
  INDEX `outcompany`(`tocompany`) USING BTREE,
  INDEX `productlines`(`productlines`) USING BTREE,
  INDEX `forinventory`(`forinventory`) USING BTREE,
  CONSTRAINT `incompany` FOREIGN KEY (`company`) REFERENCES `incompany` (`incompany`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  CONSTRAINT `iphonecolor` FOREIGN KEY (`color`) REFERENCES `iphonecolor` (`iphonecolor`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  CONSTRAINT `iphonestorage` FOREIGN KEY (`istorage`) REFERENCES `iphonestorage` (`iphonestorage`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  CONSTRAINT `productlines` FOREIGN KEY (`productlines`) REFERENCES `productlines` (`productlines`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE = InnoDB AUTO_INCREMENT = 2 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Table structure for iphone11
-- ----------------------------
DROP TABLE IF EXISTS `iphone11`;
CREATE TABLE `iphone11`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `IEMI` varchar(45) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `istorage` varchar(45) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `color` varchar(45) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `company` varchar(45) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `intime` timestamp(0) NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP(0),
  `outtime` timestamp(0) NULL DEFAULT NULL,
  `grade` varchar(45) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `selller` varchar(45) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `bstorage` varchar(45) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `tocompany` varchar(45) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `tracknumber` varchar(45) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `salenumber` varchar(45) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `remarks` varchar(45) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `productlines` varchar(45) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `forinventory` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE INDEX `id_UNIQUE`(`id`) USING BTREE,
  UNIQUE INDEX `IEMI_UNIQUE`(`IEMI`) USING BTREE,
  INDEX `iphonestorage`(`istorage`) USING BTREE,
  INDEX `iphonecolor`(`color`) USING BTREE,
  INDEX `incompany`(`company`) USING BTREE,
  INDEX `outcompany`(`tocompany`) USING BTREE,
  INDEX `productlines`(`productlines`) USING BTREE,
  CONSTRAINT `iphone11_ibfk_1` FOREIGN KEY (`company`) REFERENCES `incompany` (`incompany`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  CONSTRAINT `iphone11_ibfk_2` FOREIGN KEY (`color`) REFERENCES `iphonecolor` (`iphonecolor`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  CONSTRAINT `iphone11_ibfk_3` FOREIGN KEY (`istorage`) REFERENCES `iphonestorage` (`iphonestorage`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  CONSTRAINT `iphone11_ibfk_5` FOREIGN KEY (`productlines`) REFERENCES `productlines` (`productlines`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE = InnoDB AUTO_INCREMENT = 923 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Table structure for iphone11pro
-- ----------------------------
DROP TABLE IF EXISTS `iphone11pro`;
CREATE TABLE `iphone11pro`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `IEMI` varchar(45) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `istorage` varchar(45) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `color` varchar(45) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `company` varchar(45) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `intime` timestamp(0) NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP(0),
  `outtime` timestamp(0) NULL DEFAULT NULL,
  `grade` varchar(45) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `selller` varchar(45) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `bstorage` varchar(45) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `tocompany` varchar(45) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `tracknumber` varchar(45) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `salenumber` varchar(45) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `remarks` varchar(45) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `productlines` varchar(45) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `forinventory` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE INDEX `id_UNIQUE`(`id`) USING BTREE,
  UNIQUE INDEX `IEMI_UNIQUE`(`IEMI`) USING BTREE,
  INDEX `iphonestorage`(`istorage`) USING BTREE,
  INDEX `iphonecolor`(`color`) USING BTREE,
  INDEX `incompany`(`company`) USING BTREE,
  INDEX `outcompany`(`tocompany`) USING BTREE,
  INDEX `productlines`(`productlines`) USING BTREE,
  CONSTRAINT `iphone11pro_ibfk_1` FOREIGN KEY (`company`) REFERENCES `incompany` (`incompany`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  CONSTRAINT `iphone11pro_ibfk_2` FOREIGN KEY (`color`) REFERENCES `iphonecolor` (`iphonecolor`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  CONSTRAINT `iphone11pro_ibfk_3` FOREIGN KEY (`istorage`) REFERENCES `iphonestorage` (`iphonestorage`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  CONSTRAINT `iphone11pro_ibfk_5` FOREIGN KEY (`productlines`) REFERENCES `productlines` (`productlines`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE = InnoDB AUTO_INCREMENT = 61 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Table structure for iphone11promax
-- ----------------------------
DROP TABLE IF EXISTS `iphone11promax`;
CREATE TABLE `iphone11promax`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `IEMI` varchar(45) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `istorage` varchar(45) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `color` varchar(45) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `company` varchar(45) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `intime` timestamp(0) NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP(0),
  `outtime` timestamp(0) NULL DEFAULT NULL,
  `grade` varchar(45) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `selller` varchar(45) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `bstorage` varchar(45) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `tocompany` varchar(45) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `tracknumber` varchar(45) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `salenumber` varchar(45) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `remarks` varchar(45) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `productlines` varchar(45) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `forinventory` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE INDEX `id_UNIQUE`(`id`) USING BTREE,
  UNIQUE INDEX `IEMI_UNIQUE`(`IEMI`) USING BTREE,
  INDEX `iphonestorage`(`istorage`) USING BTREE,
  INDEX `iphonecolor`(`color`) USING BTREE,
  INDEX `incompany`(`company`) USING BTREE,
  INDEX `outcompany`(`tocompany`) USING BTREE,
  INDEX `productlines`(`productlines`) USING BTREE,
  CONSTRAINT `iphone11promax_ibfk_1` FOREIGN KEY (`company`) REFERENCES `incompany` (`incompany`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  CONSTRAINT `iphone11promax_ibfk_2` FOREIGN KEY (`color`) REFERENCES `iphonecolor` (`iphonecolor`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  CONSTRAINT `iphone11promax_ibfk_3` FOREIGN KEY (`istorage`) REFERENCES `iphonestorage` (`iphonestorage`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  CONSTRAINT `iphone11promax_ibfk_5` FOREIGN KEY (`productlines`) REFERENCES `productlines` (`productlines`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE = InnoDB AUTO_INCREMENT = 1 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Table structure for iphone12
-- ----------------------------
DROP TABLE IF EXISTS `iphone12`;
CREATE TABLE `iphone12`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `IEMI` varchar(45) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `istorage` varchar(45) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `color` varchar(45) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `company` varchar(45) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `intime` timestamp(0) NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP(0),
  `outtime` timestamp(0) NULL DEFAULT NULL,
  `grade` varchar(45) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `selller` varchar(45) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `bstorage` varchar(45) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `tocompany` varchar(45) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `tracknumber` varchar(45) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `salenumber` varchar(45) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `remarks` varchar(45) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `productlines` varchar(45) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `forinventory` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE INDEX `id_UNIQUE`(`id`) USING BTREE,
  UNIQUE INDEX `IEMI_UNIQUE`(`IEMI`) USING BTREE,
  INDEX `iphonestorage`(`istorage`) USING BTREE,
  INDEX `iphonecolor`(`color`) USING BTREE,
  INDEX `incompany`(`company`) USING BTREE,
  INDEX `outcompany`(`tocompany`) USING BTREE,
  INDEX `productlines`(`productlines`) USING BTREE,
  CONSTRAINT `iphone12_ibfk_1` FOREIGN KEY (`company`) REFERENCES `incompany` (`incompany`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  CONSTRAINT `iphone12_ibfk_2` FOREIGN KEY (`color`) REFERENCES `iphonecolor` (`iphonecolor`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  CONSTRAINT `iphone12_ibfk_3` FOREIGN KEY (`istorage`) REFERENCES `iphonestorage` (`iphonestorage`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  CONSTRAINT `iphone12_ibfk_5` FOREIGN KEY (`productlines`) REFERENCES `productlines` (`productlines`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE = InnoDB AUTO_INCREMENT = 8 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Table structure for iphone12mini
-- ----------------------------
DROP TABLE IF EXISTS `iphone12mini`;
CREATE TABLE `iphone12mini`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `IEMI` varchar(45) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `istorage` varchar(45) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `color` varchar(45) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `company` varchar(45) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `intime` timestamp(0) NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP(0),
  `outtime` timestamp(0) NULL DEFAULT NULL,
  `grade` varchar(45) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `selller` varchar(45) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `bstorage` varchar(45) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `tocompany` varchar(45) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `tracknumber` varchar(45) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `salenumber` varchar(45) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `remarks` varchar(45) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `productlines` varchar(45) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `forinventory` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE INDEX `id_UNIQUE`(`id`) USING BTREE,
  UNIQUE INDEX `IEMI_UNIQUE`(`IEMI`) USING BTREE,
  INDEX `iphonestorage`(`istorage`) USING BTREE,
  INDEX `iphonecolor`(`color`) USING BTREE,
  INDEX `incompany`(`company`) USING BTREE,
  INDEX `outcompany`(`tocompany`) USING BTREE,
  INDEX `productlines`(`productlines`) USING BTREE,
  CONSTRAINT `iphone12mini_ibfk_1` FOREIGN KEY (`company`) REFERENCES `incompany` (`incompany`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  CONSTRAINT `iphone12mini_ibfk_2` FOREIGN KEY (`color`) REFERENCES `iphonecolor` (`iphonecolor`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  CONSTRAINT `iphone12mini_ibfk_3` FOREIGN KEY (`istorage`) REFERENCES `iphonestorage` (`iphonestorage`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  CONSTRAINT `iphone12mini_ibfk_5` FOREIGN KEY (`productlines`) REFERENCES `productlines` (`productlines`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE = InnoDB AUTO_INCREMENT = 21 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Table structure for iphone12pro
-- ----------------------------
DROP TABLE IF EXISTS `iphone12pro`;
CREATE TABLE `iphone12pro`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `IEMI` varchar(45) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `istorage` varchar(45) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `color` varchar(45) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `company` varchar(45) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `intime` timestamp(0) NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP(0),
  `outtime` timestamp(0) NULL DEFAULT NULL,
  `grade` varchar(45) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `selller` varchar(45) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `bstorage` varchar(45) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `tocompany` varchar(45) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `tracknumber` varchar(45) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `salenumber` varchar(45) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `remarks` varchar(45) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `productlines` varchar(45) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `forinventory` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE INDEX `id_UNIQUE`(`id`) USING BTREE,
  UNIQUE INDEX `IEMI_UNIQUE`(`IEMI`) USING BTREE,
  INDEX `iphonestorage`(`istorage`) USING BTREE,
  INDEX `iphonecolor`(`color`) USING BTREE,
  INDEX `incompany`(`company`) USING BTREE,
  INDEX `outcompany`(`tocompany`) USING BTREE,
  INDEX `productlines`(`productlines`) USING BTREE,
  CONSTRAINT `iphone12pro_ibfk_1` FOREIGN KEY (`company`) REFERENCES `incompany` (`incompany`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  CONSTRAINT `iphone12pro_ibfk_2` FOREIGN KEY (`color`) REFERENCES `iphonecolor` (`iphonecolor`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  CONSTRAINT `iphone12pro_ibfk_3` FOREIGN KEY (`istorage`) REFERENCES `iphonestorage` (`iphonestorage`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  CONSTRAINT `iphone12pro_ibfk_5` FOREIGN KEY (`productlines`) REFERENCES `productlines` (`productlines`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE = InnoDB AUTO_INCREMENT = 2 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Table structure for iphone12promax
-- ----------------------------
DROP TABLE IF EXISTS `iphone12promax`;
CREATE TABLE `iphone12promax`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `IEMI` varchar(45) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `istorage` varchar(45) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `color` varchar(45) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `company` varchar(45) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `intime` timestamp(0) NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP(0),
  `outtime` timestamp(0) NULL DEFAULT NULL,
  `grade` varchar(45) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `selller` varchar(45) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `bstorage` varchar(45) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `tocompany` varchar(45) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `tracknumber` varchar(45) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `salenumber` varchar(45) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `remarks` varchar(45) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `productlines` varchar(45) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `forinventory` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE INDEX `id_UNIQUE`(`id`) USING BTREE,
  UNIQUE INDEX `IEMI_UNIQUE`(`IEMI`) USING BTREE,
  INDEX `iphonestorage`(`istorage`) USING BTREE,
  INDEX `iphonecolor`(`color`) USING BTREE,
  INDEX `incompany`(`company`) USING BTREE,
  INDEX `outcompany`(`tocompany`) USING BTREE,
  INDEX `productlines`(`productlines`) USING BTREE,
  CONSTRAINT `iphone12promax_ibfk_1` FOREIGN KEY (`company`) REFERENCES `incompany` (`incompany`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  CONSTRAINT `iphone12promax_ibfk_2` FOREIGN KEY (`color`) REFERENCES `iphonecolor` (`iphonecolor`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  CONSTRAINT `iphone12promax_ibfk_3` FOREIGN KEY (`istorage`) REFERENCES `iphonestorage` (`iphonestorage`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  CONSTRAINT `iphone12promax_ibfk_5` FOREIGN KEY (`productlines`) REFERENCES `productlines` (`productlines`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE = InnoDB AUTO_INCREMENT = 15 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Table structure for iphone7
-- ----------------------------
DROP TABLE IF EXISTS `iphone7`;
CREATE TABLE `iphone7`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `IEMI` varchar(45) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `istorage` varchar(45) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `color` varchar(45) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `company` varchar(45) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `intime` timestamp(0) NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP(0),
  `outtime` timestamp(0) NULL DEFAULT NULL,
  `grade` varchar(45) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `selller` varchar(45) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `bstorage` varchar(45) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `tocompany` varchar(45) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `tracknumber` varchar(45) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `salenumber` varchar(45) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `remarks` varchar(45) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `productlines` varchar(45) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `forinventory` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE INDEX `id_UNIQUE`(`id`) USING BTREE,
  UNIQUE INDEX `IEMI_UNIQUE`(`IEMI`) USING BTREE,
  INDEX `iphonestorage`(`istorage`) USING BTREE,
  INDEX `iphonecolor`(`color`) USING BTREE,
  INDEX `incompany`(`company`) USING BTREE,
  INDEX `outcompany`(`tocompany`) USING BTREE,
  INDEX `productlines`(`productlines`) USING BTREE,
  CONSTRAINT `iphone7_ibfk_1` FOREIGN KEY (`company`) REFERENCES `incompany` (`incompany`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  CONSTRAINT `iphone7_ibfk_2` FOREIGN KEY (`color`) REFERENCES `iphonecolor` (`iphonecolor`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  CONSTRAINT `iphone7_ibfk_3` FOREIGN KEY (`istorage`) REFERENCES `iphonestorage` (`iphonestorage`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  CONSTRAINT `iphone7_ibfk_5` FOREIGN KEY (`productlines`) REFERENCES `productlines` (`productlines`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE = InnoDB AUTO_INCREMENT = 1 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Table structure for iphone7plus
-- ----------------------------
DROP TABLE IF EXISTS `iphone7plus`;
CREATE TABLE `iphone7plus`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `IEMI` varchar(45) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `istorage` varchar(45) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `color` varchar(45) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `company` varchar(45) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `intime` timestamp(0) NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP(0),
  `outtime` timestamp(0) NULL DEFAULT NULL,
  `grade` varchar(45) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `selller` varchar(45) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `bstorage` varchar(45) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `tocompany` varchar(45) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `tracknumber` varchar(45) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `salenumber` varchar(45) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `remarks` varchar(45) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `productlines` varchar(45) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `forinventory` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE INDEX `id_UNIQUE`(`id`) USING BTREE,
  UNIQUE INDEX `IEMI_UNIQUE`(`IEMI`) USING BTREE,
  INDEX `iphonestorage`(`istorage`) USING BTREE,
  INDEX `iphonecolor`(`color`) USING BTREE,
  INDEX `incompany`(`company`) USING BTREE,
  INDEX `outcompany`(`tocompany`) USING BTREE,
  INDEX `productlines`(`productlines`) USING BTREE,
  CONSTRAINT `iphone7plus_ibfk_1` FOREIGN KEY (`company`) REFERENCES `incompany` (`incompany`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  CONSTRAINT `iphone7plus_ibfk_2` FOREIGN KEY (`color`) REFERENCES `iphonecolor` (`iphonecolor`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  CONSTRAINT `iphone7plus_ibfk_3` FOREIGN KEY (`istorage`) REFERENCES `iphonestorage` (`iphonestorage`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  CONSTRAINT `iphone7plus_ibfk_5` FOREIGN KEY (`productlines`) REFERENCES `productlines` (`productlines`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE = InnoDB AUTO_INCREMENT = 22 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Table structure for iphone8
-- ----------------------------
DROP TABLE IF EXISTS `iphone8`;
CREATE TABLE `iphone8`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `IEMI` varchar(45) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `istorage` varchar(45) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `color` varchar(45) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `company` varchar(45) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `intime` timestamp(0) NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP(0),
  `outtime` timestamp(0) NULL DEFAULT NULL,
  `grade` varchar(45) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `selller` varchar(45) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `bstorage` varchar(45) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `tocompany` varchar(45) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `tracknumber` varchar(45) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `salenumber` varchar(45) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `remarks` varchar(45) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `productlines` varchar(45) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `forinventory` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE INDEX `id_UNIQUE`(`id`) USING BTREE,
  UNIQUE INDEX `IEMI_UNIQUE`(`IEMI`) USING BTREE,
  INDEX `iphonestorage`(`istorage`) USING BTREE,
  INDEX `iphonecolor`(`color`) USING BTREE,
  INDEX `incompany`(`company`) USING BTREE,
  INDEX `outcompany`(`tocompany`) USING BTREE,
  INDEX `productlines`(`productlines`) USING BTREE,
  CONSTRAINT `iphone8_ibfk_1` FOREIGN KEY (`company`) REFERENCES `incompany` (`incompany`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  CONSTRAINT `iphone8_ibfk_2` FOREIGN KEY (`color`) REFERENCES `iphonecolor` (`iphonecolor`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  CONSTRAINT `iphone8_ibfk_3` FOREIGN KEY (`istorage`) REFERENCES `iphonestorage` (`iphonestorage`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  CONSTRAINT `iphone8_ibfk_5` FOREIGN KEY (`productlines`) REFERENCES `productlines` (`productlines`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE = InnoDB AUTO_INCREMENT = 1 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Table structure for iphone8plus
-- ----------------------------
DROP TABLE IF EXISTS `iphone8plus`;
CREATE TABLE `iphone8plus`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `IEMI` varchar(45) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `istorage` varchar(45) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `color` varchar(45) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `company` varchar(45) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `intime` timestamp(0) NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP(0),
  `outtime` timestamp(0) NULL DEFAULT NULL,
  `grade` varchar(45) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `selller` varchar(45) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `bstorage` varchar(45) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `tocompany` varchar(45) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `tracknumber` varchar(45) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `salenumber` varchar(45) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `remarks` varchar(45) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `productlines` varchar(45) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `forinventory` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE INDEX `id_UNIQUE`(`id`) USING BTREE,
  UNIQUE INDEX `IEMI_UNIQUE`(`IEMI`) USING BTREE,
  INDEX `iphonestorage`(`istorage`) USING BTREE,
  INDEX `iphonecolor`(`color`) USING BTREE,
  INDEX `incompany`(`company`) USING BTREE,
  INDEX `outcompany`(`tocompany`) USING BTREE,
  INDEX `productlines`(`productlines`) USING BTREE,
  CONSTRAINT `iphone8plus_ibfk_1` FOREIGN KEY (`company`) REFERENCES `incompany` (`incompany`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  CONSTRAINT `iphone8plus_ibfk_2` FOREIGN KEY (`color`) REFERENCES `iphonecolor` (`iphonecolor`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  CONSTRAINT `iphone8plus_ibfk_3` FOREIGN KEY (`istorage`) REFERENCES `iphonestorage` (`iphonestorage`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  CONSTRAINT `iphone8plus_ibfk_5` FOREIGN KEY (`productlines`) REFERENCES `productlines` (`productlines`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE = InnoDB AUTO_INCREMENT = 2 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Table structure for iphonecolor
-- ----------------------------
DROP TABLE IF EXISTS `iphonecolor`;
CREATE TABLE `iphonecolor`  (
  `idiphonecolor` int(11) NOT NULL,
  `iphonecolor` varchar(45) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  PRIMARY KEY (`idiphonecolor`) USING BTREE,
  UNIQUE INDEX `idiphonecolor_UNIQUE`(`idiphonecolor`) USING BTREE,
  UNIQUE INDEX `iphonecolor_UNIQUE`(`iphonecolor`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of iphonecolor
-- ----------------------------
INSERT INTO `iphonecolor` VALUES (10, '亮黑色');
INSERT INTO `iphonecolor` VALUES (14, '暗夜绿色');
INSERT INTO `iphonecolor` VALUES (12, '深空灰色');
INSERT INTO `iphonecolor` VALUES (13, '玫瑰金色');
INSERT INTO `iphonecolor` VALUES (11, '珊瑚色');
INSERT INTO `iphonecolor` VALUES (5, '白色');
INSERT INTO `iphonecolor` VALUES (8, '紫色');
INSERT INTO `iphonecolor` VALUES (4, '红色');
INSERT INTO `iphonecolor` VALUES (9, '绿色');
INSERT INTO `iphonecolor` VALUES (6, '蓝色');
INSERT INTO `iphonecolor` VALUES (3, '金色');
INSERT INTO `iphonecolor` VALUES (1, '银色');
INSERT INTO `iphonecolor` VALUES (7, '黄色');
INSERT INTO `iphonecolor` VALUES (2, '黑色');

-- ----------------------------
-- Table structure for iphoneinfo
-- ----------------------------
DROP TABLE IF EXISTS `iphoneinfo`;
CREATE TABLE `iphoneinfo`  (
  `type` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `istorage` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `color` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL
) ENGINE = InnoDB CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Table structure for iphonese
-- ----------------------------
DROP TABLE IF EXISTS `iphonese`;
CREATE TABLE `iphonese`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `IEMI` varchar(45) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `istorage` varchar(45) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `color` varchar(45) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `company` varchar(45) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `intime` timestamp(0) NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP(0),
  `outtime` timestamp(0) NULL DEFAULT NULL,
  `grade` varchar(45) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `selller` varchar(45) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `bstorage` varchar(45) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `tocompany` varchar(45) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `tracknumber` varchar(45) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `salenumber` varchar(45) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `remarks` varchar(45) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `productlines` varchar(45) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `forinventory` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE INDEX `id_UNIQUE`(`id`) USING BTREE,
  UNIQUE INDEX `IEMI_UNIQUE`(`IEMI`) USING BTREE,
  INDEX `iphonestorage`(`istorage`) USING BTREE,
  INDEX `iphonecolor`(`color`) USING BTREE,
  INDEX `incompany`(`company`) USING BTREE,
  INDEX `outcompany`(`tocompany`) USING BTREE,
  INDEX `productlines`(`productlines`) USING BTREE,
  CONSTRAINT `iphonese_ibfk_1` FOREIGN KEY (`company`) REFERENCES `incompany` (`incompany`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  CONSTRAINT `iphonese_ibfk_2` FOREIGN KEY (`color`) REFERENCES `iphonecolor` (`iphonecolor`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  CONSTRAINT `iphonese_ibfk_3` FOREIGN KEY (`istorage`) REFERENCES `iphonestorage` (`iphonestorage`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  CONSTRAINT `iphonese_ibfk_4` FOREIGN KEY (`tocompany`) REFERENCES `outcompany` (`outcompany`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  CONSTRAINT `iphonese_ibfk_5` FOREIGN KEY (`productlines`) REFERENCES `productlines` (`productlines`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE = InnoDB AUTO_INCREMENT = 1 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Table structure for iphonestorage
-- ----------------------------
DROP TABLE IF EXISTS `iphonestorage`;
CREATE TABLE `iphonestorage`  (
  `idiphonestorage` int(11) NOT NULL,
  `iphonestorage` varchar(45) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  PRIMARY KEY (`idiphonestorage`) USING BTREE,
  UNIQUE INDEX `iphonestorage_UNIQUE`(`iphonestorage`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of iphonestorage
-- ----------------------------
INSERT INTO `iphonestorage` VALUES (4, '128G');
INSERT INTO `iphonestorage` VALUES (1, '16G');
INSERT INTO `iphonestorage` VALUES (5, '256G');
INSERT INTO `iphonestorage` VALUES (2, '32G');
INSERT INTO `iphonestorage` VALUES (6, '512G');
INSERT INTO `iphonestorage` VALUES (3, '64G');

-- ----------------------------
-- Table structure for iphonetype
-- ----------------------------
DROP TABLE IF EXISTS `iphonetype`;
CREATE TABLE `iphonetype`  (
  `idiphonetype` int(10) UNSIGNED NOT NULL,
  `iphonetype` varchar(45) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  PRIMARY KEY (`idiphonetype`) USING BTREE,
  UNIQUE INDEX `iphonetype_UNIQUE`(`iphonetype`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of iphonetype
-- ----------------------------
INSERT INTO `iphonetype` VALUES (9, 'iphone 11');
INSERT INTO `iphonetype` VALUES (10, 'iphone 11 Pro');
INSERT INTO `iphonetype` VALUES (12, 'iphone 11 Pro Max');
INSERT INTO `iphonetype` VALUES (13, 'iphone 12');
INSERT INTO `iphonetype` VALUES (16, 'iphone 12 mini');
INSERT INTO `iphonetype` VALUES (14, 'iphone 12 Pro');
INSERT INTO `iphonetype` VALUES (15, 'iphone 12 Pro Max');
INSERT INTO `iphonetype` VALUES (1, 'iphone 7');
INSERT INTO `iphonetype` VALUES (2, 'iphone 7 Plus');
INSERT INTO `iphonetype` VALUES (3, 'iphone 8');
INSERT INTO `iphonetype` VALUES (4, 'iphone 8 Plus');
INSERT INTO `iphonetype` VALUES (11, 'iphone SE');
INSERT INTO `iphonetype` VALUES (5, 'iphone X');
INSERT INTO `iphonetype` VALUES (8, 'iphone XR');
INSERT INTO `iphonetype` VALUES (6, 'iphone XS');
INSERT INTO `iphonetype` VALUES (7, 'iphone XS Max');

-- ----------------------------
-- Table structure for iphonex
-- ----------------------------
DROP TABLE IF EXISTS `iphonex`;
CREATE TABLE `iphonex`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `IEMI` varchar(45) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `istorage` varchar(45) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `color` varchar(45) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `company` varchar(45) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `intime` timestamp(0) NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP(0),
  `outtime` timestamp(0) NULL DEFAULT NULL,
  `grade` varchar(45) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `selller` varchar(45) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `bstorage` varchar(45) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `tocompany` varchar(45) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `tracknumber` varchar(45) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `salenumber` varchar(45) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `remarks` varchar(45) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `productlines` varchar(45) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `forinventory` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE INDEX `id_UNIQUE`(`id`) USING BTREE,
  UNIQUE INDEX `IEMI_UNIQUE`(`IEMI`) USING BTREE,
  INDEX `iphonestorage`(`istorage`) USING BTREE,
  INDEX `iphonecolor`(`color`) USING BTREE,
  INDEX `incompany`(`company`) USING BTREE,
  INDEX `outcompany`(`tocompany`) USING BTREE,
  INDEX `productlines`(`productlines`) USING BTREE,
  CONSTRAINT `iphonex_ibfk_1` FOREIGN KEY (`company`) REFERENCES `incompany` (`incompany`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  CONSTRAINT `iphonex_ibfk_2` FOREIGN KEY (`color`) REFERENCES `iphonecolor` (`iphonecolor`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  CONSTRAINT `iphonex_ibfk_3` FOREIGN KEY (`istorage`) REFERENCES `iphonestorage` (`iphonestorage`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  CONSTRAINT `iphonex_ibfk_4` FOREIGN KEY (`tocompany`) REFERENCES `outcompany` (`outcompany`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  CONSTRAINT `iphonex_ibfk_5` FOREIGN KEY (`productlines`) REFERENCES `productlines` (`productlines`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE = InnoDB AUTO_INCREMENT = 1 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Table structure for iphonexr
-- ----------------------------
DROP TABLE IF EXISTS `iphonexr`;
CREATE TABLE `iphonexr`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `IEMI` varchar(45) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `istorage` varchar(45) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `color` varchar(45) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `company` varchar(45) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `intime` timestamp(0) NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP(0),
  `outtime` timestamp(0) NULL DEFAULT NULL,
  `grade` varchar(45) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `selller` varchar(45) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `bstorage` varchar(45) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `tocompany` varchar(45) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `tracknumber` varchar(45) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `salenumber` varchar(45) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `remarks` varchar(45) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `productlines` varchar(45) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `forinventory` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE INDEX `id_UNIQUE`(`id`) USING BTREE,
  UNIQUE INDEX `IEMI_UNIQUE`(`IEMI`) USING BTREE,
  INDEX `iphonestorage`(`istorage`) USING BTREE,
  INDEX `iphonecolor`(`color`) USING BTREE,
  INDEX `incompany`(`company`) USING BTREE,
  INDEX `outcompany`(`tocompany`) USING BTREE,
  INDEX `productlines`(`productlines`) USING BTREE,
  CONSTRAINT `iphonexr_ibfk_1` FOREIGN KEY (`company`) REFERENCES `incompany` (`incompany`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  CONSTRAINT `iphonexr_ibfk_2` FOREIGN KEY (`color`) REFERENCES `iphonecolor` (`iphonecolor`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  CONSTRAINT `iphonexr_ibfk_3` FOREIGN KEY (`istorage`) REFERENCES `iphonestorage` (`iphonestorage`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  CONSTRAINT `iphonexr_ibfk_4` FOREIGN KEY (`tocompany`) REFERENCES `outcompany` (`outcompany`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  CONSTRAINT `iphonexr_ibfk_5` FOREIGN KEY (`productlines`) REFERENCES `productlines` (`productlines`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE = InnoDB AUTO_INCREMENT = 1 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Table structure for iphonexs
-- ----------------------------
DROP TABLE IF EXISTS `iphonexs`;
CREATE TABLE `iphonexs`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `IEMI` varchar(45) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `istorage` varchar(45) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `color` varchar(45) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `company` varchar(45) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `intime` timestamp(0) NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP(0),
  `outtime` timestamp(0) NULL DEFAULT NULL,
  `grade` varchar(45) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `selller` varchar(45) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `bstorage` varchar(45) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `tocompany` varchar(45) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `tracknumber` varchar(45) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `salenumber` varchar(45) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `remarks` varchar(45) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `productlines` varchar(45) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `forinventory` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE INDEX `id_UNIQUE`(`id`) USING BTREE,
  UNIQUE INDEX `IEMI_UNIQUE`(`IEMI`) USING BTREE,
  INDEX `iphonestorage`(`istorage`) USING BTREE,
  INDEX `iphonecolor`(`color`) USING BTREE,
  INDEX `incompany`(`company`) USING BTREE,
  INDEX `outcompany`(`tocompany`) USING BTREE,
  INDEX `productlines`(`productlines`) USING BTREE,
  CONSTRAINT `iphonexs_ibfk_1` FOREIGN KEY (`company`) REFERENCES `incompany` (`incompany`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  CONSTRAINT `iphonexs_ibfk_2` FOREIGN KEY (`color`) REFERENCES `iphonecolor` (`iphonecolor`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  CONSTRAINT `iphonexs_ibfk_3` FOREIGN KEY (`istorage`) REFERENCES `iphonestorage` (`iphonestorage`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  CONSTRAINT `iphonexs_ibfk_4` FOREIGN KEY (`tocompany`) REFERENCES `outcompany` (`outcompany`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  CONSTRAINT `iphonexs_ibfk_5` FOREIGN KEY (`productlines`) REFERENCES `productlines` (`productlines`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE = InnoDB AUTO_INCREMENT = 1 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Table structure for iphonexsmax
-- ----------------------------
DROP TABLE IF EXISTS `iphonexsmax`;
CREATE TABLE `iphonexsmax`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `IEMI` varchar(45) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `istorage` varchar(45) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `color` varchar(45) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `company` varchar(45) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `intime` timestamp(0) NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP(0),
  `outtime` timestamp(0) NULL DEFAULT NULL,
  `grade` varchar(45) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `selller` varchar(45) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `bstorage` varchar(45) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `tocompany` varchar(45) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `tracknumber` varchar(45) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `salenumber` varchar(45) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `remarks` varchar(45) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `productlines` varchar(45) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `forinventory` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE INDEX `id_UNIQUE`(`id`) USING BTREE,
  UNIQUE INDEX `IEMI_UNIQUE`(`IEMI`) USING BTREE,
  INDEX `iphonestorage`(`istorage`) USING BTREE,
  INDEX `iphonecolor`(`color`) USING BTREE,
  INDEX `incompany`(`company`) USING BTREE,
  INDEX `outcompany`(`tocompany`) USING BTREE,
  INDEX `productlines`(`productlines`) USING BTREE,
  CONSTRAINT `iphonexsmax_ibfk_1` FOREIGN KEY (`company`) REFERENCES `incompany` (`incompany`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  CONSTRAINT `iphonexsmax_ibfk_2` FOREIGN KEY (`color`) REFERENCES `iphonecolor` (`iphonecolor`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  CONSTRAINT `iphonexsmax_ibfk_3` FOREIGN KEY (`istorage`) REFERENCES `iphonestorage` (`iphonestorage`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  CONSTRAINT `iphonexsmax_ibfk_4` FOREIGN KEY (`tocompany`) REFERENCES `outcompany` (`outcompany`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  CONSTRAINT `iphonexsmax_ibfk_5` FOREIGN KEY (`productlines`) REFERENCES `productlines` (`productlines`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE = InnoDB AUTO_INCREMENT = 19 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Table structure for outcompany
-- ----------------------------
DROP TABLE IF EXISTS `outcompany`;
CREATE TABLE `outcompany`  (
  `idcompany` int(10) UNSIGNED NOT NULL,
  `outcompany` varchar(45) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  PRIMARY KEY (`idcompany`) USING BTREE,
  INDEX `incompany`(`outcompany`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Table structure for polishedline
-- ----------------------------
DROP TABLE IF EXISTS `polishedline`;
CREATE TABLE `polishedline`  (
  `IEMI` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `changetime` timestamp(0) NULL DEFAULT NULL ON UPDATE CURRENT_TIMESTAMP(0),
  `bool` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `id` int(11) NOT NULL AUTO_INCREMENT,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 11 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Table structure for productlines
-- ----------------------------
DROP TABLE IF EXISTS `productlines`;
CREATE TABLE `productlines`  (
  `idproductlines` int(11) NOT NULL,
  `productlines` varchar(45) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  PRIMARY KEY (`idproductlines`) USING BTREE,
  UNIQUE INDEX `productlines_UNIQUE`(`productlines`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of productlines
-- ----------------------------
INSERT INTO `productlines` VALUES (1, '仓库');
INSERT INTO `productlines` VALUES (5, '打磨');
INSERT INTO `productlines` VALUES (4, '换屏');
INSERT INTO `productlines` VALUES (2, '测试');
INSERT INTO `productlines` VALUES (3, '维修');
INSERT INTO `productlines` VALUES (6, '返修');

-- ----------------------------
-- Table structure for repaireline
-- ----------------------------
DROP TABLE IF EXISTS `repaireline`;
CREATE TABLE `repaireline`  (
  `IEMI` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `changetime` timestamp(0) NULL DEFAULT NULL ON UPDATE CURRENT_TIMESTAMP(0),
  `bool` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `id` int(11) NOT NULL AUTO_INCREMENT,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 45 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Table structure for returnline
-- ----------------------------
DROP TABLE IF EXISTS `returnline`;
CREATE TABLE `returnline`  (
  `IEMI` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `changetime` timestamp(0) NULL DEFAULT NULL ON UPDATE CURRENT_TIMESTAMP(0),
  `bool` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `id` int(11) NOT NULL AUTO_INCREMENT,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 13 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Table structure for testline
-- ----------------------------
DROP TABLE IF EXISTS `testline`;
CREATE TABLE `testline`  (
  `IEMI` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `changetime` timestamp(0) NULL DEFAULT NULL ON UPDATE CURRENT_TIMESTAMP(0),
  `bool` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `id` int(11) NOT NULL AUTO_INCREMENT,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 83 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Table structure for warehouseline
-- ----------------------------
DROP TABLE IF EXISTS `warehouseline`;
CREATE TABLE `warehouseline`  (
  `IEMI` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `changetime` timestamp(0) NULL DEFAULT NULL ON UPDATE CURRENT_TIMESTAMP(0),
  `bool` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `id` int(11) NOT NULL AUTO_INCREMENT,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 41 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

SET FOREIGN_KEY_CHECKS = 1;
