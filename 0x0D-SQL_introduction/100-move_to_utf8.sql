-- Converts hbtn_0c_0 to UTF8, converting;
-- Database `hbtn_0c_0
-- Table `first_table`
-- Field `name` in `first_table`
USE `hbtn_0c_0`
ALTER TABLE `first_table`
CONVERT TO CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
