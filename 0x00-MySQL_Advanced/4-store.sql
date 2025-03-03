-- Script that creates a trigger that decreases quantity of an item after a pending order
CREATE TRIGGER reduce_quantity AFTER INSERT ON orders FOR EACH ROW
UPDATE items SET quantity = quantity - NEW.number WHERE name = NEW.item_name;
