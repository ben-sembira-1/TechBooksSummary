# Chapter 10 - Classes

## Summarizing Instructions
When writing summaries:
1. For each sub-chapter in the chapter:
    1. **While Reading**: Add lots of points under the [Random Points](#random-points) section.
    1. **If you do not fully agree with something**: Add a point in the [Controversial Points](#controversial-points) section.
    1. **After finishing the sub-chapter**: Add rules to the [Rules](#rules) section
1. After finishing the chapter, write an [Overall Summary](#overall-summary) with all the main ideas.

## New Terms
1. _Cohesion_ - The more instance variables a function uses, the more cohesive it is. A class that all its methods use all its instance variables is said to be maximally cohesive.

## Random Points
1. Classes should be very small - By that we mean that a class should have as close to one responsability as possible. Their are some code smells to a too-many-responsability class:
    1. The class name. If the name is not concise or contains on of the words "Processor", "Manager" or "Super" it could hint about a too many responsability class.
    1. Try to write a brief description of the class, if you need to use "if", "and", "or" or "but" it is probably too big.
1. It is ok to start from making our software to work, and to do that in a not too clean fasion way. But the important thing is not to think we finished our work when the code works, we still need to clean it and it is as important if not more then actually making it clean.
1. Many small classes are better than few large ones. The fear of having to travel through too much classes is not real because the reader will need to travel through the same ideas if with one class or with 5, but the difference is that when divided it is organized too.
1. In general, we should try and make classes as _cohesive_ as possible. When the cohesion is high, it means that all the methods are tangled together for a reason, which is a clue that setteling them to be together was correct.
    1. The writer describes a very satisfying process for cleaning code:
        1. Write tests to the code you want to clean.
        1. Change variable names to longer, more percise names.
        1. Seperate big functions to many smaller ones and move variables declared in functions to be instance variables.
        1. Higher the cohesion by gathering variable groups that are modified together, and move them to a seperate class.
    1. This is very cool, and in a certain way satisfying because we it kind of wraps up a lot of the things we learned until now.
1. The writer talks about thinking about why should a class change? And then seperates the class according to the answer. Actually what he did, was a kinda Strategy pattern (Which is the best pattern ever).

## Rules
1. The single responsability principle: A class should have one, and only one, reason to change.
1. Many small classes are better than few large ones.
1. we should try and make classes as _cohesive_ as possible.
1. If the name is not concise or contains on of the words "Processor", "Manager" or "Super" it could hint about a too many responsability class.
1. If you need to use "if", "and", "or" or "but" in a class description, the class is probably too big.

## Controversial Points
1. Dependency inversion is talked in the last chapter, I think I agree. He sais that all classes and functions should depend upon abstractions and not on concrete classes. This way - the dependency is on the interface only, and the change to change a class because a depencey of it changes goes down, and it makes the code more testable. The only think I am a bit afraid of here is to abuse it by creating too much abstractions to minor things that are not important. But should we fear from it? Or is it always a good idea to depend upon interfaces instead of concreate classes? Another questions that rises here is where to put those interface declerations? On the class that uses them side, or in a global scope that stores general abstractions. For python, I think that if we are using protocols it is an easy choise to just put it near the code that uses it becuase we will never need to import it, but in case our intent is to create an abstract base class, where should it be?

## Overall Summary
Here you are supposed to write not more then just a couple of sentences. The idea here is to give 
