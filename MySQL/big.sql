/*
 Navicat Premium Data Transfer

 Source Server         : root
 Source Server Type    : MySQL
 Source Server Version : 80019
 Source Host           : localhost:3306
 Source Schema         : big

 Target Server Type    : MySQL
 Target Server Version : 80019
 File Encoding         : 65001

 Date: 15/05/2020 23:01:58
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
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of asset
-- ----------------------------
INSERT INTO `asset` VALUES (1, 'car', 'character', 'big', '2020-04-13 10:36:46', 'zhansan');
INSERT INTO `asset` VALUES (2, 'tree', 'character', 'big', '2020-04-29 06:31:08', 'asda');
INSERT INTO `asset` VALUES (15, 'tree', 'character', 'big', '2020-04-29 06:31:08', 'asda');
INSERT INTO `asset` VALUES (16, 'cat', 'character', 'big', '2020-04-29 07:03:29', 'qwe');

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
) ENGINE = InnoDB AUTO_INCREMENT = 19 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of eps
-- ----------------------------
INSERT INTO `eps` VALUES (1, 'EP001', '2020-04-10 18:17:49.270803', 'zahnsan', 'big');
INSERT INTO `eps` VALUES (2, 'EP002', '2020-04-10 18:17:55.080514', 'zahnsan', 'big');
INSERT INTO `eps` VALUES (3, 'EP003', '2020-04-10 18:17:55.912290', 'zahnsan', 'big');
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
) ENGINE = InnoDB AUTO_INCREMENT = 13 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = DYNAMIC;

-- ----------------------------
-- Records of project
-- ----------------------------
INSERT INTO `project` VALUES (1, 'big', '{\"databasecode\":\"big\",\"chinesename\":\"大熊兔\",\"date\":\"2020.3.23\",\"auther\":\"张三\"}', '[\'Big/asset/work\', \'Big/asset/publish\', \'Big/shot/work\', \'Big/shot/publish\']', '{\'asset\': {\'mod\': \'模型\', \'shd\': \'材质\', \'rig\': \'绑定\', \'cloth\': \'布料\', \'big\': \'大熊兔\'}}', '{\'shot\': {\'vfx\': \'特效\', \'comp\': \'合成\', \'light\': \'灯光\'}}');

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
INSERT INTO `shottask` VALUES (2, 'SC002', '合成', 'approve', 'sanf', 'comp');
INSERT INTO `shottask` VALUES (3, 'SC003', '灯光', 'wait', '王磊', 'light');
INSERT INTO `shottask` VALUES (4, '213', '123', '工作中', '123', 'layout');
INSERT INTO `shottask` VALUES (5, '213', '123', 'wait', '123', 'layout');

-- ----------------------------
-- Table structure for user
-- ----------------------------
DROP TABLE IF EXISTS `user`;
CREATE TABLE `user`  (
  `id` int(0) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `age` int(0) NULL DEFAULT NULL,
  `sex` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `address` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `department` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `email` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `phone` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `password` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `account` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 6 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = DYNAMIC;

-- ----------------------------
-- Records of user
-- ----------------------------
INSERT INTO `user` VALUES (1, 'zhansan', 12, 'men', '123', '特效', '785415581@qq.com', '15188221619', '123', 'pa');
INSERT INTO `user` VALUES (2, 'lish', 34, 'women', '123', '特效', '785415581@qq.com', '15188221619', '1234', 'qinjiaxin1');
INSERT INTO `user` VALUES (3, '秦家鑫', 18, '男', '淞泽家园', '技术部', '785415581@qq.com', '15188221619', 'qinjiaxin', 'qinjiaxin');
INSERT INTO `user` VALUES (4, '安琪', 19, '男', '尹山湖', '技术组', '123456789@qq.com', '110', 'anqi', 'anqi');
INSERT INTO `user` VALUES (5, '金环', 20, '女', '菁英公寓', '技术组', '123456789@qq.com', '119', 'jinhuan', 'jinhuan');
INSERT INTO `user` VALUES (6, 'qinjiaxin', 12, '男', '淞泽', '动画', '大苏打', '大苏打', 'asd', 'asd');

SET FOREIGN_KEY_CHECKS = 1;
