# What is REST?

**RE**presentational **S**tate **T**ransfer uses HTTP 'verbs' (methods) to interact with resources.

* A resource is some representation of data accessible by URI
* Each resource is uniquely identified
* HTTP methods represent typical operations (CRUD)
* Output/transport format agnostic (HTML, JSON, XML…)

# What is REST - Resources

* Resources represent data and are accessible by unique URIs.

    + `/customers/1`
    + `/orders/2012/04/MP29`
    + `/products/42`
    + `/movies/snakes-on-a-plane`

* The same URI is used for most operations (Read, Update, Delete)
    * Parent URI used for Create

# What is REST - HTTP Methods

HTTP methods correspond to typical operations

<table style="width: 80%">
    <tr><th>CRUD operations</th><th>HTTP methods</th></tr>
    <tr><td>Create</td><td>`POST`</td></tr>
    <tr><td>Read</td><td>`GET`</td></tr>
    <tr><td>Update</td><td>`PUT`</td></tr>
    <tr><td>Delete</td><td>`DELETE`</td></tr>
</table>

1. `POST` data to `/customers` to *create* a new customer
2. `GET` from `/customers/123` to *read* the information
3. `PUT` to `/customers/123` to *update* customer info
4. `DELETE` `/customers/123` to *delete* a record

# What is REST - Read more 
* Proposed in Roy Thomas Fielding's Thesis [Architectural Styles and
the Design of Network-based Software Architectures](http://www.ics.uci.edu/~fielding/pubs/dissertation/top.htm)
* [A Brief Introduction to REST](http://www.infoq.com/articles/rest-introduction)
