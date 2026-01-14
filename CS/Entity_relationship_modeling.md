# Entity
- Entity: A category or object, person, event or thing of 
interest about which data needs to be recorded. Each entity 
has attributes.

# Identifier (primary key)
- Each entity needs an identifier with uniquely identifies 
  a particular record.
- In a relational database, the identifier is known as the 
  primary key. It is underlined in the entity description.
- The is no natural attribute for a primary key, one should be
  introduced.

# Composite primary key
- Sometimes two or more attributes are needed to uniquely 
  define a record. 
- For example, in a customer order consisting of many
  different order lines, each order line may be uniquely 
  identified by the two attributes orderNumber and orderLine. 
- OrderLine(OrderNumber, OrderLine, ProductId, ...)
- OrderNumber, OrderLine is a composite primary key

# Relationshpips between entities
- The three entities are linked or related,
- There are three possible ways in which two entities may be
  related:
    - One-to-one    e.g. husband and wife
    - One-to-many   e.g. mother and child, school and pupil
    - Many-to-many  e.g. actor and film

# Entity relationship diagrams
- An entity (E-R) diagram is a graphical way of representing
  the relationships between entities.
- (see the slides for the diagram)
- We can say, for example, that one school has many pupils,
  or many pupils attend one school.

## Worksheet
1. An entity is a category or object, person, event or thing 
of interest about which data needs to be recorded. Each 
entity has attributes.

2. The three degries of relationships between entities are 
one-to-one, one-to-many and many-to-many.

3. Draw entity relationship diagrams for each of the following
pairs of related entities:
    a. Dentist and patient       
    Dentist >--- Patient, Many to one
    b. Student and teacher
    Student >--< Teacher, Many to many
    c. UK citizen and UK passport
    UK citizen----UK passport, One to one
    d. Product and component
    Product >--- Component, Many to one

4. Customer >--- Product, Many to one
   Order ---< OrderLine, One to many

5. Customer details: email, name, banking details,
   Address: 73 waterloo street, 92 fishermead grove, 
   1 queensway,
   OrderNumber: 6328, 1230, 2438,
   Date: 2/12/09, 12/11/25, 06/05/15
   Line: ?
   Qty: ?
   Product code: 97209, 4382340, 1281
   Description: A kitchen knife, bike, games console
   Unit price: 36, 29, 385
   Total: 36, 29, 385
   Total price: 40, 35, 420

# Database structure
- Each entity is represented as a table,
- Tables in a relational database are commonly reffered to as
  relations,
- A database contains one or more relations,
- A relation has rows, each row containing one record,
- The columns in the relation each contain one field (i.e.
  attribute) belonging to the records).

# Many-to-many relationships
- When there is a many-to-many relationship between tables, 
  they cannot be directly linked,
- However, you can link tables "in the middle" just as the 
  entity between customer and product:
    Member ---< Enrolment >--- Class.



