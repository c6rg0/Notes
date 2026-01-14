# Relational database design
- In a relational database, data is help in tables, also
  known as relations.
- One row in the table holds one record,
- Each column represents one attribute,
- Each relation should hold data about a single entity.

# Normalisation
- Normalisation is a process used to come up with the best 
  possible design for a database.
- Tables should be organised so that data is not duplicated
  in the same table or in different tables.
- The structure should allow complex queries to be made.
- There are 3 stages in normalisation, called First Normal 
  Form (1NF), Second Normal Form (2NF) and Third Normal form
  (3NF).

# 1NF
- A table is in the first normal form if it contains no 
  repeating attributes or groups of attributes.
- All attributes must be atomic - a single attribute cannot 
  consist of 2 data items such as firstname and surname.
- This would make it difficult or impossible to sort on 
  surname.

# 2NF
- A table is in second normal form (2NF) if it's in first 
  normal form and contains no partial dependencies.
- This can only occur if the primary key is a composite
  key.

# 3NF
- A table is in third normal form if it's in second normal  
  form and contains no non-key dependencies.
- This can be defined by saying:
    - "All attributes are dependent on the key, the whole
       key and nothing but the key".

# The importance of normalisation
- The advantages of normalisation are that:
    - It is easier to maintain and change a normalised 
      database,
    - There is no unnecessary duplication of data,
    - Data integrity is maintained - if a person changes
      address, for example, the update needs to be made only
      once to a single table.
    - Having smaller tables with fewer fields means faster 
      searches and savings in storage.




# Worksheet:
2. 
a. It has repeating primary keys - there is a max of one 
   branch per town.

b.

| SalesID   | Name      | Branch    |
|-----------|-----------|-----------|
| S123      | Garry     | Norwich   |
|-----------|-----------|-----------|
| S555      | Shirely   | Cromer    |



c. Throught the use of the composite key SalesID.

d. Model is dependent on the manufacturer, so not everything 
   is only dependent on the SalesID.

e. 

f. SalesPerson(SalesID, Name, Branch)
   ProductSales(SalesID, Model, Manufacturer)
   SoldFromManufturer(SalesID, Manufacturer)

g. SalesID, branch(?) and model(?)


