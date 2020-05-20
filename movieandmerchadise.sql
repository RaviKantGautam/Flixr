-- phpMyAdmin SQL Dump
-- version 5.0.1
-- https://www.phpmyadmin.net/
--
-- Host: localhost
-- Generation Time: May 17, 2020 at 01:58 PM
-- Server version: 10.4.11-MariaDB
-- PHP Version: 7.4.2

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `movieandmerchadise`
--

-- --------------------------------------------------------

--
-- Table structure for table `admin`
--

CREATE TABLE `admin` (
  `email` varchar(40) NOT NULL,
  `password` varchar(29) NOT NULL,
  `type` varchar(12) NOT NULL,
  `mobile` bigint(12) NOT NULL,
  `otp` varchar(10) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `admin`
--

INSERT INTO `admin` (`email`, `password`, `type`, `mobile`, `otp`) VALUES
('a12@gmail.com', 'admin', 'Admin', 9876543456, 'None'),
('a@gmail.com', '123', 'Super-Admin', 1234567899, NULL),
('annn@gmail.com', 'admin', 'Admin', 7340761885, 'None'),
('batejurago@mailinator.com', 'Pa$$w0rd!', 'Admin', 8532130, NULL),
('bunyluka@mailinator.com', 'Pa$$w0rd!', 'Super-Admin', 4524078501, NULL),
('buqygyz@mailinator.com', 'Pa$$w0rd!', 'Super-Admin', 9831743445, NULL),
('c@gmail.com', '12345', 'Admin', 7340761885, NULL),
('celaqoge@mailinator.net', 'Pa$$w0rd!', 'Super-Admin', 7185254961, NULL),
('dokox@mailinator.net', 'Pa$$w0rd!', 'Super-Admin', 8416387634, NULL),
('f@gmail.com', '12345', 'Admin', 7340761885, NULL),
('fyga@mailinator.com', 'Pa$$w0rd!', 'Super-Admin', 8096423393, NULL),
('guco@mailinator.net', 'Pa$$w0rd!', 'Super-Admin', 5118596882, NULL),
('gugi@mailinator.net', 'Pa$$w0rd!', 'Super-Admin', 18671865761, NULL),
('h@gmail.com', '12345', 'Admin', 7340761885, NULL),
('hesex@mailinator.com', 'Pa$$w0rd!', 'Super-Admin', 16016466291, NULL),
('hoxabubi@mailinator.net', 'Pa$$w0rd!', 'Super-Admin', 1297687989, NULL),
('keqojuq@mailinator.com', 'Pa$$w0rd!', 'Super-Admin', 7451327011, NULL),
('kudunote@mailinator.com', 'Pa$$w0rd!', 'Super-Admin', 1968405583, NULL),
('lapafaferi@mailinator.net', 'Pa$$w0rd!', 'Admin', 5375198622, NULL),
('pa@gmal.com', '123', 'Admin', 7340761885, NULL),
('ramesh@gmail.com', 'demo', 'Admin', 6280276218, 'None'),
('ravikantgautamjazz@gmail.com', 'demo', 'Super-Admin', 6280276218, 'None'),
('recyf@mailinator.com', 'Pa$$w0rd!', 'Super-Admin', 16094991838, NULL),
('sofiz@mailinator.com', 'Pa$$w0rd!', 'Super-Admin', 9891157911, NULL),
('sonia@gmail.com', 'demo', 'Super-Admin', 6280276218, 'None'),
('terubamewa@mailinator.net', 'Pa$$w0rd!', 'Admin', 3049911789, NULL),
('zyban@mailinator.com', 'Pa$$w0rd!', 'Super-Admin', 1136074877, NULL);

-- --------------------------------------------------------

--
-- Table structure for table `bill`
--

CREATE TABLE `bill` (
  `billID` int(11) NOT NULL,
  `datatime` datetime NOT NULL,
  `grandtotal` decimal(10,0) NOT NULL,
  `payment_method` varchar(100) NOT NULL,
  `city` varchar(200) NOT NULL,
  `zipcode` int(11) NOT NULL,
  `address` text NOT NULL,
  `remarks` text DEFAULT NULL,
  `email` varchar(200) NOT NULL,
  `status` varchar(100) NOT NULL,
  `personrecieved` varchar(100) DEFAULT NULL,
  `trackid` int(11) DEFAULT NULL,
  `companyname` varchar(300) DEFAULT NULL,
  `cancelledremarks` text DEFAULT NULL,
  `trackurl` varchar(100) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `bill`
--

INSERT INTO `bill` (`billID`, `datatime`, `grandtotal`, `payment_method`, `city`, `zipcode`, `address`, `remarks`, `email`, `status`, `personrecieved`, `trackid`, `companyname`, `cancelledremarks`, `trackurl`) VALUES
(1, '2020-04-09 11:56:17', '9186', 'cod', 'Jalandhar', 811334, 'Nulla eum explicabo', 'Laborum et quia fugi', 'client@gmail.com', 'Dispatched', 'Kapil Ji', 143456, 'Wiley Norris LLC', NULL, 'https://www.ralozu.me'),
(2, '2020-04-09 12:00:21', '1759', 'cod', 'Chandigarh', 170862, 'Deserunt consequuntu', 'Laborum et quia fugi', 'client@gmail.com', 'Dispatched', 'Kapil Ji', 143456, 'Wiley Norris LLC', NULL, 'https://www.ralozu.me'),
(3, '2020-04-09 12:11:16', '1759', 'online', 'Ludhiana', 619382, 'Sunt quia enim eiusm', 'Illum facilis nostr', 'client@gmail.com', 'cancelled', NULL, NULL, NULL, 'i don\'t have enough money', NULL),
(4, '2020-04-09 12:18:00', '1759', 'cod', 'Ludhiana', 619382, 'Sunt quia enim eiusm', 'Illum facilis nostr', 'client@gmail.com', 'cancelled', NULL, NULL, NULL, 'i can\'t pay at the moment', NULL),
(5, '2020-05-09 06:52:18', '966', 'cod', 'Ludhiana', 143001, 'putlighar', 'Incididunt voluptati', 'ravikantgautamjazz@gmail.com', 'Shipped', 'suraj', 312345, 'Todd Hyde Associates', NULL, 'https://www.tazeripuroxicir.mobi'),
(6, '2020-05-09 06:52:20', '966', 'cod', 'Ludhiana', 143001, 'putlighar', 'Incididunt voluptati', 'ravikantgautamjazz@gmail.com', 'Shipped', 'suraj', 312345, 'Todd Hyde Associates', NULL, 'https://www.tazeripuroxicir.mobi'),
(7, '2020-05-09 06:52:39', '966', 'online', 'Ludhiana', 143001, 'putlighar', 'Incididunt voluptati', 'ravikantgautamjazz@gmail.com', 'Shipped', 'suraj', 312345, 'Todd Hyde Associates', NULL, 'https://www.tazeripuroxicir.mobi'),
(8, '2020-05-09 07:37:37', '2172', 'online', 'Amritsar', 143001, 'putlighar', 'Incididunt voluptati', 'ravikantgautamjazz@gmail.com', 'Shipped', 'suraj', 312345, 'Todd Hyde Associates', NULL, 'https://www.tazeripuroxicir.mobi'),
(9, '2020-05-10 03:38:38', '1259', 'cod', 'Patiala', 232575, 'Fugit inventore vel', 'Incididunt voluptati', 'ravikantgautamjazz@gmail.com', 'Shipped', NULL, 312345, 'Todd Hyde Associates', NULL, 'https://www.tazeripuroxicir.mobi'),
(10, '2020-05-10 03:38:40', '1259', 'cod', 'Patiala', 232575, 'Fugit inventore vel', 'Incididunt voluptati', 'ravikantgautamjazz@gmail.com', 'Shipped', NULL, 312345, 'Todd Hyde Associates', NULL, 'https://www.tazeripuroxicir.mobi'),
(11, '2020-05-10 03:38:40', '1259', 'cod', 'Patiala', 232575, 'Fugit inventore vel', 'Incididunt voluptati', 'ravikantgautamjazz@gmail.com', 'Shipped', NULL, 312345, 'Todd Hyde Associates', NULL, 'https://www.tazeripuroxicir.mobi'),
(12, '2020-05-10 03:38:40', '1259', 'cod', 'Patiala', 232575, 'Fugit inventore vel', 'Incididunt voluptati', 'ravikantgautamjazz@gmail.com', 'Shipped', NULL, 312345, 'Todd Hyde Associates', NULL, 'https://www.tazeripuroxicir.mobi'),
(13, '2020-05-10 03:38:41', '1259', 'cod', 'Patiala', 232575, 'Fugit inventore vel', 'Incididunt voluptati', 'ravikantgautamjazz@gmail.com', 'Shipped', NULL, 312345, 'Todd Hyde Associates', NULL, 'https://www.tazeripuroxicir.mobi'),
(14, '2020-05-10 03:43:08', '1259', 'cod', 'Patiala', 232575, 'Fugit inventore vel', 'Incididunt voluptati', 'ravikantgautamjazz@gmail.com', 'Shipped', NULL, 312345, 'Todd Hyde Associates', NULL, 'https://www.tazeripuroxicir.mobi'),
(15, '2020-05-10 03:47:07', '1259', 'cod', 'Patiala', 232575, 'Fugit inventore vel', 'Incididunt voluptati', 'ravikantgautamjazz@gmail.com', 'Shipped', NULL, 312345, 'Todd Hyde Associates', NULL, 'https://www.tazeripuroxicir.mobi'),
(16, '2020-05-10 03:48:25', '1259', 'cod', 'Patiala', 232575, 'Fugit inventore vel', 'Incididunt voluptati', 'ravikantgautamjazz@gmail.com', 'Shipped', NULL, 312345, 'Todd Hyde Associates', NULL, 'https://www.tazeripuroxicir.mobi'),
(17, '2020-05-10 03:58:58', '644', 'cod', 'Ludhiana', 239971, 'Blanditiis et iste l', 'Incididunt voluptati', 'ravikantgautamjazz@gmail.com', 'Shipped', NULL, 312345, 'Todd Hyde Associates', NULL, 'https://www.tazeripuroxicir.mobi'),
(18, '2020-05-10 04:01:00', '422', 'cod', 'Jalandhar', 851532, 'Similique eaque nost', 'Incididunt voluptati', 'ravikantgautamjazz@gmail.com', 'Shipped', NULL, 312345, 'Todd Hyde Associates', NULL, 'https://www.tazeripuroxicir.mobi'),
(19, '2020-05-10 04:03:12', '364', 'cod', 'Chandigarh', 429752, 'Optio aut et esse a', 'Incididunt voluptati', 'ravikantgautamjazz@gmail.com', 'Shipped', NULL, 312345, 'Todd Hyde Associates', NULL, 'https://www.tazeripuroxicir.mobi'),
(20, '2020-05-10 04:19:52', '364', 'cod', 'Chandigarh', 429752, 'Optio aut et esse a', 'Incididunt voluptati', 'ravikantgautamjazz@gmail.com', 'Shipped', NULL, 312345, 'Todd Hyde Associates', NULL, 'https://www.tazeripuroxicir.mobi'),
(21, '2020-05-10 04:19:54', '364', 'cod', 'Chandigarh', 429752, 'Optio aut et esse a', 'Incididunt voluptati', 'ravikantgautamjazz@gmail.com', 'Shipped', NULL, 312345, 'Todd Hyde Associates', NULL, 'https://www.tazeripuroxicir.mobi'),
(22, '2020-05-10 04:20:03', '364', 'cod', 'Chandigarh', 429752, 'Optio aut et esse a', 'Incididunt voluptati', 'ravikantgautamjazz@gmail.com', 'Shipped', NULL, 312345, 'Todd Hyde Associates', NULL, 'https://www.tazeripuroxicir.mobi'),
(23, '2020-05-10 04:21:48', '364', 'cod', 'Chandigarh', 429752, 'Optio aut et esse a', 'Incididunt voluptati', 'ravikantgautamjazz@gmail.com', 'Shipped', NULL, 312345, 'Todd Hyde Associates', NULL, 'https://www.tazeripuroxicir.mobi'),
(24, '2020-05-10 04:21:50', '364', 'cod', 'Chandigarh', 429752, 'Optio aut et esse a', 'Incididunt voluptati', 'ravikantgautamjazz@gmail.com', 'Shipped', NULL, 312345, 'Todd Hyde Associates', NULL, 'https://www.tazeripuroxicir.mobi'),
(25, '2020-05-10 04:22:55', '364', 'cod', 'Chandigarh', 429752, 'Optio aut et esse a', 'Incididunt voluptati', 'ravikantgautamjazz@gmail.com', 'Shipped', NULL, 312345, 'Todd Hyde Associates', NULL, 'https://www.tazeripuroxicir.mobi'),
(26, '2020-05-10 04:25:23', '364', 'cod', 'Chandigarh', 429752, 'Optio aut et esse a', 'Incididunt voluptati', 'ravikantgautamjazz@gmail.com', 'Dispatched', 'Kabir', 312345, 'Todd Hyde Associates', NULL, 'https://www.tazeripuroxicir.mobi'),
(27, '2020-05-10 04:26:25', '364', 'cod', 'Chandigarh', 429752, 'Optio aut et esse a', 'Incididunt voluptati', 'ravikantgautamjazz@gmail.com', 'Dispatched', 'rajan', 312345, 'Todd Hyde Associates', NULL, 'https://www.tazeripuroxicir.mobi'),
(28, '2020-05-10 04:34:58', '364', 'cod', 'Chandigarh', 429752, 'Optio aut et esse a', 'Incididunt voluptati', 'ravikantgautamjazz@gmail.com', 'Dispatched', 'SRK', 312345, 'Todd Hyde Associates', NULL, 'https://www.tazeripuroxicir.mobi'),
(29, '2020-05-10 16:19:28', '2078', 'cod', 'Jalandhar', 843766, 'Quaerat ullamco cill', 'Quaerat hic placeat', 'ravikantgautamjazz@gmail.com', 'cancelled', NULL, NULL, NULL, 'not enough money', NULL),
(30, '2020-05-11 05:14:59', '1774', 'cod', 'Jalandhar', 654495, 'Ut velit fugiat esse', 'Error quaerat commod', 'ravikantgautamjazz@gmail.com', 'pending', NULL, NULL, NULL, NULL, NULL);

-- --------------------------------------------------------

--
-- Table structure for table `billdetail`
--

CREATE TABLE `billdetail` (
  `billdetailid` int(11) NOT NULL,
  `price` float(10,2) NOT NULL,
  `quantity` int(11) NOT NULL,
  `merchandise` int(11) NOT NULL,
  `billid` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `billdetail`
--

INSERT INTO `billdetail` (`billdetailid`, `price`, `quantity`, `merchandise`, `billid`) VALUES
(1, 205.00, 914, 112, 4),
(2, 144.00, 845, 113, 4),
(3, 114.00, 966, 109, 5),
(4, 114.00, 966, 109, 6),
(5, 114.00, 966, 109, 7),
(6, 114.00, 966, 109, 8),
(7, 240.00, 456, 105, 8),
(8, 285.00, 750, 110, 8),
(9, 217.00, 895, 106, 9),
(10, 143.00, 364, 107, 9),
(11, 217.00, 895, 106, 10),
(12, 143.00, 364, 107, 10),
(13, 217.00, 895, 106, 11),
(14, 143.00, 364, 107, 11),
(15, 217.00, 895, 106, 12),
(16, 143.00, 364, 107, 12),
(17, 217.00, 895, 106, 13),
(18, 143.00, 364, 107, 13),
(19, 217.00, 895, 106, 14),
(20, 143.00, 364, 107, 14),
(21, 217.00, 895, 106, 15),
(22, 143.00, 364, 107, 15),
(23, 217.00, 895, 106, 16),
(24, 143.00, 364, 107, 16),
(25, 111.00, 644, 109, 17),
(26, 205.00, 422, 111, 18),
(27, 141.00, 364, 107, 19),
(28, 141.00, 364, 107, 20),
(29, 141.00, 364, 107, 21),
(30, 141.00, 364, 107, 22),
(31, 141.00, 364, 107, 23),
(32, 141.00, 364, 107, 24),
(33, 141.00, 364, 107, 25),
(34, 141.00, 364, 107, 26),
(35, 141.00, 364, 107, 27),
(36, 141.00, 364, 107, 28),
(37, 282.00, 250, 110, 29),
(38, 204.00, 1828, 112, 29),
(39, 283.00, 1090, 104, 30),
(40, 236.00, 684, 105, 30);

-- --------------------------------------------------------

--
-- Table structure for table `booking`
--

CREATE TABLE `booking` (
  `id` int(11) NOT NULL,
  `showtimeid` int(11) NOT NULL,
  `seats` text NOT NULL,
  `grandtotal` float(10,2) NOT NULL,
  `noofseats` int(11) NOT NULL,
  `useremail` varchar(100) NOT NULL,
  `datetime` datetime NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `booking`
--

INSERT INTO `booking` (`id`, `showtimeid`, `seats`, `grandtotal`, `noofseats`, `useremail`, `datetime`) VALUES
(1, 11, '18,19', 1800.00, 2, 'client@gmail.com', '2020-05-06 12:11:21'),
(2, 11, '35,36', 1800.00, 2, 'client@gmail.com', '2020-05-06 13:49:35'),
(3, 11, '16', 900.00, 1, 'client@gmail.com', '2020-05-06 15:36:06'),
(4, 11, '15', 900.00, 1, 'client@gmail.com', '2020-05-06 15:38:37'),
(5, 11, '41,43', 1800.00, 2, 'client@gmail.com', '2020-05-06 15:39:15'),
(6, 11, '46,47', 1800.00, 2, 'client@gmail.com', '2020-05-06 15:40:07'),
(7, 11, '66,67', 180000.00, 2, 'client@gmail.com', '2020-05-06 16:00:05'),
(8, 11, '31,45', 1800.00, 2, 'ravikantgautamjazz@gmail.com', '2020-05-09 07:26:28'),
(9, 11, '29,30', 1800.00, 2, 'ravikantgautamjazz@gmail.com', '2020-05-10 16:21:38'),
(10, 11, '29,30', 1800.00, 2, 'ravikantgautamjazz@gmail.com', '2020-05-10 16:23:20'),
(11, 7, '22,23', 1980.00, 2, 'ravikantgautamjazz@gmail.com', '2020-05-11 05:23:28');

-- --------------------------------------------------------

--
-- Table structure for table `customers`
--

CREATE TABLE `customers` (
  `email` varchar(100) NOT NULL,
  `password` varchar(50) NOT NULL,
  `dob` date NOT NULL,
  `gender` varchar(20) NOT NULL,
  `mobilenumber` varchar(13) NOT NULL,
  `otp` varchar(10) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `customers`
--

INSERT INTO `customers` (`email`, `password`, `dob`, `gender`, `mobilenumber`, `otp`) VALUES
('bakomaho@mailinator.net', 'Pa$$w0rd!', '2019-11-11', 'male', '3948877791', NULL),
('client@gmail.com', 'password', '2020-04-05', 'male', '1234567890', NULL),
('ravikantgautamjazz@gmail.com', 'ravi', '2020-05-13', 'male', '6280276218', 'None');

-- --------------------------------------------------------

--
-- Table structure for table `merchandise`
--

CREATE TABLE `merchandise` (
  `productid` int(11) NOT NULL,
  `productname` varchar(100) NOT NULL,
  `price` float NOT NULL,
  `stock` int(11) DEFAULT NULL,
  `movieid` int(11) NOT NULL,
  `productdescription` text DEFAULT NULL,
  `photo1` text DEFAULT NULL,
  `photo2` text DEFAULT NULL,
  `photo3` text DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `merchandise`
--

INSERT INTO `merchandise` (`productid`, `productname`, `price`, `stock`, `movieid`, `productdescription`, `photo1`, `photo2`, `photo3`) VALUES
(103, 'Mugs', 649, 191, 872, 'Playing in robes of black and yellow, you can now support your house Quidditch team with this matching tee from Harry Potter. Complete with the Hogwart\'s crest over the left-hand side and silver lettering decorating the back, this marvellous tee will look totally patriotic from the towering stands! Official merchandise.', '60015product-9.jpg', '27250fashion-fashionable-footwear-leather-267301.jpg', '67793footwear-leather-shoes-wear-267320.jpg'),
(104, 'Puma', 545, 281, 873, 'Playing in robes of black and yellow, you can now support your house Quidditch team with this matching tee from Harry Potter. Complete with the Hogwart\'s crest over the left-hand side and silver lettering decorating the back, this marvellous tee will look totally patriotic from the towering stands! Official merchandise.', '14188product-7.jpg', '78714Daddys_Lil_Monster_-_mug-min_280x.webp', '32145product15.jpg'),
(105, 'Puma', 114, 230, 860, 'Playing in robes of black and yellow, you can now support your house Quidditch team with this matching tee from Harry Potter. Complete with the Hogwart\'s crest over the left-hand side and silver lettering decorating the back, this marvellous tee will look totally patriotic from the towering stands! Official merchandise.', '17533close-up-photography-of-red-and-black-nike-running-shoe-786003.jpg', '94427product9.jpg', '28712product-13.jpg'),
(106, 'Mugs', 895, 216, 856, 'Playing in robes of black and yellow, you can now support your house Quidditch team with this matching tee from Harry Potter. Complete with the Hogwart\'s crest over the left-hand side and silver lettering decorating the back, this marvellous tee will look totally patriotic from the towering stands! Official merchandise.', '37110product-1.jpg', '95391category4.png', '44309product-6.jpg'),
(107, 'necklace', 182, 139, 858, 'Playing in robes of black and yellow, you can now support your house Quidditch team with this matching tee from Harry Potter. Complete with the Hogwart\'s crest over the left-hand side and silver lettering decorating the back, this marvellous tee will look totally patriotic from the towering stands! Official merchandise.', '2262834.jpg', '90084product-18.jpg', '93191photo-of-nike-shoes-1598505.jpg'),
(108, 'Cooper Hogan', 145, 218, 863, 'Playing in robes of black and yellow, you can now support your house Quidditch team with this matching tee from Harry Potter. Complete with the Hogwart\'s crest over the left-hand side and silver lettering decorating the back, this marvellous tee will look totally patriotic from the towering stands! Official merchandise.', '2810121320028214_280x.webp', '1053339.jpg', '46236blog12.jpg'),
(109, 'Lehnga', 322, 109, 870, 'Playing in robes of black and yellow, you can now support your house Quidditch team with this matching tee from Harry Potter. Complete with the Hogwart\'s crest over the left-hand side and silver lettering decorating the back, this marvellous tee will look totally patriotic from the towering stands! Official merchandise.', '42410product9.jpg', '28432man-sitting-on-ledge-1306248.jpg', '84614unpaired-yellow-dr-martens-lace-up-boot-1159670.jpg'),
(110, 'Mugs', 250, 281, 864, 'Playing in robes of black and yellow, you can now support your house Quidditch team with this matching tee from Harry Potter. Complete with the Hogwart\'s crest over the left-hand side and silver lettering decorating the back, this marvellous tee will look totally patriotic from the towering stands! Official merchandise.', '89930man-wearing-nike-shoes-sitting-on-wooden-bench-2065695.jpg', '88648blur-close-up-depth-of-field-fashion-1478442.jpg', '68666537.jpg'),
(111, 'Winter Cheater', 422, 204, 859, 'Playing in robes of black and yellow, you can now support your house Quidditch team with this matching tee from Harry Potter. Complete with the Hogwart\'s crest over the left-hand side and silver lettering decorating the back, this marvellous tee will look totally patriotic from the towering stands! Official merchandise.', '2150020.jpg', '27696121319027485_280x.webp', '83175blog13.jpg'),
(112, 'Puma', 914, 202, 861, 'Playing in robes of black and yellow, you can now support your house Quidditch team with this matching tee from Harry Potter. Complete with the Hogwart\'s crest over the left-hand side and silver lettering decorating the back, this marvellous tee will look totally patriotic from the towering stands! Official merchandise.', '60314product17.jpg', '65766product-18.jpg', '6539882017026126_280x.webp'),
(113, 'Lehnga', 845, 143, 854, 'Playing in robes of black and yellow, you can now support your house Quidditch team with this matching tee from Harry Potter. Complete with the Hogwart\'s crest over the left-hand side and silver lettering decorating the back, this marvellous tee will look totally patriotic from the towering stands! Official merchandise.', '72559man-wearing-nike-shoes-sitting-on-wooden-bench-2065695.jpg', '75355product-1.jpg', '76262100419026752_280x.webp'),
(114, 'Kids Shoes', 674, 110, 873, 'Playing in robes of black and yellow, you can now support your house Quidditch team with this matching tee from Harry Potter. Complete with the Hogwart\'s crest over the left-hand side and silver lettering decorating the back, this marvellous tee will look totally patriotic from the towering stands! Official merchandise.', '3204963.jpg', '83758footwear-leather-shoes-wear-267320.jpg', '1206093019026586_280x.webp'),
(115, 'Mugs', 629, 115, 866, 'Playing in robes of black and yellow, you can now support your house Quidditch team with this matching tee from Harry Potter. Complete with the Hogwart\'s crest over the left-hand side and silver lettering decorating the back, this marvellous tee will look totally patriotic from the towering stands! Official merchandise.', '12203product16.jpg', '7851521320028215_280x.webp', '71010250.jpg'),
(116, 'T-shirts', 944, 210, 870, 'Playing in robes of black and yellow, you can now support your house Quidditch team with this matching tee from Harry Potter. Complete with the Hogwart\'s crest over the left-hand side and silver lettering decorating the back, this marvellous tee will look totally patriotic from the towering stands! Official merchandise.', '50490blur-close-up-depth-of-field-fashion-1478442.jpg', '74149100419026752_280x.webp', '51184product-13.jpg'),
(117, 'T-shirts', 886, 229, 866, 'Playing in robes of black and yellow, you can now support your house Quidditch team with this matching tee from Harry Potter. Complete with the Hogwart\'s crest over the left-hand side and silver lettering decorating the back, this marvellous tee will look totally patriotic from the towering stands! Official merchandise.', '35752category3.png', '6652820320028149_280x.webp', '8881621320028215_280x.webp'),
(118, 'sport & shoes', 510, 255, 857, 'Playing in robes of black and yellow, you can now support your house Quidditch team with this matching tee from Harry Potter. Complete with the Hogwart\'s crest over the left-hand side and silver lettering decorating the back, this marvellous tee will look totally patriotic from the towering stands! Official merchandise.', '56086537.jpg', '71579unpaired-yellow-dr-martens-lace-up-boot-1159670.jpg', '13113product17.jpg'),
(119, 'Winter Cheater', 626, 263, 855, 'Playing in robes of black and yellow, you can now support your house Quidditch team with this matching tee from Harry Potter. Complete with the Hogwart\'s crest over the left-hand side and silver lettering decorating the back, this marvellous tee will look totally patriotic from the towering stands! Official merchandise.', '83904footwear-leather-shoes-wear-267320.jpg', '64895130.jpg', '73547product-13.jpg'),
(120, 'Kids Shoes', 786, 181, 866, 'Playing in robes of black and yellow, you can now support your house Quidditch team with this matching tee from Harry Potter. Complete with the Hogwart\'s crest over the left-hand side and silver lettering decorating the back, this marvellous tee will look totally patriotic from the towering stands! Official merchandise.', '56868category6.png', '14717product-18.jpg', '3054041.jpg'),
(121, 'bracklets', 639, 150, 873, 'Playing in robes of black and yellow, you can now support your house Quidditch team with this matching tee from Harry Potter. Complete with the Hogwart\'s crest over the left-hand side and silver lettering decorating the back, this marvellous tee will look totally patriotic from the towering stands! Official merchandise.', '23468deal1.jpg', '57519product-6.jpg', '89254close-up-photo-of-diamond-stud-silver-colored-eternity-ring-691046.jpg'),
(122, 'Kids Shoes', 210, 287, 867, 'Playing in robes of black and yellow, you can now support your house Quidditch team with this matching tee from Harry Potter. Complete with the Hogwart\'s crest over the left-hand side and silver lettering decorating the back, this marvellous tee will look totally patriotic from the towering stands! Official merchandise.', '60673391.jpg', '75340product-7.jpg', '26062category9.png'),
(123, 'Formal Wear', 816, 276, 870, 'Playing in robes of black and yellow, you can now support your house Quidditch team with this matching tee from Harry Potter. Complete with the Hogwart\'s crest over the left-hand side and silver lettering decorating the back, this marvellous tee will look totally patriotic from the towering stands! Official merchandise.', '50919category5.png', '79580product-5.jpg', '38420product8.jpg'),
(124, 'T-shirts', 873, 154, 864, 'Playing in robes of black and yellow, you can now support your house Quidditch team with this matching tee from Harry Potter. Complete with the Hogwart\'s crest over the left-hand side and silver lettering decorating the back, this marvellous tee will look totally patriotic from the towering stands! Official merchandise.', '14182product-1.jpg', '90659product19.jpg', '8124121.jpg'),
(125, 'Cooper Hogan', 494, 252, 872, 'Playing in robes of black and yellow, you can now support your house Quidditch team with this matching tee from Harry Potter. Complete with the Hogwart\'s crest over the left-hand side and silver lettering decorating the back, this marvellous tee will look totally patriotic from the towering stands! Official merchandise.', '32609blog12.jpg', '16772391.jpg', '16899blog13.jpg'),
(126, 'Cooper Hogan', 871, 122, 873, 'Playing in robes of black and yellow, you can now support your house Quidditch team with this matching tee from Harry Potter. Complete with the Hogwart\'s crest over the left-hand side and silver lettering decorating the back, this marvellous tee will look totally patriotic from the towering stands! Official merchandise.', '27002product19.jpg', '85782fashion-fashionable-footwear-leather-267301.jpg', '94351product-16.jpg'),
(127, 'Marvel Cups', 267, 249, 863, 'Playing in robes of black and yellow, you can now support your house Quidditch team with this matching tee from Harry Potter. Complete with the Hogwart\'s crest over the left-hand side and silver lettering decorating the back, this marvellous tee will look totally patriotic from the towering stands! Official merchandise.', '80757black-and-white-close-up-jewellery-jewelry-265906.jpg', '24956blue-nike-low-top-shoes-637076.jpg', '8196693019026586_280x.webp'),
(128, 'Check Shirts', 648, 215, 856, 'Playing in robes of black and yellow, you can now support your house Quidditch team with this matching tee from Harry Potter. Complete with the Hogwart\'s crest over the left-hand side and silver lettering decorating the back, this marvellous tee will look totally patriotic from the towering stands! Official merchandise.', '87821207.jpg', '93235category7.png', '70546197.jpg'),
(129, 'T-shirts', 767, 120, 862, 'Playing in robes of black and yellow, you can now support your house Quidditch team with this matching tee from Harry Potter. Complete with the Hogwart\'s crest over the left-hand side and silver lettering decorating the back, this marvellous tee will look totally patriotic from the towering stands! Official merchandise.', '8827263.jpg', '54281product-11.jpg', '11703close-up-photo-of-ring-with-diamonds-1457801.jpg'),
(130, 'bracklets', 987, 251, 857, 'Playing in robes of black and yellow, you can now support your house Quidditch team with this matching tee from Harry Potter. Complete with the Hogwart\'s crest over the left-hand side and silver lettering decorating the back, this marvellous tee will look totally patriotic from the towering stands! Official merchandise.', '45875product9.jpg', '65016347.jpg', '9826121320028216_280x.webp'),
(131, 'Formal Wear', 131, 102, 872, 'Playing in robes of black and yellow, you can now support your house Quidditch team with this matching tee from Harry Potter. Complete with the Hogwart\'s crest over the left-hand side and silver lettering decorating the back, this marvellous tee will look totally patriotic from the towering stands! Official merchandise.', '37871product17.jpg', '25363627.jpg', '94891blog13.jpg'),
(132, 'T-shirts', 683, 275, 856, 'Playing in robes of black and yellow, you can now support your house Quidditch team with this matching tee from Harry Potter. Complete with the Hogwart\'s crest over the left-hand side and silver lettering decorating the back, this marvellous tee will look totally patriotic from the towering stands! Official merchandise.', '6049930.jpg', '50835product11.jpg', '4686063.jpg'),
(133, 'Formal Wear', 195, 168, 869, 'Playing in robes of black and yellow, you can now support your house Quidditch team with this matching tee from Harry Potter. Complete with the Hogwart\'s crest over the left-hand side and silver lettering decorating the back, this marvellous tee will look totally patriotic from the towering stands! Official merchandise.', '44448Daddys_Lil_Monster_-_mug-min_280x.webp', '89605product-details-img2.jpg', '96247black-casual-classic-clothes-292999.jpg'),
(134, 'Puma', 515, 221, 870, 'Playing in robes of black and yellow, you can now support your house Quidditch team with this matching tee from Harry Potter. Complete with the Hogwart\'s crest over the left-hand side and silver lettering decorating the back, this marvellous tee will look totally patriotic from the towering stands! Official merchandise.', '49099366.jpg', '33739227.jpg', '3726240.jpg'),
(135, 'Cooper Hogan', 525, 187, 857, 'Playing in robes of black and yellow, you can now support your house Quidditch team with this matching tee from Harry Potter. Complete with the Hogwart\'s crest over the left-hand side and silver lettering decorating the back, this marvellous tee will look totally patriotic from the towering stands! Official merchandise.', '17439BLACK_mug_layout-min_280x.webp', '96278category4.png', '16707fashion-fashionable-footwear-leather-267301.jpg'),
(136, 'Mugs', 870, 112, 867, 'Playing in robes of black and yellow, you can now support your house Quidditch team with this matching tee from Harry Potter. Complete with the Hogwart\'s crest over the left-hand side and silver lettering decorating the back, this marvellous tee will look totally patriotic from the towering stands! Official merchandise.', '13898blur-close-up-depth-of-field-fashion-1478442.jpg', '96405BLACK_mug_layout-min_280x.webp', '63726product10.jpg'),
(137, 'Mugs', 837, 136, 868, 'Playing in robes of black and yellow, you can now support your house Quidditch team with this matching tee from Harry Potter. Complete with the Hogwart\'s crest over the left-hand side and silver lettering decorating the back, this marvellous tee will look totally patriotic from the towering stands! Official merchandise.', '23726536.jpg', '67533close-up-photography-of-blue-earrings-1413420.jpg', '22082product-details-img1.jpg'),
(138, 'Kids Shoes', 876, 141, 854, 'Playing in robes of black and yellow, you can now support your house Quidditch team with this matching tee from Harry Potter. Complete with the Hogwart\'s crest over the left-hand side and silver lettering decorating the back, this marvellous tee will look totally patriotic from the towering stands! Official merchandise.', '53072product14.jpg', '95165product19.jpg', '5996621320028216_280x.webp'),
(139, 'Long- Sleeves Shirts', 987, 139, 871, 'Playing in robes of black and yellow, you can now support your house Quidditch team with this matching tee from Harry Potter. Complete with the Hogwart\'s crest over the left-hand side and silver lettering decorating the back, this marvellous tee will look totally patriotic from the towering stands! Official merchandise.', '85100product-details-img2.jpg', '35092556.jpg', '94667product-12.jpg'),
(140, 'sport & shoes', 790, 284, 865, 'Playing in robes of black and yellow, you can now support your house Quidditch team with this matching tee from Harry Potter. Complete with the Hogwart\'s crest over the left-hand side and silver lettering decorating the back, this marvellous tee will look totally patriotic from the towering stands! Official merchandise.', '1061920320028149_280x.webp', '78478product-10.jpg', '19204product19.jpg'),
(141, 'necklace', 708, 110, 866, 'Playing in robes of black and yellow, you can now support your house Quidditch team with this matching tee from Harry Potter. Complete with the Hogwart\'s crest over the left-hand side and silver lettering decorating the back, this marvellous tee will look totally patriotic from the towering stands! Official merchandise.', '19234closeup-photography-of-clear-jeweled-gold-colored-cluster-1232931.jpg', '83513BLACK_mug_layout-min_280x.webp', '4699021320028216_280x.webp'),
(142, 'Long- Sleeves Shirts', 778, 119, 862, 'Playing in robes of black and yellow, you can now support your house Quidditch team with this matching tee from Harry Potter. Complete with the Hogwart\'s crest over the left-hand side and silver lettering decorating the back, this marvellous tee will look totally patriotic from the towering stands! Official merchandise.', '21774category8.png', '67629category9.png', '34873close-up-photography-of-blue-earrings-1413420.jpg'),
(143, 'Gems', 286, 244, 857, 'Playing in robes of black and yellow, you can now support your house Quidditch team with this matching tee from Harry Potter. Complete with the Hogwart\'s crest over the left-hand side and silver lettering decorating the back, this marvellous tee will look totally patriotic from the towering stands! Official merchandise.', '32395close-up-photo-of-golden-rings-1670723.jpg', '47954product-8.jpg', '3252582017026126_280x.webp'),
(144, 'Puma', 317, 177, 869, 'Playing in robes of black and yellow, you can now support your house Quidditch team with this matching tee from Harry Potter. Complete with the Hogwart\'s crest over the left-hand side and silver lettering decorating the back, this marvellous tee will look totally patriotic from the towering stands! Official merchandise.', '40156product-12.jpg', '82188264.jpg', '8214641.jpg'),
(145, 'Cooper Hogan', 445, 152, 858, 'Playing in robes of black and yellow, you can now support your house Quidditch team with this matching tee from Harry Potter. Complete with the Hogwart\'s crest over the left-hand side and silver lettering decorating the back, this marvellous tee will look totally patriotic from the towering stands! Official merchandise.', '67658131.jpg', '99031product16.jpg', '3129582017026126_280x.webp'),
(146, 'Long- Sleeves Shirts', 585, 255, 869, 'Playing in robes of black and yellow, you can now support your house Quidditch team with this matching tee from Harry Potter. Complete with the Hogwart\'s crest over the left-hand side and silver lettering decorating the back, this marvellous tee will look totally patriotic from the towering stands! Official merchandise.', '10237photo-of-pair-of-vans-sneakers-1598508.jpg', '80582category3.png', '96063product-11.jpg'),
(147, 'T-shirts', 703, 111, 871, 'Playing in robes of black and yellow, you can now support your house Quidditch team with this matching tee from Harry Potter. Complete with the Hogwart\'s crest over the left-hand side and silver lettering decorating the back, this marvellous tee will look totally patriotic from the towering stands! Official merchandise.', '27288product-5.jpg', '8183530.jpg', '7721140.jpg'),
(148, 'Power Ring', 720, 287, 867, 'Playing in robes of black and yellow, you can now support your house Quidditch team with this matching tee from Harry Potter. Complete with the Hogwart\'s crest over the left-hand side and silver lettering decorating the back, this marvellous tee will look totally patriotic from the towering stands! Official merchandise.', '31788close-up-of-wedding-rings-on-floor-17834.jpg', '28128366.jpg', '11938product-15.jpg'),
(149, 'Superman Cup', 297, 186, 860, 'Playing in robes of black and yellow, you can now support your house Quidditch team with this matching tee from Harry Potter. Complete with the Hogwart\'s crest over the left-hand side and silver lettering decorating the back, this marvellous tee will look totally patriotic from the towering stands! Official merchandise.', '48626product-3.jpg', '65017blur-close-up-depth-of-field-fashion-1478442.jpg', '63338product10.jpg'),
(150, 'sport & shoes', 994, 135, 858, 'Playing in robes of black and yellow, you can now support your house Quidditch team with this matching tee from Harry Potter. Complete with the Hogwart\'s crest over the left-hand side and silver lettering decorating the back, this marvellous tee will look totally patriotic from the towering stands! Official merchandise.', '76133product13.jpg', '13346product-12.jpg', '40318Daddys_Lil_Monster_-_mug-min_280x.webp'),
(151, 'Superman Cup', 436, 217, 856, 'Playing in robes of black and yellow, you can now support your house Quidditch team with this matching tee from Harry Potter. Complete with the Hogwart\'s crest over the left-hand side and silver lettering decorating the back, this marvellous tee will look totally patriotic from the towering stands! Official merchandise.', '61409536.jpg', '4386663.jpg', '7887433.jpg'),
(152, 'Mugs', 971, 136, 866, 'Playing in robes of black and yellow, you can now support your house Quidditch team with this matching tee from Harry Potter. Complete with the Hogwart\'s crest over the left-hand side and silver lettering decorating the back, this marvellous tee will look totally patriotic from the towering stands! Official merchandise.', '65203close-up-photo-of-diamond-stud-silver-colored-eternity-ring-691046.jpg', '19026product-12.jpg', '9196130.jpg'),
(154, 'Phoebe Douglas', 78, 977, 863, 'Totam et deserunt veniam, id reprehenderit sequi qui illo quae sit, illum, iste voluptatem. Et proid.', '619giraffes.jpg', '107474insta1490.jpg', '884newimage.jpg');

-- --------------------------------------------------------

--
-- Table structure for table `movies`
--

CREATE TABLE `movies` (
  `movieid` int(11) NOT NULL,
  `moviename` varchar(100) NOT NULL,
  `description` text NOT NULL,
  `coverphoto` text NOT NULL,
  `direction` varchar(200) NOT NULL,
  `productionhouse` varchar(100) NOT NULL,
  `dateofrelease` datetime NOT NULL,
  `genre` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `movies`
--

INSERT INTO `movies` (`movieid`, `moviename`, `description`, `coverphoto`, `direction`, `productionhouse`, `dateofrelease`, `genre`) VALUES
(854, 'Toy Story', 'Lorem ipsum dolor sit amet, consectetur adipisicing elit. Assumenda commodi delectus est fugit itaque magnam placeat, quas reiciendis sapiente sunt tempore, voluptate, voluptates. Facere laudantium minima non perferendis vero. Corporis distinctio magni nulla reiciendis suscipit tempore unde vitae. Ab accusamus ad animi aperiam beatae consequuntur dicta dignissimos dolor dolorem doloremque dolores doloribus dolorum earum esse eum eveniet ex inventore iste iusto maiores minima modi, natus officia optio perspiciatis placeat porro praesentium qui quisquam reiciendis rem sed tempore temporibus totam voluptas!', '199562.4_223250.jpg', ' Jaden Smith', 'Tarang Cine Productions', '1995-08-31 00:00:00', 'Sci-fi & Fantasy'),
(855, ' Jumanji', 'Lorem ipsum dolor sit amet, consectetur adipisicing elit. Assumenda commodi delectus est fugit itaque magnam placeat, quas reiciendis sapiente sunt tempore, voluptate, voluptates. Facere laudantium minima non perferendis vero. Corporis distinctio magni nulla reiciendis suscipit tempore unde vitae. Ab accusamus ad animi aperiam beatae consequuntur dicta dignissimos dolor dolorem doloremque dolores doloribus dolorum earum esse eum eveniet ex inventore iste iusto maiores minima modi, natus officia optio perspiciatis placeat porro praesentium qui quisquam reiciendis rem sed tempore temporibus totam voluptas!', '314792.8_121261.jpg', ' Taylor Lautner', 'Colour Yellow Productions', '1982-06-08 00:00:00', 'Documentary'),
(856, ' Grumpier Old Men', 'Lorem ipsum dolor sit amet, consectetur adipisicing elit. Assumenda commodi delectus est fugit itaque magnam placeat, quas reiciendis sapiente sunt tempore, voluptate, voluptates. Facere laudantium minima non perferendis vero. Corporis distinctio magni nulla reiciendis suscipit tempore unde vitae. Ab accusamus ad animi aperiam beatae consequuntur dicta dignissimos dolor dolorem doloremque dolores doloribus dolorum earum esse eum eveniet ex inventore iste iusto maiores minima modi, natus officia optio perspiciatis placeat porro praesentium qui quisquam reiciendis rem sed tempore temporibus totam voluptas!', '837782.8_116756.jpg', ' Jack Nicholson', 'Qube Cinema Technologies', '1994-09-16 00:00:00', 'comedy'),
(857, ' Waiting to Exhale', 'Lorem ipsum dolor sit amet, consectetur adipisicing elit. Assumenda commodi delectus est fugit itaque magnam placeat, quas reiciendis sapiente sunt tempore, voluptate, voluptates. Facere laudantium minima non perferendis vero. Corporis distinctio magni nulla reiciendis suscipit tempore unde vitae. Ab accusamus ad animi aperiam beatae consequuntur dicta dignissimos dolor dolorem doloremque dolores doloribus dolorum earum esse eum eveniet ex inventore iste iusto maiores minima modi, natus officia optio perspiciatis placeat porro praesentium qui quisquam reiciendis rem sed tempore temporibus totam voluptas!', '998402.8_46213.jpg', ' KVIEW ALL', 'Red Chillies Entertainment', '1968-05-03 00:00:00', 'Sci-fi & Fantasy'),
(858, ' Father of the Bride Part II', 'Lorem ipsum dolor sit amet, consectetur adipisicing elit. Assumenda commodi delectus est fugit itaque magnam placeat, quas reiciendis sapiente sunt tempore, voluptate, voluptates. Facere laudantium minima non perferendis vero. Corporis distinctio magni nulla reiciendis suscipit tempore unde vitae. Ab accusamus ad animi aperiam beatae consequuntur dicta dignissimos dolor dolorem doloremque dolores doloribus dolorum earum esse eum eveniet ex inventore iste iusto maiores minima modi, natus officia optio perspiciatis placeat porro praesentium qui quisquam reiciendis rem sed tempore temporibus totam voluptas!', '223372.7_110629.jpg', ' Will Ferrell', 'CineMan Productions', '2007-02-25 00:00:00', 'action'),
(859, ' Heat', 'Lorem ipsum dolor sit amet, consectetur adipisicing elit. Assumenda commodi delectus est fugit itaque magnam placeat, quas reiciendis sapiente sunt tempore, voluptate, voluptates. Facere laudantium minima non perferendis vero. Corporis distinctio magni nulla reiciendis suscipit tempore unde vitae. Ab accusamus ad animi aperiam beatae consequuntur dicta dignissimos dolor dolorem doloremque dolores doloribus dolorum earum esse eum eveniet ex inventore iste iusto maiores minima modi, natus officia optio perspiciatis placeat porro praesentium qui quisquam reiciendis rem sed tempore temporibus totam voluptas!', '776692.3_82815.jpg', ' Abhishek Bachchan', 'AVM Productions', '2014-10-22 00:00:00', 'Thrillers'),
(860, ' Sabrina', 'Lorem ipsum dolor sit amet, consectetur adipisicing elit. Assumenda commodi delectus est fugit itaque magnam placeat, quas reiciendis sapiente sunt tempore, voluptate, voluptates. Facere laudantium minima non perferendis vero. Corporis distinctio magni nulla reiciendis suscipit tempore unde vitae. Ab accusamus ad animi aperiam beatae consequuntur dicta dignissimos dolor dolorem doloremque dolores doloribus dolorum earum esse eum eveniet ex inventore iste iusto maiores minima modi, natus officia optio perspiciatis placeat porro praesentium qui quisquam reiciendis rem sed tempore temporibus totam voluptas!', '367421.6_245943.jpg', ' Rachel Bilson', 'Grazing Goat Pictures', '1977-01-23 00:00:00', 'horror'),
(861, ' Tom and Huck', 'Lorem ipsum dolor sit amet, consectetur adipisicing elit. Assumenda commodi delectus est fugit itaque magnam placeat, quas reiciendis sapiente sunt tempore, voluptate, voluptates. Facere laudantium minima non perferendis vero. Corporis distinctio magni nulla reiciendis suscipit tempore unde vitae. Ab accusamus ad animi aperiam beatae consequuntur dicta dignissimos dolor dolorem doloremque dolores doloribus dolorum earum esse eum eveniet ex inventore iste iusto maiores minima modi, natus officia optio perspiciatis placeat porro praesentium qui quisquam reiciendis rem sed tempore temporibus totam voluptas!', '949462.8_113449.jpg', ' Vidya Malvade', 'Aamir Khan Productions', '1971-09-05 00:00:00', 'Sports'),
(862, ' Sudden Death', 'Lorem ipsum dolor sit amet, consectetur adipisicing elit. Assumenda commodi delectus est fugit itaque magnam placeat, quas reiciendis sapiente sunt tempore, voluptate, voluptates. Facere laudantium minima non perferendis vero. Corporis distinctio magni nulla reiciendis suscipit tempore unde vitae. Ab accusamus ad animi aperiam beatae consequuntur dicta dignissimos dolor dolorem doloremque dolores doloribus dolorum earum esse eum eveniet ex inventore iste iusto maiores minima modi, natus officia optio perspiciatis placeat porro praesentium qui quisquam reiciendis rem sed tempore temporibus totam voluptas!', '804522.9_77942.jpg', ' AVIEW ALL', 'Bhansali Productions', '1998-02-23 00:00:00', 'Children & Family'),
(863, ' GoldenEye', 'Lorem ipsum dolor sit amet, consectetur adipisicing elit. Assumenda commodi delectus est fugit itaque magnam placeat, quas reiciendis sapiente sunt tempore, voluptate, voluptates. Facere laudantium minima non perferendis vero. Corporis distinctio magni nulla reiciendis suscipit tempore unde vitae. Ab accusamus ad animi aperiam beatae consequuntur dicta dignissimos dolor dolorem doloremque dolores doloribus dolorum earum esse eum eveniet ex inventore iste iusto maiores minima modi, natus officia optio perspiciatis placeat porro praesentium qui quisquam reiciendis rem sed tempore temporibus totam voluptas!', '883352.7_360916.jpg', ' Sam Mendes', 'Kanteerava Studios', '2013-02-22 00:00:00', 'Crime'),
(864, ' The American President', 'Lorem ipsum dolor sit amet, consectetur adipisicing elit. Assumenda commodi delectus est fugit itaque magnam placeat, quas reiciendis sapiente sunt tempore, voluptate, voluptates. Facere laudantium minima non perferendis vero. Corporis distinctio magni nulla reiciendis suscipit tempore unde vitae. Ab accusamus ad animi aperiam beatae consequuntur dicta dignissimos dolor dolorem doloremque dolores doloribus dolorum earum esse eum eveniet ex inventore iste iusto maiores minima modi, natus officia optio perspiciatis placeat porro praesentium qui quisquam reiciendis rem sed tempore temporibus totam voluptas!', '830072.8_120598.jpg', ' Elle Macpherson', 'Felis Creations', '2009-01-12 00:00:00', 'Romantic'),
(865, ' Dracula: Dead and Loving It', 'Lorem ipsum dolor sit amet, consectetur adipisicing elit. Assumenda commodi delectus est fugit itaque magnam placeat, quas reiciendis sapiente sunt tempore, voluptate, voluptates. Facere laudantium minima non perferendis vero. Corporis distinctio magni nulla reiciendis suscipit tempore unde vitae. Ab accusamus ad animi aperiam beatae consequuntur dicta dignissimos dolor dolorem doloremque dolores doloribus dolorum earum esse eum eveniet ex inventore iste iusto maiores minima modi, natus officia optio perspiciatis placeat porro praesentium qui quisquam reiciendis rem sed tempore temporibus totam voluptas!', '344092.9_93300.jpg', ' Salma Hayek', 'Zee Entertainment Enterprises', '1965-06-14 00:00:00', 'comedy'),
(866, ' Balto', 'Lorem ipsum dolor sit amet, consectetur adipisicing elit. Assumenda commodi delectus est fugit itaque magnam placeat, quas reiciendis sapiente sunt tempore, voluptate, voluptates. Facere laudantium minima non perferendis vero. Corporis distinctio magni nulla reiciendis suscipit tempore unde vitae. Ab accusamus ad animi aperiam beatae consequuntur dicta dignissimos dolor dolorem doloremque dolores doloribus dolorum earum esse eum eveniet ex inventore iste iusto maiores minima modi, natus officia optio perspiciatis placeat porro praesentium qui quisquam reiciendis rem sed tempore temporibus totam voluptas!', '542942.2_71198.jpg', ' Aarti Chhabria', 'August Cinema', '1971-01-24 00:00:00', 'Action & Adventure'),
(867, ' Nixon', 'Lorem ipsum dolor sit amet, consectetur adipisicing elit. Assumenda commodi delectus est fugit itaque magnam placeat, quas reiciendis sapiente sunt tempore, voluptate, voluptates. Facere laudantium minima non perferendis vero. Corporis distinctio magni nulla reiciendis suscipit tempore unde vitae. Ab accusamus ad animi aperiam beatae consequuntur dicta dignissimos dolor dolorem doloremque dolores doloribus dolorum earum esse eum eveniet ex inventore iste iusto maiores minima modi, natus officia optio perspiciatis placeat porro praesentium qui quisquam reiciendis rem sed tempore temporibus totam voluptas!', '892912.2_57181.jpg', ' Bebhinn Kelly', 'Sun Pictures', '2000-11-12 00:00:00', 'Romantic'),
(868, ' Cutthroat Island', 'Lorem ipsum dolor sit amet, consectetur adipisicing elit. Assumenda commodi delectus est fugit itaque magnam placeat, quas reiciendis sapiente sunt tempore, voluptate, voluptates. Facere laudantium minima non perferendis vero. Corporis distinctio magni nulla reiciendis suscipit tempore unde vitae. Ab accusamus ad animi aperiam beatae consequuntur dicta dignissimos dolor dolorem doloremque dolores doloribus dolorum earum esse eum eveniet ex inventore iste iusto maiores minima modi, natus officia optio perspiciatis placeat porro praesentium qui quisquam reiciendis rem sed tempore temporibus totam voluptas!', '150162.8_73043.jpg', ' Sacha Jafri', 'Aashirvad Cinemas', '2000-01-28 00:00:00', 'Sci-fi & Fantasy'),
(869, ' Casino', 'Lorem ipsum dolor sit amet, consectetur adipisicing elit. Assumenda commodi delectus est fugit itaque magnam placeat, quas reiciendis sapiente sunt tempore, voluptate, voluptates. Facere laudantium minima non perferendis vero. Corporis distinctio magni nulla reiciendis suscipit tempore unde vitae. Ab accusamus ad animi aperiam beatae consequuntur dicta dignissimos dolor dolorem doloremque dolores doloribus dolorum earum esse eum eveniet ex inventore iste iusto maiores minima modi, natus officia optio perspiciatis placeat porro praesentium qui quisquam reiciendis rem sed tempore temporibus totam voluptas!', '391362.4_299930.jpg', ' Upen Patel', 'Aashirvad Cinemas', '2014-10-27 00:00:00', 'Dramas'),
(870, ' Sense and Sensibility', 'Lorem ipsum dolor sit amet, consectetur adipisicing elit. Assumenda commodi delectus est fugit itaque magnam placeat, quas reiciendis sapiente sunt tempore, voluptate, voluptates. Facere laudantium minima non perferendis vero. Corporis distinctio magni nulla reiciendis suscipit tempore unde vitae. Ab accusamus ad animi aperiam beatae consequuntur dicta dignissimos dolor dolorem doloremque dolores doloribus dolorum earum esse eum eveniet ex inventore iste iusto maiores minima modi, natus officia optio perspiciatis placeat porro praesentium qui quisquam reiciendis rem sed tempore temporibus totam voluptas!', '191632.7_326820.jpg', ' Salma Hayek', 'Navketan Films', '1982-02-06 00:00:00', 'Thrillers'),
(871, ' Four Rooms', 'Lorem ipsum dolor sit amet, consectetur adipisicing elit. Assumenda commodi delectus est fugit itaque magnam placeat, quas reiciendis sapiente sunt tempore, voluptate, voluptates. Facere laudantium minima non perferendis vero. Corporis distinctio magni nulla reiciendis suscipit tempore unde vitae. Ab accusamus ad animi aperiam beatae consequuntur dicta dignissimos dolor dolorem doloremque dolores doloribus dolorum earum esse eum eveniet ex inventore iste iusto maiores minima modi, natus officia optio perspiciatis placeat porro praesentium qui quisquam reiciendis rem sed tempore temporibus totam voluptas!', '172582.4_185183.jpg', ' Yash Chopra', 'Anurag Kashyap Films', '1992-05-16 00:00:00', 'Documentary'),
(872, ' Ace Ventura: When Nature Calls', 'Lorem ipsum dolor sit amet, consectetur adipisicing elit. Assumenda commodi delectus est fugit itaque magnam placeat, quas reiciendis sapiente sunt tempore, voluptate, voluptates. Facere laudantium minima non perferendis vero. Corporis distinctio magni nulla reiciendis suscipit tempore unde vitae. Ab accusamus ad animi aperiam beatae consequuntur dicta dignissimos dolor dolorem doloremque dolores doloribus dolorum earum esse eum eveniet ex inventore iste iusto maiores minima modi, natus officia optio perspiciatis placeat porro praesentium qui quisquam reiciendis rem sed tempore temporibus totam voluptas!', '937162.1_81693.jpg', ' Lars Narfeldt', 'UTV Motion Pictures', '2011-09-23 00:00:00', 'Romantic'),
(873, ' Money Train', 'Lorem ipsum dolor sit amet, consectetur adipisicing elit. Assumenda commodi delectus est fugit itaque magnam placeat, quas reiciendis sapiente sunt tempore, voluptate, voluptates. Facere laudantium minima non perferendis vero. Corporis distinctio magni nulla reiciendis suscipit tempore unde vitae. Ab accusamus ad animi aperiam beatae consequuntur dicta dignissimos dolor dolorem doloremque dolores doloribus dolorum earum esse eum eveniet ex inventore iste iusto maiores minima modi, natus officia optio perspiciatis placeat porro praesentium qui quisquam reiciendis rem sed tempore temporibus totam voluptas!', '572882.1_68291.jpg', ' Hansika Motwani', 'Mowgli Productions', '1976-05-25 00:00:00', 'Sports');

-- --------------------------------------------------------

--
-- Table structure for table `seating`
--

CREATE TABLE `seating` (
  `id` int(11) NOT NULL,
  `seatnumber` int(11) NOT NULL,
  `price` float NOT NULL,
  `auditoriumname` varchar(200) NOT NULL,
  `theatreid` int(11) NOT NULL,
  `auditoriumkey` varchar(200) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `shows`
--

CREATE TABLE `shows` (
  `id` int(11) NOT NULL,
  `showdate` date NOT NULL,
  `movieid` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `shows`
--

INSERT INTO `shows` (`id`, `showdate`, `movieid`) VALUES
(7, '2020-05-10', 857),
(9, '2020-05-08', 862),
(11, '2020-05-05', 855),
(12, '2020-05-08', 860),
(13, '2020-05-05', 871),
(14, '2020-05-07', 871);

-- --------------------------------------------------------

--
-- Table structure for table `showtimings`
--

CREATE TABLE `showtimings` (
  `id` int(11) NOT NULL,
  `audi` varchar(20) NOT NULL,
  `price` int(11) NOT NULL,
  `showtime` time NOT NULL,
  `showid` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `showtimings`
--

INSERT INTO `showtimings` (`id`, `audi`, `price`, `showtime`, `showid`) VALUES
(1, 'Audi-1', 200, '05:09:00', 7),
(7, 'Audi-2', 990, '02:59:00', 7),
(8, 'Audi-1', 200, '13:59:00', 9),
(10, 'Audi-2', 400, '23:00:00', 9),
(11, 'Audi-1', 900, '13:59:00', 11),
(13, 'Audi-2', 100, '11:58:00', 13),
(15, 'Audi-2', 100, '13:58:00', 14),
(16, 'Audi-1', 300, '12:59:00', 14);

-- --------------------------------------------------------

--
-- Table structure for table `theatres`
--

CREATE TABLE `theatres` (
  `theatreid` int(11) NOT NULL,
  `city` varchar(200) NOT NULL,
  `location` text NOT NULL,
  `description` text NOT NULL,
  `coverphoto` text NOT NULL,
  `password` varchar(50) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `theatres`
--

INSERT INTO `theatres` (`theatreid`, `city`, `location`, `description`, `coverphoto`, `password`) VALUES
(1, 'Culpa consequatur ', 'Soluta itaque sint d', 'Iste natus quis duis sint expedita ut sit impedit, voluptate omnis quo aute aut eius velit non dolor.', '713insta14486.jpg', 'thth'),
(4, ' Imphal', '134 12TH STREET SE', 'Check out movie ticket rates and show timings at Cinepolis: Celebration Mall, Amritsar. Book tickets online for latest movies near you in Amritsar on BookMyShow. ... material, in the manner complained of as reported by me, is not authorized by the copyright owner, its agent, or the law.', '424497.0_68853.jpg', 'password'),
(5, ' West Bengal', '1746 LANIER PLACE NW', 'Check out movie ticket rates and show timings at Cinepolis: Celebration Mall, Amritsar. Book tickets online for latest movies near you in Amritsar on BookMyShow. ... material, in the manner complained of as reported by me, is not authorized by the copyright owner, its agent, or the law.', '191315.7_86998.jpg', 'password'),
(6, ' Hazaribag', '1710 H STREET NW', 'Check out movie ticket rates and show timings at Cinepolis: Celebration Mall, Amritsar. Book tickets online for latest movies near you in Amritsar on BookMyShow. ... material, in the manner complained of as reported by me, is not authorized by the copyright owner, its agent, or the law.', '962708.2_118715.jpg', 'password'),
(7, ' Sangli', '1615 RHODE ISLAND AVENUE NW', 'Check out movie ticket rates and show timings at Cinepolis: Celebration Mall, Amritsar. Book tickets online for latest movies near you in Amritsar on BookMyShow. ... material, in the manner complained of as reported by me, is not authorized by the copyright owner, its agent, or the law.', '507886.9_73747.jpg', 'password'),
(8, ' Darjiling', '1121 NEW HAMPSHIRE AVENUE NW', 'Check out movie ticket rates and show timings at Cinepolis: Celebration Mall, Amritsar. Book tickets online for latest movies near you in Amritsar on BookMyShow. ... material, in the manner complained of as reported by me, is not authorized by the copyright owner, its agent, or the law.', '125998.8_113147.jpg', 'password'),
(9, ' Shrirampur', '733 15TH STREET NW', 'Check out movie ticket rates and show timings at Cinepolis: Celebration Mall, Amritsar. Book tickets online for latest movies near you in Amritsar on BookMyShow. ... material, in the manner complained of as reported by me, is not authorized by the copyright owner, its agent, or the law.', '189757.0_89791.jpg', 'password'),
(10, ' Ghaziabad', '1615 NEW YORK AVENUE NE', 'Check out movie ticket rates and show timings at Cinepolis: Celebration Mall, Amritsar. Book tickets online for latest movies near you in Amritsar on BookMyShow. ... material, in the manner complained of as reported by me, is not authorized by the copyright owner, its agent, or the law.', '568935.9_99371.jpg', 'password'),
(11, ' Shahdol', '1050 31ST STREET NW', 'Check out movie ticket rates and show timings at Cinepolis: Celebration Mall, Amritsar. Book tickets online for latest movies near you in Amritsar on BookMyShow. ... material, in the manner complained of as reported by me, is not authorized by the copyright owner, its agent, or the law.', '434238.3_55630.jpg', 'password'),
(12, ' Kathua', '1001 16TH STREET NW', 'Check out movie ticket rates and show timings at Cinepolis: Celebration Mall, Amritsar. Book tickets online for latest movies near you in Amritsar on BookMyShow. ... material, in the manner complained of as reported by me, is not authorized by the copyright owner, its agent, or the law.', '336725.8_71216.jpg', 'password'),
(13, ' Giridih', '480 L\'ENFANT PLAZA SW', 'Check out movie ticket rates and show timings at Cinepolis: Celebration Mall, Amritsar. Book tickets online for latest movies near you in Amritsar on BookMyShow. ... material, in the manner complained of as reported by me, is not authorized by the copyright owner, its agent, or the law.', '494525.5_99165.jpg', 'password'),
(14, ' Aurangabad', '301 I STREET NW', 'Check out movie ticket rates and show timings at Cinepolis: Celebration Mall, Amritsar. Book tickets online for latest movies near you in Amritsar on BookMyShow. ... material, in the manner complained of as reported by me, is not authorized by the copyright owner, its agent, or the law.', '721366.0_103060.jpg', 'password'),
(15, ' Ajmer', '2224 F STREET NW', 'Check out movie ticket rates and show timings at Cinepolis: Celebration Mall, Amritsar. Book tickets online for latest movies near you in Amritsar on BookMyShow. ... material, in the manner complained of as reported by me, is not authorized by the copyright owner, its agent, or the law.', '438784.8_80861.jpg', 'password'),
(16, ' Moradabad', '2005 COLUMBIA ROAD NW', 'Check out movie ticket rates and show timings at Cinepolis: Celebration Mall, Amritsar. Book tickets online for latest movies near you in Amritsar on BookMyShow. ... material, in the manner complained of as reported by me, is not authorized by the copyright owner, its agent, or the law.', '567087.7_120802.jpg', 'password'),
(17, ' Kalyan', '1207 KENYON STREET NW', 'Check out movie ticket rates and show timings at Cinepolis: Celebration Mall, Amritsar. Book tickets online for latest movies near you in Amritsar on BookMyShow. ... material, in the manner complained of as reported by me, is not authorized by the copyright owner, its agent, or the law.', '535076.5_102900.jpg', 'password'),
(18, ' Buxar', '2500 PENNSYLVANIA AVENUE NW', 'Check out movie ticket rates and show timings at Cinepolis: Celebration Mall, Amritsar. Book tickets online for latest movies near you in Amritsar on BookMyShow. ... material, in the manner complained of as reported by me, is not authorized by the copyright owner, its agent, or the law.', '363345.7_287364.jpg', 'password'),
(19, ' Bundi', '200 C STREET SE', 'Check out movie ticket rates and show timings at Cinepolis: Celebration Mall, Amritsar. Book tickets online for latest movies near you in Amritsar on BookMyShow. ... material, in the manner complained of as reported by me, is not authorized by the copyright owner, its agent, or the law.', '940155.5_134619.jpg', 'password'),
(20, ' Ganganagar', '10 I STREET SW', 'Check out movie ticket rates and show timings at Cinepolis: Celebration Mall, Amritsar. Book tickets online for latest movies near you in Amritsar on BookMyShow. ... material, in the manner complained of as reported by me, is not authorized by the copyright owner, its agent, or the law.', '203317.0_98067.jpg', 'password'),
(21, ' Dharmapuri', '1731 NEW HAMPSHIRE AVENUE NW', 'Check out movie ticket rates and show timings at Cinepolis: Celebration Mall, Amritsar. Book tickets online for latest movies near you in Amritsar on BookMyShow. ... material, in the manner complained of as reported by me, is not authorized by the copyright owner, its agent, or the law.', '519867.8_40416.jpg', 'password');

-- --------------------------------------------------------

--
-- Table structure for table `ticketsbooked`
--

CREATE TABLE `ticketsbooked` (
  `ticketid` int(11) NOT NULL,
  `dateofbooking` datetime NOT NULL,
  `numberofticket` int(11) NOT NULL,
  `showid` int(11) NOT NULL,
  `theatreid` int(11) NOT NULL,
  `audinumber` int(11) NOT NULL,
  `totalprice` float NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `ticket_category`
--

CREATE TABLE `ticket_category` (
  `id` int(11) NOT NULL,
  `categoryname` varchar(100) NOT NULL,
  `price` float NOT NULL,
  `threatreid` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `ticket_category`
--

INSERT INTO `ticket_category` (`id`, `categoryname`, `price`, `threatreid`) VALUES
(1, 'Gold VIP Pass', 959, 1),
(3, 'Ground hall', 800, 1),
(13, 'Balcony', 100, 1),
(14, 'Basic', 300, 1),
(20, 'Balcony', 50, 4),
(21, 'preimium', 106, 4),
(22, 'Middle Hall', 281, 5),
(23, 'Balcony', 58, 4),
(26, 'Balcony', 506, 5),
(27, 'Ground hall', 121, 5),
(28, 'Middle Hall', 314, 5),
(29, 'Balcony', 507, 6),
(30, 'Ground hall', 146, 6),
(31, 'Middle Hall', 394, 6),
(32, 'Balcony', 511, 7),
(33, 'Ground hall', 129, 7),
(34, 'Middle Hall', 319, 7),
(35, 'Balcony', 412, 8),
(36, 'Ground hall', 152, 8),
(37, 'Middle Hall', 311, 8),
(38, 'Balcony', 584, 9),
(39, 'Ground hall', 194, 9),
(40, 'Middle Hall', 398, 9),
(41, 'Balcony', 575, 10),
(42, 'Ground hall', 223, 10),
(43, 'Middle Hall', 295, 10),
(44, 'Balcony', 500, 11),
(45, 'Ground hall', 171, 11),
(46, 'Middle Hall', 265, 11),
(47, 'Balcony', 422, 12),
(48, 'Ground hall', 155, 12),
(49, 'Middle Hall', 395, 12),
(50, 'Balcony', 539, 13),
(51, 'Ground hall', 203, 13),
(52, 'Middle Hall', 350, 13),
(53, 'Balcony', 515, 14),
(54, 'Ground hall', 140, 14),
(55, 'Middle Hall', 302, 14),
(56, 'Balcony', 548, 15),
(57, 'Ground hall', 187, 15),
(58, 'Middle Hall', 363, 15),
(59, 'Balcony', 560, 16),
(60, 'Ground hall', 203, 16),
(61, 'Middle Hall', 262, 16),
(62, 'Balcony', 503, 17),
(63, 'Ground hall', 242, 17),
(64, 'Middle Hall', 268, 17),
(65, 'Balcony', 520, 18),
(66, 'Ground hall', 159, 18),
(67, 'Middle Hall', 385, 18),
(68, 'Balcony', 579, 19),
(69, 'Ground hall', 140, 19),
(70, 'Middle Hall', 299, 19),
(71, 'Balcony', 483, 20),
(72, 'Ground hall', 124, 20),
(73, 'Middle Hall', 288, 20),
(74, 'Balcony', 415, 21),
(75, 'Ground hall', 138, 21),
(76, 'Middle Hall', 391, 21),
(77, 'rkd', 122, 4);

--
-- Indexes for dumped tables
--

--
-- Indexes for table `admin`
--
ALTER TABLE `admin`
  ADD PRIMARY KEY (`email`);

--
-- Indexes for table `bill`
--
ALTER TABLE `bill`
  ADD PRIMARY KEY (`billID`),
  ADD KEY `email` (`email`);

--
-- Indexes for table `billdetail`
--
ALTER TABLE `billdetail`
  ADD PRIMARY KEY (`billdetailid`),
  ADD KEY `billid` (`billid`),
  ADD KEY `productid` (`merchandise`);

--
-- Indexes for table `booking`
--
ALTER TABLE `booking`
  ADD PRIMARY KEY (`id`),
  ADD KEY `showtimeid` (`showtimeid`);

--
-- Indexes for table `customers`
--
ALTER TABLE `customers`
  ADD PRIMARY KEY (`email`);

--
-- Indexes for table `merchandise`
--
ALTER TABLE `merchandise`
  ADD PRIMARY KEY (`productid`),
  ADD KEY `movieid` (`movieid`);

--
-- Indexes for table `movies`
--
ALTER TABLE `movies`
  ADD PRIMARY KEY (`movieid`);

--
-- Indexes for table `seating`
--
ALTER TABLE `seating`
  ADD PRIMARY KEY (`id`),
  ADD KEY `theatreid` (`theatreid`);

--
-- Indexes for table `shows`
--
ALTER TABLE `shows`
  ADD PRIMARY KEY (`id`),
  ADD KEY `movieid` (`movieid`);

--
-- Indexes for table `showtimings`
--
ALTER TABLE `showtimings`
  ADD PRIMARY KEY (`id`),
  ADD KEY `showid` (`showid`);

--
-- Indexes for table `theatres`
--
ALTER TABLE `theatres`
  ADD PRIMARY KEY (`theatreid`);

--
-- Indexes for table `ticketsbooked`
--
ALTER TABLE `ticketsbooked`
  ADD PRIMARY KEY (`ticketid`),
  ADD KEY `theatreid` (`theatreid`);

--
-- Indexes for table `ticket_category`
--
ALTER TABLE `ticket_category`
  ADD PRIMARY KEY (`id`),
  ADD KEY `threatreid` (`threatreid`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `bill`
--
ALTER TABLE `bill`
  MODIFY `billID` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=31;

--
-- AUTO_INCREMENT for table `billdetail`
--
ALTER TABLE `billdetail`
  MODIFY `billdetailid` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=41;

--
-- AUTO_INCREMENT for table `booking`
--
ALTER TABLE `booking`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=12;

--
-- AUTO_INCREMENT for table `merchandise`
--
ALTER TABLE `merchandise`
  MODIFY `productid` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=155;

--
-- AUTO_INCREMENT for table `movies`
--
ALTER TABLE `movies`
  MODIFY `movieid` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=875;

--
-- AUTO_INCREMENT for table `seating`
--
ALTER TABLE `seating`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `shows`
--
ALTER TABLE `shows`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=15;

--
-- AUTO_INCREMENT for table `showtimings`
--
ALTER TABLE `showtimings`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=17;

--
-- AUTO_INCREMENT for table `theatres`
--
ALTER TABLE `theatres`
  MODIFY `theatreid` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=173;

--
-- AUTO_INCREMENT for table `ticketsbooked`
--
ALTER TABLE `ticketsbooked`
  MODIFY `ticketid` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `ticket_category`
--
ALTER TABLE `ticket_category`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=78;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `bill`
--
ALTER TABLE `bill`
  ADD CONSTRAINT `bill_ibfk_1` FOREIGN KEY (`email`) REFERENCES `customers` (`email`);

--
-- Constraints for table `billdetail`
--
ALTER TABLE `billdetail`
  ADD CONSTRAINT `billdetail_ibfk_1` FOREIGN KEY (`merchandise`) REFERENCES `merchandise` (`productid`),
  ADD CONSTRAINT `billdetail_ibfk_2` FOREIGN KEY (`billid`) REFERENCES `bill` (`billID`);

--
-- Constraints for table `booking`
--
ALTER TABLE `booking`
  ADD CONSTRAINT `booking_ibfk_1` FOREIGN KEY (`showtimeid`) REFERENCES `showtimings` (`id`);

--
-- Constraints for table `merchandise`
--
ALTER TABLE `merchandise`
  ADD CONSTRAINT `merchandise_ibfk_1` FOREIGN KEY (`movieid`) REFERENCES `movies` (`movieid`);

--
-- Constraints for table `seating`
--
ALTER TABLE `seating`
  ADD CONSTRAINT `seating_ibfk_1` FOREIGN KEY (`theatreid`) REFERENCES `theatres` (`theatreid`);

--
-- Constraints for table `shows`
--
ALTER TABLE `shows`
  ADD CONSTRAINT `shows_ibfk_1` FOREIGN KEY (`movieid`) REFERENCES `movies` (`movieid`);

--
-- Constraints for table `showtimings`
--
ALTER TABLE `showtimings`
  ADD CONSTRAINT `showtimings_ibfk_1` FOREIGN KEY (`showid`) REFERENCES `shows` (`id`);

--
-- Constraints for table `ticketsbooked`
--
ALTER TABLE `ticketsbooked`
  ADD CONSTRAINT `ticketsbooked_ibfk_1` FOREIGN KEY (`theatreid`) REFERENCES `theatres` (`theatreid`);

--
-- Constraints for table `ticket_category`
--
ALTER TABLE `ticket_category`
  ADD CONSTRAINT `ticket_category_ibfk_1` FOREIGN KEY (`threatreid`) REFERENCES `theatres` (`theatreid`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
