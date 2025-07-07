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

-- Add more pricing entries
INSERT INTO pricing (product_id, market_id, price) VALUES
-- Nescafe Classic (already in Walmart, Carrefour)
(1, 3, 6.29),  -- Nescafe at Tesco
(1, 4, 5.79),  -- Nescafe at Aldi
(1, 5, 5.49),  -- Nescafe at Costco

-- Nesquik Chocolate (already in Walmart, Tesco)
(2, 2, 5.19),  -- Nesquik at Carrefour
(2, 4, 4.89),  -- Nesquik at Aldi
(2, 5, 4.49),  -- Nesquik at Costco

-- Coca-Cola Classic (already in Walmart, Carrefour)
(3, 3, 2.09),  -- Coca-Cola at Tesco
(3, 4, 1.89),  -- Coca-Cola at Aldi
(3, 5, 1.79),  -- Coca-Cola at Costco

-- Sprite (already in Walmart, Aldi)
(4, 2, 1.89),  -- Sprite at Carrefour
(4, 3, 1.99),  -- Sprite at Tesco
(4, 5, 1.59),  -- Sprite at Costco

-- Corn Flakes (already in Walmart, Costco)
(5, 2, 4.19),  -- Corn Flakes at Carrefour
(5, 3, 4.09),  -- Corn Flakes at Tesco
(5, 4, 3.79),  -- Corn Flakes at Aldi

-- Rice Krispies (already in Walmart, Tesco)
(6, 2, 4.39),  -- Rice Krispies at Carrefour
(6, 4, 4.19),  -- Rice Krispies at Aldi
(6, 5, 3.99),  -- Rice Krispies at Costco

-- Lay's Classic (already in Walmart, Carrefour)
(7, 3, 3.89),  -- Lay's at Tesco
(7, 4, 3.29),  -- Lay's at Aldi
(7, 5, 3.19),  -- Lay's at Costco

-- Doritos (already in Walmart, Aldi)
(8, 2, 3.89),  -- Doritos at Carrefour
(8, 3, 3.99),  -- Doritos at Tesco
(8, 5, 3.49),  -- Doritos at Costco

-- Heinz Ketchup (already in Walmart, Costco)
(9, 2, 3.19),  -- Ketchup at Carrefour
(9, 3, 2.89),  -- Ketchup at Tesco
(9, 4, 2.79),  -- Ketchup at Aldi

-- Mac & Cheese (already in Walmart, Tesco)
(10, 2, 2.19), -- Mac & Cheese at Carrefour
(10, 4, 1.89), -- Mac & Cheese at Aldi
(10, 5, 1.79); -- Mac & Cheese at Costco