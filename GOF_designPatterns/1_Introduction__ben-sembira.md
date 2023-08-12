# Chapter 1 - Introduction
Ben Sembira

Pages 1-18:
---
---

## (Maybe) Interesting Ideas
1. It is near impossible to get the "right" design at first try.
1. A way for testing if a design is good, is to try and reuse / extend it several times and see how hard it is.
1. Expert software designers do not invent new solutions for every problem, but use a solution that worked for them in the past.
1. Decomposing a system into objects may influence on: encapsulation, granularity, dependency, flexibility, performance, evolution and reusability.
1. The writer talks about three methodologies to design software:
  1. **Using our natural language:** Factor the nouns and verbs from the problem statement.
  1. **Analyzing collaborations and responsibilities:** Focus on the collaborations and responsibilities in the system.
  1. **Modelling the real world:** Model the real world and translate the objects found during analysis into design.
1. According to the writer, using only real-world oriented technics can make a design reflect todays problems, but not tomorrows, for answering this problem we present abstractions but the problem here is the difficulty in spotting the abstractions needed, because they do not have a real-world counterpart. For this, we define design patterns.
1. The writer talks about the definition of types (or interfaces), it is interesting how different it is from our python world (put out protocols) where types are the classes declarations themselves. Here, he talks about the philosophical definition of types, which is the set of *promises* an object should fulfil. This type of definition can open a whole new ara of typing polymorphism. I think it is a great approach because it decouples implementation details from the root, this is the main reason I like typescript.
1. Dynamic-Binding - The run-time association of a request to a concrete implementation.


## Questions
1. Here you write questions that you asked yourself during the reading.

## Unclear Points
1. At page 18, they talk about the idea of deriving from abstract base classes while sharing the same interface. How is it possible to do so without?

## Research I Did
1. What is the meaning of the terms: encapsulation, granularity, dependency, flexibility, performance, evolution and reusability?
    1. **Encapsulation:** The bundling of data with the mechanisms or methods that operate on the data. It may also refer to the limiting of direct access to some of that data, such as an object's components. (Wikipedia)
    1. **Granularity:** Granularity is the degree to which a material or system is composed of distinguishable pieces. (Wikipedia)
    1. **Dependency:** A situation in which you need something or someone and are unable to continue normally without them. (Cambridge Dictionary)
    1. **Flexibility:** The ease with which the system can respond to uncertainty in a manner to sustain or increase its value delivery. (Wikipedia)
    1. **Performance:** A degree of how well a system is working, estimated through a set of chosen aspects in which the system is measured by. (Ben Sembira with some help of Wikipedia, I could not find a good and full general definition)
    1. **Evolution:** A process of continuous change from a lower, simpler, or worse to a higher, more complex, or better state. (Merriam Webster dictionary)
    1. **Reusability:** The ability to be used more than once. (Collins Dictionary)

## Controversial Points
1. The book says that: *Program to an interface, not an implementation.* Is it always a good idea? Can't it sometimes make the code hard to debug through because going up is hard? I am not sure, but tending to agree with the writer most of the times. I think that the part that is missing to me, is the fact that the language of interfaces and types, is not precise enough, it can promise what functions will be and the structure of the inputs and outputs, but not what behavior do you expect. I would fill much more comfortable with using abstraction everywhere if I had a tool to check that every class that pretends to fulfil the interface, behaves in a specific way. For example, if I get an object that pretends to fulfil a function "generate_one_or_more_dogs_and_one_or_more_cats" that returns a list of animals with dogs and cats, if I want to know that their is at least one cat and at least one dog - I can't do that to all the subclasses without testing them all manually. Another example is that I have no tools to make sure that objects of type "sortable" with the method "sort" actually sorts the data they get. Maybe a feature in future programming languages can be to test all objects that pretend to fulfil an interface with specific tests.


Pages 18-32:
---
---

## (Maybe) Interesting Ideas
1. The writer talks about inheritance and composition as alternatives to each other, and the differences between them:
    1. Advantages of **inheritance** over composition:
        * Inheritance is straight forward to use because it is part of the language. [UnclearPoints-1](#unclear-points-1)
        * Inheritance makes it easier to change the reusable code by overriding methods.
        * Dynamic, highly parameterized software is harder to understand than more static software.
        * Inheritance is more efficient at runtime.
    1. Advantages of **composition** over inheritance:
        * With composition it is possible to change the implementation used for the reusable code at run time.
        * Inheritance breaks encapsulation because parent classes exposes implementation details to their subclasses. - Change in parent will probably cause the subclass to change.
            * This limits *flexibility* and *reusability*
        * Favoring composition will lead to more encapsulated and focused classes, because implementation details do not matter.
        * (My addition) If inheritance is used extensively, it can lead to deep inheritance trees, which are very hard to debug and understand because it is not clear from where each implementation comes from.
    1. This leads the writer to write: **"Favor object composition over class inheritance"**, but because of the advantages of inheritance, we should probably use them together.
1. *Delegation:* To give a particular job, duty, right, etc. to someone else so that they do it for you. The writer talks about delegation as a simple pattern to replace inheritance by composition. It has the advantages of composition, but makes the software more complex and should be used carefully, maybe mostly in standardized design patterns.
1. Human inefficiencies are more important then runtime inefficiencies in the long run.
1. The writer talks about templates in c++, but **be aware**, this is not exactly the same as generics it python. The difference is that templates in c++ are available at runtime, while generics are purely for "lint-time". For example you can`t call a function given as a generic parameter, or instantiate an object from a class given as a generic parameter in python.
1. *Aggregation* and *acquaintance* are 2 kind of philosophical properties describing a relationship between objects. Aggregation stands for objects **having** other objects, and acquaintance stands for objects **using** other objects.
1. It happens a lot that run-time structures aren't clear from the code until you understand the patterns used.
1. Each design pattern helps make specific aspects of the code extensible and flexible. To choose a design pattern, start by thinking about how the requirements may change in the future.
1. Because the nature of inheritance, that in the short term makes things simpler but at the long term if used to much makes things hard to understand and highly coupled, most design patterns use the short term advantages by producing not more than one layer of inheritance, along side with composition.
1. An added benefit to using design patterns is that one can document code using the names of the design patterns he used and thus making it easy to learn for new comers.

## Questions
1. Here you write questions that you asked yourself during the reading.

## Unclear Points
1. Why is inheritance more straight forward to use then composition? Is it because Composition requires indirection?
1. When talking about frameworks and design patterns differences, the following line was written: "A graphical editor framework might be used in a factory simulation, but it won't be mistaken for a simulation framework". What does it mean?

## Research I Did
1. If you found yourself researching about something, write about it here.

## Controversial Points
1. Here you write any thing that you do not fully agree with.
