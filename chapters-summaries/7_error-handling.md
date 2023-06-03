# Chapter 7 - Error Handling
**Name, put your summary here**

## Random Points
1. I really like the wrapper thing style! I think it is a great idea to wrap 3rd party functions to not mess with ugly interfaces in the main logic.

## Rules
1. Prefer exceptions on error return codes, especially NULLs.
1. _Try making the error handling logic in the same abstract level as the code near it_

## Contraversial Points
1. I am not sure I agree about the point about checked exceptions.. I feel like if the implementation of an internal function changes in a way that can effect the caller (obviously true if the function can throw a new kind of exception) then the caller should give it some kind of treatment. A treatment can be doing nothing, but in this case the above caller will be potentially caught unready, and should give it treatment. Maybe I missed the point in some matter, but I really think that checking exceptions in a way of explicitly writing what exceptions the caller expects is a good path going through. In general I think that an IDE add-on that writes on each function what it may throw and from what root, is a good add-on. I really prefer handling all my errors anywhere instead of being surprised at runtime. Moreover, maybe a linter that forces me to catch or throw all the errors that may jump is a good idea.
1. I am not sure what I think about the NEVER PASS NULL thing, because if I typed an argument to get NULL I think it is OK to use NULL as a nothing object to represent something that we do not want to use (maybe like a filter that we do not want, or a logger that we do not want). But when I am thinking more about it, it is probably best practice to just send an empty filter that passes everything, or a void logger - Most likely to be more readable.

## Overall Summary
I really think that incorrect error handling can make a really hard to read and maintain code, mostly because of the blend in logic and specific error handling logic. I think we can not and **should not** try to remove error handling from the main logic, as it is just a way for specifying our program edge cases, but we should make the error handling logic be in the same abstraction layer as the logic in the same function, which can be a hard task, but in my opinion, really important for code readability and maintainability.
