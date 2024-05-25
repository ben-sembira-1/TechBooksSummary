# Chapter 1 - Clean Code
**Ben Sembira**

## (Maybe) Interesting Ideas
1. Rushing to add more and more features without cleaning the code and creating a mess, will give an immediate "cash" boost to the product, but if not fixing it quickly, it will add up and create by the long term an unsustainable code that as the environment keeps changing will catch more bugs, more crashes and eventually become unusable and end its life. This process is a multi-year process, that is hard to put the finger on the point in time where the project passed the point of no return.
1. _Later equals never_
1. It is your responsibility to defend the code the same way it is your manager responsibility to defend the schedule. Do not blame the pressure, schedule or managers that the code has rotten, it is your responsibility to defend it and do all you can to keep it clean and tidy.
1. Most of the time making mess slows down the pace almost instantly, and will make the deadline that in the essence of meeting it you did not write clean code - will be absurdly missed.
1. To identify messy code is much easier then to clean messy code.
1. Clean code heuristics:
    1. Bad code tries to do too much.
    1. Clean code should read like well-written prose.
    1. Smaller is better.
    1. Code should be literate.
    1. Clean code is code that has been taken care of.
    1. When you read clean code you should not be surprised at all.
    1. It is not the language that makes programs appear simple. It is the programmer that make the language appear simple!
1. Don’t make the mistake of thinking that we (The book authors) are somehow “right” in any absolute sense. There are other schools and other masters that have just as much claim to professionalism as we. It would behoove you to learn from them as well.
1. The next time you write a line of code, remember you are an author,
writing for readers who will judge your effort.
1. We most of the time **read** code and not write code. The ratio is surprisingly high.
1. Leave the campground cleaner than you found it.

## Questions
1. None

## Unclear Points
1. None

## Research I Did
1. I am reading at the same time the book "Atomic Habits" which explains how small changes in our habits and point of view can make a huge impact on our quality of life. Although different I think one fact he is talking about is highly relevant in the context of clean code. The "Atomic Habits" writer talks about small changes in context of self improvement. One of his takes is that given a subject that is important to us, only 1% of improvement a day will evaluate at the end of a year as a huge 37 times improvement (1.01 raised to the power of 365 equals approximately to 37). Of course that this 1% improvement is not actually measurable, but the idea here is that even though in the moment of a small change it will probably pass un-notable or even may be unnoticeable, small changes add together in a surprisingly fast exponential nature. Connecting this to clean code - Making the code you are working on just 1% better/cleaner/faster every time you pass through will probably pass without anyone noticing, but if every one will do it, this code will faster than you think become much much better. And the same is true to the other direction, if while adding a feature every day we will add just 1% of clutter, it will not be noticeable at all, but eventually after just one year the math throws us to a horrifying 97% degradation. Each small change does not matter and we should not feel very bad or very good when doing a small change to any direction, but we should create a culture that blesses and appreciates small upgrades and improvements done along the way. Connecting it to the real world - we most of the time have tight schedules and stakeholders that put pressure on us to finish as fast as possible, so we usually can not afford huge changes that are not urgent, but removing some clutter and cleaning a bit of code when passing through it can add to the schedule just a little bit more, in a fashion that nobody will ever even notice. The long term effect of this kind of culture is invaluable. Important note here: We still did not talk about what is clean code, why clean code is good and how it effects our products. This is the essence of the book and we are in front of hard time convincing ourselves that the takes in the book are actually valuable and relevant. This specific take assumes that you know how to improve the code in a matter that you believe makes positive impact.
1. Ron Jeffries talks about duplication. He says that _"when the same thing is done over and over, it’s a sign that there is an idea in our mind that is not well represented in the code. I try to figure out what it is. Then I try to express that idea more clearly."_ This is true, but I have to emphasize here the fact that after he finds duplication he starts to search for the idea that is not well represented in the code and just **after** he finds the idea he tries to express it in code. Finding duplication is easy, understanding the abstract idea that made the duplication present in the code is sometimes very hard, and you may not find it. In rare cases - the duplication is just pure accidental. When you can not find the abstract idea from the domain the code emerged from, you really should not try and make an abstraction to the duplication. In my opinion **duplication is better then wrong abstraction.**

## Controversial Points
1. Ron Jeffries says that part of the definition of clean code for him is: _"early building of simple abstractions"_. I guess that the magic word here is _simple_ but I am still a bit confused because I know the problems that emerge when abstractions are made to early. Most of the time they present complexity that at the time written is not needed, and may never be needed. Maybe by simple he means abstractions that we know from our experience that will probably be needed? The example of finding inside a collection is of this kind, it is obvious for an experienced engineer that creating an abstraction to collections will have good impact on the code.

