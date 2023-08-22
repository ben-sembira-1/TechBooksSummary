# Chapter Creational Patterns - Abstract Factory
Ben Sembira

## (Maybe) Interesting Ideas
1. Consequences:
    1. It isolates concrete classes.
    1. It makes exchanging product families easy.
    1. It promotes consistency among products.
    1. Supporting new kinds of products is difficult.


## Questions
1. In aplicability - what is: you want to provide a class library of products, and you want to reveal just
their interfaces, not their implementations.
1. Why does a factory as a singleton is a good idea?
1. Is their a way to ensure in the typesystem that the types that are being sent to an object correspond to its family of objects? I really do not like those down casting patterns. It is wierd because it makes the "Wall" coupled to the Factory that creates it. What will happen if one day someone else will decide to create or use a Wall of its own? This down cast can make a lot of trouble.

## Unclear Points
1. I did not understand the section about creating the products in "Implementation". Why does a factory method helps their? Generally all this section was unclear.
1. I hate smalltalk

## Research I Did
1. -

## Controversial Points
1. The writer talks about another variation of the abstract factory pattern, in which their is only one function that creates an object just by name. It sounds for me as a SUPER ANTI PATTERN to do so. Very not clean in my opinion. He says himself that this is not very good, but says it is the tradeoff for highly dynamic and flexible code.
1. Here the writer shows a pattern in which the abstract factory is not abstract and has default implementations. Do we like it? It can be difficult to track in some cases from where the creation function came from.

