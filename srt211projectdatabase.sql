-- MySQL dump 10.13  Distrib 8.0.36, for Win64 (x86_64)
--
-- Host: localhost    Database: project
-- ------------------------------------------------------
-- Server version	8.0.36

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `articles`
--

DROP TABLE IF EXISTS `articles`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `articles` (
  `idarticles` int NOT NULL AUTO_INCREMENT,
  `title` varchar(255) NOT NULL,
  `content` text NOT NULL,
  `publication_date` datetime DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`idarticles`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `articles`
--

LOCK TABLES `articles` WRITE;
/*!40000 ALTER TABLE `articles` DISABLE KEYS */;
INSERT INTO `articles` VALUES (2,'New Courses for 2024','In 2024, P1 Private School of Education is thrilled to unveil a fresh array of courses designed to equip students with cutting-edge skills and knowledge. These courses have been developed to meet the evolving educational needs of our students, incorporating contemporary topics and innovative teaching methodologies. The aim is to provide a diverse selection of subjects that cater to various interests and career aspirations, fostering a holistic learning environment.\r\n\r\nUpcoming Courses:\r\nArtificial Intelligence and Machine Learning: Delve into the world of AI and machine learning, exploring the foundations of neural networks, natural language processing, and robotics.\r\nSustainable Urban Planning: An interdisciplinary course focusing on sustainable development, eco-friendly infrastructure, and the creation of green spaces within urban settings.\r\nVirtual Reality and Game Design: A hands-on course where students learn the principles of VR environments and game design, including 3D modeling and user experience.\r\nDigital Marketing and Social Media: Covering the latest trends in digital marketing strategies, SEO, and the impactful use of social media for branding and community engagement.','2024-03-30 15:09:11'),(3,'Important Upcoming Dates\n','Register for Classes #1 - April 1, 2024\nDrop Classes for Refund - April 12, 2024\nLast Day for Tuition Payment - April 20, 2024\n\nRegister for Classes #2- June 1, 2024\nDrop Classes for Refund - June 12, 2024\nLast Day for Tuition Payment - June 20, 2024\n\nRegister for Classes #3- September 1, 2024\nDrop Classes for Refund - September 12, 2024\nLast Day for Tuition Payment - September 20, 2024\n\nThanksgiving - October 14, 2024\n\nRemembrance Day - November 11, 2024\n\nChristmas Holiday - December23, 2024 - Janruary 6,2025','2024-03-30 15:09:16'),(4,'Important Notice: Temporary Closure of P1 Private School of Education','In light of unforeseen circumstances, P1 Private School of Education will be temporarily closed for the day. This decision was made with the utmost concern for the safety and well-being of our students, faculty, and staff. We understand that this may cause inconvenience, but please be assured that the decision to close was not made lightly.\n\nReason for Closure\nDue to an emergency situation that has arisen within our local area, we have been advised by local authorities to close the school for the day to ensure the safety of our school community. The nature of the emergency is such that it requires immediate attention and precautionary measures to be taken.\n\nDuration of Closure\nThe school will be closed for the entire day, effective immediately. We are closely monitoring the situation in collaboration with local authorities and will provide updates regarding the reopening of the school as soon as possible.','2024-03-30 15:21:30'),(5,'Guide to Paying Your Tuition: Bank Transfers and Cash Payments at P1 Private School of Education','At P1 Private School of Education, we strive to make the process of paying tuition as convenient and secure as possible for our families. Understanding the importance of flexibility, we offer several payment options, including bank transfers and cash payments. This guide will walk you through the steps to ensure your tuition payment is processed smoothly and efficiently, regardless of the method you choose.\n\nPaying Tuition via Bank Transfer\nBank transfers are a popular choice for tuition payments due to their convenience and record-keeping benefits. To complete a bank transfer, please follow these steps:\n\nObtain School Bank Details: The first step is to obtain the official bank account details of P1 Private School of Education. This information can be found on the school’s website, in the tuition fees section, or by contacting our finance department directly.\n\nInitiate the Transfer: Log in to your online banking platform or visit your bank in person to initiate the transfer. You will need to provide the school\'s bank account number, sort code (if applicable), and the name on the account.\n\nInclude Student Information: It\'s crucial to include the student\'s name and identification number in the transfer description or reference field. This information ensures that the payment is accurately applied to the correct student account.\n\nVerify the Amount: Double-check the tuition amount before confirming the transfer. This reduces the risk of underpayments or overpayments and the need for adjustments later.\n\nConfirm the Transfer: Once you\'ve entered all the necessary information and reviewed it for accuracy, confirm the transfer.\n\nKeep a Record: After completing the transfer, save the confirmation receipt or transaction number. This will be your proof of payment and is essential for resolving any discrepancies.\n\nPaying Tuition in Cash\nWhile digital payments are encouraged for their convenience and security, we understand that some families prefer or require the option to pay in cash. If you choose to make a cash payment, please follow these guidelines:\n\nVisit the School’s Finance Office: Cash payments can be made in person at the school’s finance office. Please check the office hours to ensure the staff is available to assist you.\n\nPrepare the Exact Amount: To streamline the process, please bring the exact amount owed. The finance office can provide change if necessary, but exact payments expedite the process.\n\nReceive a Receipt: Upon making your cash payment, you will receive an official receipt from the finance office. This receipt is your proof of payment and should be kept for your records.\n\nAvoid Mailing Cash: For security reasons, we strongly advise against sending cash payments through the mail. In-person payments ensure that your funds are directly received and properly accounted for.\n\nIf you have anymore questions feel free to contact us at contacts@p1school.ca or call (416) 491-5050.','2024-03-30 17:15:30');
/*!40000 ALTER TABLE `articles` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `comments`
--

DROP TABLE IF EXISTS `comments`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `comments` (
  `idcomments` int NOT NULL AUTO_INCREMENT,
  `article_id` int NOT NULL,
  `author_name` varchar(255) NOT NULL,
  `comment` text NOT NULL,
  `comment_date` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`idcomments`),
  KEY `article_id_idx` (`article_id`),
  CONSTRAINT `article_id` FOREIGN KEY (`article_id`) REFERENCES `articles` (`idarticles`)
) ENGINE=InnoDB AUTO_INCREMENT=15 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `comments`
--

LOCK TABLES `comments` WRITE;
/*!40000 ALTER TABLE `comments` DISABLE KEYS */;
INSERT INTO `comments` VALUES (12,2,'ben10','Looking forward to the new classes that will be offered','2024-04-06 16:08:22'),(13,3,'Student1','Thank you for letting us know the dates','2024-04-06 16:13:20'),(14,5,'Student1','Thank you for the information\r\n','2024-04-06 17:45:21');
/*!40000 ALTER TABLE `comments` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `courses`
--

DROP TABLE IF EXISTS `courses`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `courses` (
  `idcourses` int NOT NULL AUTO_INCREMENT,
  `coursename` varchar(45) NOT NULL,
  `coursedescription` varchar(500) NOT NULL,
  `coursecost` int NOT NULL,
  PRIMARY KEY (`idcourses`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `courses`
--

LOCK TABLES `courses` WRITE;
/*!40000 ALTER TABLE `courses` DISABLE KEYS */;
INSERT INTO `courses` VALUES (1,'Biotechnology','This class explores the intersection of biology and technology, teaching students about the use of living organisms or their systems to develop or make products. It may cover topics such as genetic engineering, biofuel production, and pharmaceuticals, as well as ethical considerations in the field.',2000),(2,'Civil Engineering','In this course, students learn about the design, construction, and maintenance of infrastructure projects and systems in the public and private sector, including roads, buildings, airports, tunnels, dams, bridges, and systems for water supply and sewage treatment.',2000),(3,'Computer System Technology','This class delves into the hardware and software aspects of computer systems. It covers topics like system architecture, networking, system integration, and troubleshooting, with hands-on experience in maintaining and configuring computer systems.',2000),(4,'Software Engineering','This course introduces the principles and practices of software development. Students learn about the software lifecycle, including requirements analysis, design, coding, testing, and maintenance, along with project management and collaborative development practices.\n',2000),(5,'Social Service Worker','Students in this class study how to assist individuals, families, and communities to improve their well-being. It covers areas like psychology, sociology, counseling, and social justice, preparing students to work in various social services settings.',2000);
/*!40000 ALTER TABLE `courses` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `courseselection`
--

DROP TABLE IF EXISTS `courseselection`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `courseselection` (
  `selectionid` int NOT NULL AUTO_INCREMENT,
  `selectioncourse` varchar(255) NOT NULL,
  `user_id` int DEFAULT NULL,
  PRIMARY KEY (`selectionid`),
  KEY `user_id_idx` (`user_id`)
) ENGINE=InnoDB AUTO_INCREMENT=82 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `courseselection`
--

LOCK TABLES `courseselection` WRITE;
/*!40000 ALTER TABLE `courseselection` DISABLE KEYS */;
INSERT INTO `courseselection` VALUES (77,'Biotechnology',3),(78,'Civil Engineering',3),(79,'Computer System Technology',3),(80,'Software Engineering',3),(81,'Social Service Worker',3);
/*!40000 ALTER TABLE `courseselection` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `users`
--

DROP TABLE IF EXISTS `users`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `users` (
  `idusers` int NOT NULL AUTO_INCREMENT,
  `username` varchar(255) NOT NULL,
  `password` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `address` varchar(255) NOT NULL,
  `email` varchar(255) NOT NULL,
  `mobile` varchar(255) NOT NULL,
  PRIMARY KEY (`idusers`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `users`
--

LOCK TABLES `users` WRITE;
/*!40000 ALTER TABLE `users` DISABLE KEYS */;
INSERT INTO `users` VALUES (1,'bob123','P@ssw0rd','bob the builder','321 Finch Ave','bob@gmail.com','098-098-0987'),(2,'ben10','password','ben','123 hello street','ben@gmail.com','098-098-0987'),(3,'Student1','P@ssw0rd','Benjamin Yang','123 hello street','ben@gmail.com','098-098-0987');
/*!40000 ALTER TABLE `users` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping events for database 'project'
--

--
-- Dumping routines for database 'project'
--
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2024-04-06 17:53:05
