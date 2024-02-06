-- === TASK 1 ===

-- DROP INDEX IF EXISTS j1, j2, j3, j4, j5, j6, j7, j8, j9;

CREATE INDEX j1 ON actor USING HASH(first_name);
CREATE INDEX j2 ON film USING HASH(film_id);
CREATE INDEX j3 ON customer USING HASH(first_name);
CREATE INDEX j4 ON film_actor(film_id, actor_id);
CREATE INDEX j5 ON rental(customer_id, inventory_id);
CREATE INDEX j6 ON inventory(film_id, inventory_id);
CREATE INDEX j7 ON film_category(film_id, category_id);

-- === TASK 2 ===

-- DROP INDEX IF EXISTS j21;
CREATE INDEX j21 ON inventory(film_id, inventory_id);

-- === TASK 3 ===

-- DROP INDEX IF EXISTS j31;
CREATE INDEX j31 ON rental(last_update);

-- === TASK 4 ===

-- DROP INDEX IF EXISTS j41, j42;;
CREATE INDEX j41 ON film(rental_rate DESC, length ASC);
CREATE INDEX j42 ON film_category(category_id ASC);
