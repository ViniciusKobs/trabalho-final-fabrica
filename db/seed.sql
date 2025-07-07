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
-- First, clear existing pricing data
DELETE FROM pricing;

-- Insert new shuffled pricing data where each product is cheapest at a different market
INSERT INTO pricing (product_id, market_id, price) VALUES
-- Nescafe (cheapest at Costco)
(1, 1, 6.29),  -- Walmart
(1, 2, 6.49),  -- Carrefour
(1, 3, 6.19),  -- Tesco
(1, 4, 5.99),  -- Aldi
(1, 5, 5.49),  -- Costco

-- Nesquik (cheapest at Walmart)
(2, 1, 4.49),  -- Walmart
(2, 2, 5.19),  -- Carrefour
(2, 3, 5.29),  -- Tesco
(2, 4, 4.89),  -- Aldi
(2, 5, 4.99),  -- Costco

-- Coca-Cola (cheapest at Aldi)
(3, 1, 2.19),  -- Walmart
(3, 2, 2.29),  -- Carrefour
(3, 3, 2.09),  -- Tesco
(3, 4, 1.79),  -- Aldi
(3, 5, 1.99),  -- Costco

-- Sprite (cheapest at Carrefour)
(4, 1, 1.89),  -- Walmart
(4, 2, 1.59),  -- Carrefour
(4, 3, 1.99),  -- Tesco
(4, 4, 1.79),  -- Aldi
(4, 5, 1.89),  -- Costco

-- Corn Flakes (cheapest at Tesco)
(5, 1, 4.19),  -- Walmart
(5, 2, 4.29),  -- Carrefour
(5, 3, 3.49),  -- Tesco
(5, 4, 3.99),  -- Aldi
(5, 5, 3.89),  -- Costco

-- Rice Krispies (cheapest at Aldi)
(6, 1, 4.29),  -- Walmart
(6, 2, 4.39),  -- Carrefour
(6, 3, 4.49),  -- Tesco
(6, 4, 3.89),  -- Aldi
(6, 5, 4.19),  -- Costco

-- Lay's (cheapest at Walmart)
(7, 1, 3.19),  -- Walmart
(7, 2, 3.99),  -- Carrefour
(7, 3, 3.89),  -- Tesco
(7, 4, 3.49),  -- Aldi
(7, 5, 3.59),  -- Costco

-- Doritos (cheapest at Costco)
(8, 1, 3.99),  -- Walmart
(8, 2, 3.89),  -- Carrefour
(8, 3, 3.79),  -- Tesco
(8, 4, 3.69),  -- Aldi
(8, 5, 3.29),  -- Costco

-- Ketchup (cheapest at Carrefour)
(9, 1, 2.99),  -- Walmart
(9, 2, 2.49),  -- Carrefour
(9, 3, 2.89),  -- Tesco
(9, 4, 2.79),  -- Aldi
(9, 5, 2.69),  -- Costco

-- Mac & Cheese (cheapest at Tesco)
(10, 1, 2.29), -- Walmart
(10, 2, 2.19), -- Carrefour
(10, 3, 1.79), -- Tesco
(10, 4, 1.99), -- Aldi
(10, 5, 1.89); -- Costco
