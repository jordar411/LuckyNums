### Conceptual Exercise

Answer the following questions below:

- What is RESTful routing?
A standardized architectural style for website services which defines constraints such as the client-server model, statelessness, and cacheability.

- What is a resource?
 An object with a type, associated data, relationships to other resources, and a set of methods that operate on it.

- When building a JSON API why do you not include routes to render a form that when submitted creates a new user?
The SQLAlchemy model information for the user must first be serialized before being jsonified.

- What does idempotent mean? Which HTTP verbs are idempotent?
This means that an operation can be performed again and again with the same data and the result will always be the same. GET, PUT/PATCH, AND DELETE are all idempotent HTTP verbs.

- What is the difference between PUT and PATCH?
A PUT request suggests that an entire resource is being updated, while a PATCH request should only update part of a resource.

- What is one way encryption?
One way encryption means that the original password cannot be reverse engineered from the hashed password.

- What is the purpose of a `salt` when hashing a password?
A salt is a random string introduced to the password before hashing that further complicates the hashing process and makes the password more secure.

- What is the purpose of the Bcrypt module?
The purpose of the Bcrypt module is to generate a secure, hashed password using a slow and complicated algorithm.

- What is the difference between authorization and authentication?
Authorization means a particular user is or is not "allowed" to access a resource, while authentication is determining whether a user is who they say they are.

- What are some ways to manage the complexities of a large codebase, like Warbler?
Some ways to manage these complexities are by breaking your code up into related models and DRYing your code