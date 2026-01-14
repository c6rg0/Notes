# Defining and updating tables using SQL.

- CHAR(n) - Char string of fixed lengths length n -
  `ProductCode CHAR(6)`.
- VARCHAR(n) - Char string variable length max n - 
  `Surname VARCHAR(25)`.
- INTEGER, INT.
- FLOAT.
- DATE - Stores day, month, year - `HireDate DATE`.
- TIME - Stores time - `RaceTime TIME`.
- CURRENCY - Formats numbers in the currency used in your 
  region - `EntryFee CURRENCY`.

- The `ALTER TABLE` statement is used to add, delete or modify
  columns in an existing table.
- To add a new column:
    - `ALTER TABLE tblProduct`
      `ADD QtyInStock INT`.

- To delete a column:
    `ALTER TABLE tblProduct`
    `DROP QtyInStock`.


# Client-server database:
- A client-server database provides simultaneous access to a 
  database for several clients.

- Database management system (DBMS) software on the server
  processes requests for clients, which are individual 
  workstations.

## Advantages of a client-server system
- Consistency of the database is maintained because only one
  copy is help,
- The reseources of a powerful computer are made available to
  a large number of users,
- Access rights and security are managed centrally,
- Backup and recovery are managed centrally.

# Record locking
- Record locking prevents simultaneous access to objects in
  a database in order to prevent updates being lost or 
  inconsistencies in the data arising.
- With record locking, a record is locked when a user 
  retrieves it for editing or updating.

# Serialisation and timestamp ordering
- Serialisation is an alternative technique used to ensure
  that transactions do not overlap in time.
- In can be implemented using timestamp ordering.
- Every object in the database has a read and write timestamp.
- These are updated whenever an object is read or written.

# Timestamp ordering
- When a user tried to save an update, if the read timestamp 
  is not the same as it was when they started the transaction,
  the DBMS knows another user has accessed the same object.

# Commitment ordering
- This is another serialisation


# Worsheet

## Task 1







