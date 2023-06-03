# Chapter **X** - **Name Of Chapter**
**Name, put your summary here**

## Summarizing Instructions
When writing summaries:
1. For each sub-chapter in the chapter:
    1. **While Reading**: Add lots of points under the [Random Points](#random-points) section.
    1. **If you do not fully agree with something**: Add a point in the [Contraversial Points](#contraversial-points) section.
    1. **After finishing the sub-chapter**: Add rules to the [Rules](#rules) section
1. After finishing the chapter, write an [Overall Summary](#overall-summary) with all the main ideas.

## Random Points
1. I am not sure I agree about the point about checked exceptions.. I feel like if the implementation of an internal function changes in a way that can effect the caller (obviously true if the function can throw a new kind of exception) then the caller should give it some kind of treatment. A treatment can be doing nothing, but in this case the above caller will be potentially caught unready, and should give it treatment. Maybe I missed the point in some matter, but I really think that checking exceptions in a way of explicitly writing what exceptions the caller expects is a good path going through. In general I think that an IDE add-on that writes on each function what it may throw and from what root, is a good add-on. I really prefer handling all my errors anywhere instead of being surprised at runtime. Moreover, maybe a linter that forces me to catch or throw all the errors that may jump is a good idea.

## Rules
1. Here you write all the rules that were written in the chapter
1. _for rules that are not written in the chapter, write as italic text_

## Contraversial Points
1. Here you write any thing that you do not fully agree with :)

## Overall Summary
Here you are supposed to write not more then just a couple of sentences. The idea here is to give 
