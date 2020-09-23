-- phpMyAdmin SQL Dump
-- version 5.0.2
-- https://www.phpmyadmin.net/
--
-- 主機： 127.0.0.1
-- 產生時間： 2020-09-16 07:32:59
-- 伺服器版本： 8.0.20
-- PHP 版本： 7.3.19

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- 資料庫： `food`
--

-- --------------------------------------------------------

--
-- 資料表結構 `food_item_table`
--

CREATE TABLE `food_item_table` (
  `id` int NOT NULL,
  `food_item` varchar(255) NOT NULL,
  `weight(g)` int NOT NULL,
  `calorie(Kcal)` float NOT NULL,
  `fat(g)` float NOT NULL,
  `carbohydrate(g)` float NOT NULL,
  `protein(g)` float NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- 傾印資料表的資料 `food_item_table`
--

INSERT INTO `food_item_table` (`id`, `food_item`, `weight(g)`, `calorie(Kcal)`, `fat(g)`, `carbohydrate(g)`, `protein(g)`) VALUES
(1, 'carrot_eggs', 100, 77.5, 4.88, 4.71, 3.88),
(2, 'chicken_nuggets', 100, 297, 18.82, 16.32, 15.59),
(3, 'chinese_cabbage', 100, 24, 0.12, 5.58, 1.44),
(4, 'curry', 100, 427, 23.1, 50.62, 9.38),
(5, 'fried_chicken', 100, 297, 18.82, 16.32, 15.59),
(6, 'fried_dumplings', 100, 256, 9.98, 25.01, 15.18),
(7, 'fried_eggs', 100, 146, 9.9, 0.76, 12.52),
(8, 'mung_bean_sprouts', 100, 63, 3.14, 6.87, 3.18),
(9, 'rice', 100, 130, 0.21, 28.59, 2.38),
(10, 'triangle_hash_brown', 100, 308, 17.86, 32.21, 4.67),
(11, 'chinese_sausage', 100, 269, 21, 8, 12.5),
(12, 'water_spinach', 100, 23, 0.39, 3.63, 2.86),
(13, 'stir-fried_broccoli', 100, 66, 4.4, 5.91, 2.27),
(14, 'stir-fried_bitter_gourd', 100, 17, 0.17, 3.7, 1),
(15, 'seaweed', 100, 38, 0.26, 8.43, 2.38),
(16, 'braised_pork_ribs', 100, 255, 19.58, 3.63, 15.52),
(17, 'fried_chicken_steak', 100, 235, 11.24, 16.9, 15.65),
(18, 'chicken_leg', 100, 161, 8.68, 0, 19.27)
(19, 'braised_egg', 100, 132, 8.16, 2.19, 12.1),
(20, 'braised_pork_belly', 100, 431, 42.73, 4.3, 7.31);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
