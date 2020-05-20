/*
 Navicat Premium Data Transfer

 Source Server         : root
 Source Server Type    : MySQL
 Source Server Version : 80019
 Source Host           : localhost:3306
 Source Schema         : up

 Target Server Type    : MySQL
 Target Server Version : 80019
 File Encoding         : 65001

 Date: 15/05/2020 23:02:45
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for asset
-- ----------------------------
DROP TABLE IF EXISTS `asset`;
CREATE TABLE `asset`  (
  `id` int(0) NOT NULL,
  `name` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `type` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `project` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `createtime` datetime(0) NULL DEFAULT NULL,
  `auther` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `other` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of asset
-- ----------------------------
INSERT INTO `asset` VALUES (1, 'car', 'prop', 'up', '2020-04-13 10:36:46', 'zhansan', '[]');
INSERT INTO `asset` VALUES (2, 'tree', 'scenes', 'up', '2020-04-13 10:36:46', 'zhansan', '[]');
INSERT INTO `asset` VALUES (3, 'cat', 'character', 'up', '2020-04-13 10:36:46', 'zhansan', '[]');

-- ----------------------------
-- Table structure for assettask
-- ----------------------------
DROP TABLE IF EXISTS `assettask`;
CREATE TABLE `assettask`  (
  `id` int(0) NOT NULL,
  `chinesename` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `type` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `pipeline` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `producer` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `status` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of assettask
-- ----------------------------
INSERT INTO `assettask` VALUES (1, '汽车', 'prop', 'mod', 'zhansan', 'work');
INSERT INTO `assettask` VALUES (2, '汽车', 'prop', 'rig', 'lisai', 'work');
INSERT INTO `assettask` VALUES (3, '树', 'scense', 'mod', 'lsi', 'work');
INSERT INTO `assettask` VALUES (4, '树', 'scense', 'shd', 'sdf', 'work');

-- ----------------------------
-- Table structure for eps
-- ----------------------------
DROP TABLE IF EXISTS `eps`;
CREATE TABLE `eps`  (
  `id` int(0) NOT NULL AUTO_INCREMENT,
  `number` varchar(12) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `createtime` datetime(6) NULL DEFAULT NULL ON UPDATE CURRENT_TIMESTAMP(6),
  `creator` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `project` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 7 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of eps
-- ----------------------------
INSERT INTO `eps` VALUES (1, 'EP001', '2020-04-10 18:17:49.270803', 'zahnsan', 'big');
INSERT INTO `eps` VALUES (2, 'EP002', '2020-04-10 18:17:55.080514', 'zahnsan', 'big');
INSERT INTO `eps` VALUES (3, 'EP003', '2020-04-10 18:17:55.912290', 'zahnsan', 'big');
INSERT INTO `eps` VALUES (4, 'EP004', '2020-04-10 18:17:56.562392', 'zahnsan', 'big');
INSERT INTO `eps` VALUES (5, 'EP005', '2020-04-10 18:17:57.375985', 'zahnsan', 'big');
INSERT INTO `eps` VALUES (6, 'EP006', '2020-04-10 18:17:58.894896', 'zahnsan', 'big');

-- ----------------------------
-- Table structure for project
-- ----------------------------
DROP TABLE IF EXISTS `project`;
CREATE TABLE `project`  (
  `id` int(0) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `infor` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `projectpath` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `assetpipeline` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `shotpipeline` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 2 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = DYNAMIC;

-- ----------------------------
-- Records of project
-- ----------------------------
INSERT INTO `project` VALUES (1, 'up', '{\"databasecode\":\"up\",\"chinesename\":\"飞屋环游记\",\"date\":\"2020.3.23\",\"auther\":\"张三\"}', '[\'Big/asset/work\', \'Big/asset/publish\', \'Big/shot/work\', \'Big/shot/publish\']', '{\'asset\': {\'mod\': \'模型\', \'shd\': \'材质\', \'rig\': \'绑定\', \'cloth\': \'布料\', \'up\': \'飞屋环游记\'}}', NULL);

-- ----------------------------
-- Table structure for shot
-- ----------------------------
DROP TABLE IF EXISTS `shot`;
CREATE TABLE `shot`  (
  `id` int(0) NOT NULL,
  `shot_name` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `shot_pipeline` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `shot_startframe` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `shot_endframe` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `shot_totalframe` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `shot_descrip` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of shot
-- ----------------------------
INSERT INTO `shot` VALUES (1, 'SC001', 'ani', '1', '100', '99', '动画镜头');
INSERT INTO `shot` VALUES (2, 'SC002', 'ani', '1', '90', '89', '动画镜头');
INSERT INTO `shot` VALUES (3, 'SC003', 'vfx', '100', '200', '99', '特效镜头');

-- ----------------------------
-- Table structure for shottask
-- ----------------------------
DROP TABLE IF EXISTS `shottask`;
CREATE TABLE `shottask`  (
  `id` int(0) NOT NULL,
  `task_name` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `task_descrip` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `task_status` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `task_user` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `task_type` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of shottask
-- ----------------------------
INSERT INTO `shottask` VALUES (1, 'SC001', '分镜', 'work', 'zhansna', 'layout');
INSERT INTO `shottask` VALUES (2, 'SC002', '合成', 'work', 'sanf', 'comp');
INSERT INTO `shottask` VALUES (3, 'SC003', '灯光', 'work', '王磊', 'light');

-- ----------------------------
-- Table structure for user
-- ----------------------------
DROP TABLE IF EXISTS `user`;
CREATE TABLE `user`  (
  `name` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `age` int(0) NULL DEFAULT NULL,
  `sex` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `id` int(0) NOT NULL AUTO_INCREMENT,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 3 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = DYNAMIC;

-- ----------------------------
-- Records of user
-- ----------------------------
INSERT INTO `user` VALUES ('zhansan', 12, 'men', 1);
INSERT INTO `user` VALUES ('lish', 34, 'women', 2);
INSERT INTO `user` VALUES ('asd', 23, 'sd', 3);

SET FOREIGN_KEY_CHECKS = 1;
