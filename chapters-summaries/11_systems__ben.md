# Chapter 11 - Systems

## Summarizing Instructions
When writing summaries:
1. For each sub-chapter in the chapter:
    1. **While Reading**: Add lots of points under the [Random Points](#random-points) section.
    1. **If you do not fully agree with something**: Add a point in the [Controversial Points](#controversial-points) section.
    1. **After finishing the sub-chapter**: Add rules to the [Rules](#rules) section
1. After finishing the chapter, write an [Overall Summary](#overall-summary) with all the main ideas.

## Random Points
1. Software should separate construction from usage when dealing with objects. The writer explains this by the fact that constructing and using an objects are 2 complicated and different operations.
1. The writer gives as an example a lazy constructor pattern that creates a default when called. He says it is bad because now the general class takes care of initializing a specific object, while the user may not even need it and use a different one. I am not sure I fully understood, but if I did, the writer is kind of saying the we should not lazy initialize our objects and try to keep all creation in the start of the application, and if we do need for some reason, we should do it with abstract factories. When we do choose to create a lazy constructor for optimizing our startup times, we should make sure it is not a premature optimization.
1. In the diagrams he puts, he shows that all the arrows goes out from the main, and nothing comes back. It is a bit straight forward, but important, and it sounds correct to separate in mind the creation of all objects, to their usage.
1. The writer talks about dependency injection, and inversion of control, which are giving an object its dependencies as arguments from outside, and the concept of giving the control to what is being instantiated to the objects container.
1. 

## Rules
1. Here you write all the rules that were written in the chapter
1. _for rules that are not written in the chapter, write as italic text_

## Controversial Points
1. Here you write any thing that you do not fully agree with :)

## Overall Summary
Here you are supposed to write not more then just a couple of sentences. The idea here is to give 
