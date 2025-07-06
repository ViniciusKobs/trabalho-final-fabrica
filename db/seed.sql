USE market;

-- Insert brands
INSERT INTO brands (name, description, image) VALUES
('Nestle', 'Global food and drink company', 'nestle_logo.png'),
('Coca-Cola', 'Beverage company', 'coke_logo.png'),
('Kelloggs', 'Breakfast cereals and snacks', 'kelloggs_logo.png'),
('PepsiCo', 'Food and beverage corporation', 'pepsi_logo.png'),
('Kraft Heinz', 'Food processing company', 'kraft_logo.png');

-- Insert categories
INSERT INTO categories (name, description) VALUES
('Beverages', 'Drinks and liquid refreshments'),
('Snacks', 'Quick food items and treats'),
('Breakfast', 'Morning meal products'),
('Condiments', 'Sauces and food enhancers'),
('Dairy', 'Milk-based products');

-- Insert products
INSERT INTO products (brand_id, name, description, image, weight, volume, units, length) VALUES
(1, 'Nescafe Classic', 'Instant coffee', 'nescafe.png', 200, NULL, NULL, NULL),
(1, 'Nesquik Chocolate', 'Chocolate milk powder', 'nesquik.png', 500, NULL, NULL, NULL),
(2, 'Coca-Cola Classic', 'Carbonated soft drink', 'coke.png', NULL, 330, NULL, NULL),
(2, 'Sprite', 'Lemon-lime soda', 'sprite.png', NULL, 500, NULL, NULL),
(3, 'Corn Flakes', 'Breakfast cereal', 'cornflakes.png', 500, NULL, NULL, NULL),
(3, 'Rice Krispies', 'Rice cereal', 'krispies.png', 375, NULL, NULL, NULL),
(4, 'Lay''s Classic', 'Potato chips', 'lays.png', 200, NULL, NULL, NULL),
(4, 'Doritos Nacho Cheese', 'Tortilla chips', 'doritos.png', 150, NULL, NULL, NULL),
(5, 'Heinz Ketchup', 'Tomato ketchup', 'ketchup.png', NULL, 500, NULL, NULL),
(5, 'Kraft Mac & Cheese', 'Macaroni and cheese', 'mac.png', 400, NULL, NULL, NULL);

-- Link products to categories
INSERT INTO products_categories (product_id, category_id) VALUES
(1, 1), -- Nescafe in Beverages
(2, 1), -- Nesquik in Beverages
(3, 1), -- Coca-Cola in Beverages
(4, 1), -- Sprite in Beverages
(5, 3), -- Corn Flakes in Breakfast
(6, 3), -- Rice Krispies in Breakfast
(7, 2), -- Lay's in Snacks
(8, 2), -- Doritos in Snacks
(9, 4), -- Ketchup in Condiments
(10, 3); -- Mac & Cheese in Breakfast

-- Link brands to categories
INSERT INTO brands_categories (brand_id, category_id) VALUES
(1, 1), -- Nestle in Beverages
(1, 3), -- Nestle in Breakfast
(2, 1), -- Coca-Cola in Beverages
(3, 3), -- Kelloggs in Breakfast
(3, 2), -- Kelloggs in Snacks
(4, 1), -- PepsiCo in Beverages
(4, 2), -- PepsiCo in Snacks
(5, 4); -- Kraft Heinz in Condiments

-- Insert markets
INSERT INTO markets (name) VALUES
('Walmart'),
('Carrefour'),
('Tesco'),
('Aldi'),
('Costco');

-- Insert pricing (with realistic prices)
INSERT INTO pricing (product_id, market_id, price) VALUES
(1, 1, 5.99),  -- Nescafe at Walmart
(1, 2, 6.49),  -- Nescafe at Carrefour
(2, 1, 4.99),  -- Nesquik at Walmart
(2, 3, 5.29),  -- Nesquik at Tesco
(3, 1, 1.99),  -- Coca-Cola at Walmart
(3, 2, 2.19),  -- Coca-Cola at Carrefour
(4, 1, 1.79),  -- Sprite at Walmart
(4, 4, 1.69),  -- Sprite at Aldi
(5, 1, 3.99),  -- Corn Flakes at Walmart
(5, 5, 3.49),  -- Corn Flakes at Costco
(6, 1, 4.29),  -- Rice Krispies at Walmart
(6, 3, 4.49),  -- Rice Krispies at Tesco
(7, 1, 3.49),  -- Lay's at Walmart
(7, 2, 3.99),  -- Lay's at Carrefour
(8, 1, 3.99),  -- Doritos at Walmart
(8, 4, 3.79),  -- Doritos at Aldi
(9, 1, 2.99),  -- Ketchup at Walmart
(9, 5, 2.49),  -- Ketchup at Costco
(10, 1, 1.99), -- Mac & Cheese at Walmart
(10, 3, 2.29); -- Mac & Cheese at Tesco