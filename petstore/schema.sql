CREATE TABLE IF NOT EXISTS categories (
  category_id integer PRIMARY KEY AUTOINCREMENT NOT NULL,
  name char(128) NOT NULL
);
CREATE TABLE IF NOT EXISTS pets (
  pet_id integer PRIMARY KEY AUTOINCREMENT NOT NULL,
  category_id integer NOT NULL,
  status integer(1) NOT NULL,
  name char(128) NOT NULL
);
CREATE TABLE IF NOT EXISTS pet_photos (
  pet_image_id integer PRIMARY KEY AUTOINCREMENT NOT NULL,
  pet_id integer NOT NULL,
  name char(128),
  url char(128) NOT NULL
);

CREATE TABLE IF NOT EXISTS customers (
  customer_id integer PRIMARY KEY AUTOINCREMENT NOT NULL,
  first_name char(128) NOT NULL,
  last_name char(128) NOT NULL,
  email char(128) NOT NULL,
  status integer NOT NULL DEFAULT(0)
);
CREATE TABLE IF NOT EXISTS orders (
  order_id integer PRIMARY KEY AUTOINCREMENT NOT NULL,
  customer_id integer NOT NULL,
  pet_id integer NOT NULL,
  status integer NOT NULL DEFAULT(0)
);
