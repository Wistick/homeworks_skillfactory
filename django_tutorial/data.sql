CREATE TABLE PRODUCTS (
    product_id INT AUTO_INCREMENT NOT NULL,
    name CHAR(255) NOT NULL,
    price FLOAT NOT NULL,

    PRIMARY KEY (product_id)
);

CREATE TABLE STAFF (
    staff_id INT AUTO_INCREMENT NOT NULL
    full_name CHAR(255) NOT NULL
    position CHAR(255) NOT NULL
    labor_contract INT NOT NULL

    PRIMARY KEY (staff_id)
);

CREATE TABLE ORDERS (
    order_id INT AUTO_INCREMENT NOT NULL,
    time_in DATETIME NOT NULL,
    time_out DATETIME,
    cost FLOAT NOT NULL,
    take_away INT NOT NULL,
    staff INT NOT NULL,

    PRIMARY KEY (order_id),
    FOREIGN KEY (staff) REFERENCES STAFF (staff_id)
);

CREATE TABLE PRODUCTS_ORDERS (
    product_order_id INT AUTO_INCREMENT NOT NULL,
    product INT NOT NULL,
    in_order INT NOT NULL,
    amount INT NOT NULL,

    PRIMARY KEY (product_order_id)
    FOREIGN KEY (product) REFERENCES PRODUCTS (product_id),
    FOREIGN KEY (in_order) REFERENCES ORDERS (order_id),
);

--При помощи SQL создайте таблицу PRODUCTS_ORDERS, которая должна:
--
--Содержать атрибут product_order_id, который предполагается целочисленным, автоматически увеличивающимся
--на 1 и тем самым должен стать первичным ключом этой таблицы.

--Содержать атрибут product, который ссылается на первичный ключ таблицы Products.
--Содержать атрибут in_order, который ссылается на первичный ключ таблицы Orders.
--Содержать атрибут amount, который определяет количество конкретного продукта в заказе. Мы предполагаем, что это целое число.
