-- MariaDB dump 10.19  Distrib 10.4.24-MariaDB, for Win64 (AMD64)
--
-- Host: localhost    Database: db_praktikum
-- ------------------------------------------------------
-- Server version	10.4.24-MariaDB

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `mahasiswa`
--

DROP TABLE IF EXISTS `mahasiswa`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `mahasiswa` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `nim` varchar(255) NOT NULL,
  `nama` varchar(255) NOT NULL,
  `jurusan` varchar(255) NOT NULL,
  `jenis_kelamin` varchar(20) NOT NULL,
  `hobi` varchar(250) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=24 DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `mahasiswa`
--

LOCK TABLES `mahasiswa` WRITE;
/*!40000 ALTER TABLE `mahasiswa` DISABLE KEYS */;
INSERT INTO `mahasiswa` VALUES (5,'1901','Udin','Filsafat Meme','',''),(6,'1902','Mike','Pendidikan Gaming','',''),(7,'1903','Wazowski','Teknik Kedokteran','',''),(8,'2007703','Sekar','Filsafat Meme','Perempuan','0,PY_VAR5,PY_VAR5,PY_VAR5,PY_VAR5'),(14,'2004191','Azar','Pendidikan Gaming','Laki-laki','0,0,0,0'),(15,'2007703','Sekar Madu','Filsafat Meme','Perempuan','0,0,0,0'),(16,'2004191','M Azar','Pendidikan Gaming','Laki-laki','0'),(17,'10100101','Sekar MMM','Sastra Mesin','Perempuan','Bernyanyi'),(18,'2007703','Madu','Filsafat Meme','Perempuan','Bernyanyi,0,0,Ngoding'),(19,'1234321','Sekar','Sastra Mesin','Laki-laki','0,Bermain Game,0,Ngoding'),(20,'1234321','Azar','Teknik Kedokteran','Laki-laki','0,Bermain Game,0,Ngoding'),(21,'1234321','Aku','Filsafat Meme','Laki-laki','Bermain Game,Ngoding'),(22,'1234567','Sekar','Filsafat Meme','Laki-laki','Bernyanyi,Ngoding'),(23,'','','Filsafat Meme','Laki-laki','');
/*!40000 ALTER TABLE `mahasiswa` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2022-05-10 21:50:30
