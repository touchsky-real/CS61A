CREATE TABLE parents AS
  SELECT "ace" AS parent, "bella" AS child UNION
  SELECT "ace"          , "charlie"        UNION
  SELECT "daisy"        , "hank"           UNION
  SELECT "finn"         , "ace"            UNION
  SELECT "finn"         , "daisy"          UNION
  SELECT "finn"         , "ginger"         UNION
  SELECT "ellie"        , "finn";

CREATE TABLE dogs AS
  SELECT "ace" AS name, "long" AS fur, 26 AS height UNION
  SELECT "bella"      , "short"      , 52           UNION
  SELECT "charlie"    , "long"       , 47           UNION
  SELECT "daisy"      , "long"       , 46           UNION
  SELECT "ellie"      , "short"      , 35           UNION
  SELECT "finn"       , "curly"      , 32           UNION
  SELECT "ginger"     , "short"      , 28           UNION
  SELECT "hank"       , "curly"      , 31;

CREATE TABLE sizes AS
  SELECT "toy" AS size, 24 AS min, 28 AS max UNION
  SELECT "mini"       , 28       , 35        UNION
  SELECT "medium"     , 35       , 45        UNION
  SELECT "standard"   , 45       , 60;


-- All dogs with parents ordered by decreasing height of their parent
CREATE TABLE by_parent_height AS
  SELECT d.name FROM dogs AS d,parents AS p, dogs AS pd
  WHERE d.name = p.child AND p.parent = pd.name
  ORDER BY pd.height DESC;





-- The size of each dog
CREATE TABLE size_of_dogs AS
  SELECT d.name,s.size
  FROM dogs as d,sizes AS s
  WHERE d.height > s.min AND d.height <= s.max;



-- [Optional] Filling out this helper table is recommended
CREATE TABLE siblings AS
  SELECT a.child AS first, b.child AS second
  FROM parents AS a, parents AS b
    WHERE a.parent = b.parent AND a.child < b.child;


-- Sentences about siblings that are the same size
CREATE TABLE sentences AS
  SELECT "The two siblings, "||s.first||" and "||s.second||", have the same size: "||sd1.size
  FROM siblings AS s, size_of_dogs AS sd1, size_of_dogs AS sd2
  WHERE s.first = sd1.name AND s.second = sd2.name AND sd1.size = sd2.size;


-- Height range for each fur type where all of the heights differ by no more than 30% from the average height
CREATE TABLE low_variance AS
  SELECT fur,MAX(height)-MIN(height) AS height_range
  FROM dogs
  GROUP BY fur
  HAVING  MIN(height) >= 0.7 * AVG(height) AND MAX(height) <= 1.3 * AVG(height);

