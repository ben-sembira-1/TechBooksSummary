# Chapter 4 - Comments
**Ben, put your summary here**

## Summarizing Instructions
When writing summaries:
1. For each sub-chapter in the chapter:
    1. **While Reading**: Add lots of points under the [Random Point](#random-points) section.
    1. **If you do not fully agree with something**: Add a point in the [Contraversial Points](#contraversial-points) section.
    1. **After finishing the sub-chapter**: Add rules to the [Rules](#rules) section
1. After finishing the chapter, write an [Overall Summary](#overall-summary) with all the main ideas.

## Random Points
1. Comments May be good, may create a mess, and may be lieing and creating bugs.
1. Using comments is a sign of **failure** expressing ourselfes using code.
1. Using comments is bad because it is near impossible to **always** maintain them while the code changes, And even if you do manage to **always** maintain your comments, this is probably taking you way too much time.
1. Inaccurate comments are far worse than no comments.
1. Instead of commenting bad code, clean bad code.
1. Creating a function with a name of what you want to comment, is not harder and far better then adding a comment.
1. There are good comments. Here are examples:
    1. Copywrites comments
    1. Warning of consiquences?
    1. Todos
    1. Public API docs.
    1. 
1. A comment should not make the reader look on other parts of the code to get the full picture.
    1. _I think that in the case of the comment in the emtpy catch block, the correct thing to do is to remove the comment and do whatever you need to do in a different way._
1. Sometimes the code is more readable then a comment. Commenting short readable code is meaningless.
1. 

## Rules
1. Clean bad code instead of documenting bad code.
    1. This can be done by using constants, functions (inline if you are using low level langueges and the amount of stack calls metters to you), and better names.
    1. Longer names are much better then adding documentation.
1. Clean todos regularly, and try not to put them in the first place by cleaning the code its talking about.

## Contraversial Points
1. I disagree with alot of the _good comments_ section.
    1. He says that putting the format regex function in a class can remove the comment: `// format matched kk:mm:ss EEE, MMM dd, yyyy`. I am not sure how, and in this specific case, how it is good to do so.
        1. Maybe a single function with only 2 lines: the first is this comment, and the second is the actual regex?
        1. I have to say that for this specific example, I think it is better to find a standard with a name and use its name, but in case there is not standard, This is a tricky question how to solve it.
        1. Maybe replace the strings with lots of constants? See [Apendix A](#apendix-a---format-matching-comments).
    1. Similar to the previous point, won't it be beter to just use constants? See [Apendix B](#apendix-b---put-intent-inside-a-constant).
    1. And why is this [solution](#apendix-c---remove-comment-using-a-function) not just better?
    1. And [this](#apendix-d---explain-bad-api-with-comments)?
    1. I am not sure about the Warning of consequences comment.. I am not sure but maybe creating a linter that takes as configurations a list of bad-named modules, and their facade replacement and then the linter will prevent using the original modules, and suggest using the facade replacement instead. What do you think??
    1. In the amplification example, whould not it be better to just create a function with an apropriate name?
1. In listing 4-4 he argued that the first comment is OK. But is it? See [Apendix D]()

## Overall Summary
Here you are supposed to write not more then just a couple of sentences. The idea here is to give 


## Apendix
### Apendix A - format matching comments
From Book:
```python
// format matched kk:mm:ss EEE, MMM dd, yyyy
Pattern timeMatcher = Pattern.compile(
    "\\d*:\\d*:\\d* \\w*, \\w* \\d*, \\d*");
```
My suggestion:
```python
def generateTimeMatcher():
    LOW_LETTERS_SEQUENCE = "\\d*"
    CAPITAL_LETTERS_SEQUENCE = "\\w*"

    kk = mm = ss = dd = yy = LOW_LETTERS_SEQUENCE
    EEE = MMM = CAPITAL_LETTERS_SEQUENCE
    return Pattern.compile(f"{kk}:{mm}:{ss} {EEE}, {MMM} {dd}, {yyyy}")

...

Pattern timeMatcher = generateTimeMatcher()
```

### Apendix B - put intent inside a constant
From book:
```c++
public int compareTo(Object o)
{
    if(o instanceof WikiPagePath)
    {
        WikiPagePath p = (WikiPagePath) o;
        String compressedName = StringUtil.join(names, "");
        String compressedArgumentName = StringUtil.join(p.names, "");
        return compressedName.compareTo(compressedArgumentName);
    }
    return 1; // we are greater because we are the right type.
}
```
My suggestion:
```c++
public int compareTo(Object o)
{
    GREATER_THEN_OBJECTS_THAT_ARE_NOT_THE_RIGHT_TYPE = 1

    if(o instanceof WikiPagePath)
    {
        WikiPagePath p = (WikiPagePath) o;
        String compressedName = StringUtil.join(names, "");
        String compressedArgumentName = StringUtil.join(p.names, "");
        return compressedName.compareTo(compressedArgumentName);
    }

    return GREATER_THEN_OBJECTS_THAT_ARE_NOT_THE_RIGHT_TYPE;
}
```

### Apendix C - remove comment using a function
From book:
```c++
public void testConcurrentAddWidgets() throws Exception {
    WidgetBuilder widgetBuilder =
        new WidgetBuilder(new Class[]{BoldWidget.class});
    String text = "'''bold text'''";
    ParentWidget parent =
        new BoldWidget(new MockWidgetRoot(), "'''bold text'''");
    AtomicBoolean failFlag = new AtomicBoolean();
    failFlag.set(false);
    //This is our best attempt to get a race condition
    //by creating large number of threads.
    for (int i = 0; i < 25000; i++) {
        WidgetBuilderThread widgetBuilderThread =
            new WidgetBuilderThread(widgetBuilder, text, parent, failFlag);
        Thread thread = new Thread(widgetBuilderThread);
        thread.start();
    }
    assertEquals(false, failFlag.get());
}
```
My suggestion:
```c++
private void attemptToGetARaceCondition(std::function<WidgetBuilderThread()> widgetBuilderThreadFactory){
    for (int i = 0; i < 25000; i++) {
        Thread thread = new Thread(widgetBuilderThreadFactory());
        thread.start();
    }
}

public void testConcurrentAddWidgets() throws Exception {
    WidgetBuilder widgetBuilder =
        new WidgetBuilder(new Class[]{BoldWidget.class});
    String text = "'''bold text'''";
    ParentWidget parent =
        new BoldWidget(new MockWidgetRoot(), "'''bold text'''");
    AtomicBoolean failFlag = new AtomicBoolean();
    failFlag.set(false);

    private WidgetBuilderThread widgetBuilderThreadFactory() {
        return new WidgetBuilderThread(widgetBuilder, text, parent, failFlag);
    }
    attemptToGetARaceCondition(widgetBuilderThreadFactory);

    assertEquals(false, failFlag.get());
}
```

### Apendix D - Explain Bad API With Comments
From book:
```c++
public void testCompareTo() throws Exception
{
    WikiPagePath a = PathParser.parse("PageA");
    WikiPagePath ab = PathParser.parse("PageA.PageB");
    WikiPagePath b = PathParser.parse("PageB");
    WikiPagePath aa = PathParser.parse("PageA.PageA");
    WikiPagePath bb = PathParser.parse("PageB.PageB");
    WikiPagePath ba = PathParser.parse("PageB.PageA");
    assertTrue(a.compareTo(a) == 0);
    // a == a
    assertTrue(a.compareTo(b) != 0);
    // a != b
    assertTrue(ab.compareTo(ab) == 0); // ab == ab
    assertTrue(a.compareTo(b) == -1); // a < b
    assertTrue(aa.compareTo(ab) == -1); // aa < ab
    assertTrue(ba.compareTo(bb) == -1); // ba < bb
    assertTrue(b.compareTo(a) == 1);
    // b > a
    assertTrue(ab.compareTo(aa) == 1); // ab > aa
    assertTrue(bb.compareTo(ba) == 1); // bb > ba
}
```
My suggestion:
```c++
public void testCompareTo() throws Exception
{
    WikiPagePath a = PathParser.parse("PageA");
    WikiPagePath ab = PathParser.parse("PageA.PageB");
    WikiPagePath b = PathParser.parse("PageB");
    WikiPagePath aa = PathParser.parse("PageA.PageA");
    WikiPagePath bb = PathParser.parse("PageB.PageB");
    WikiPagePath ba = PathParser.parse("PageB.PageA");

    BIGGER_THEN_ARGUMENT = 1
    SMALLER_THEN_ARGUMENT = -1
    EQUAL_TO_ARGUMENT = 0

    assertTrue(a.compareTo(a) == EQUAL_TO_ARGUMENT);
    assertTrue(a.compareTo(b) != EQUAL_TO_ARGUMENT);
    assertTrue(ab.compareTo(ab) == EQUAL_TO_ARGUMENT);
    assertTrue(a.compareTo(b) == SMALLER_THEN_ARGUMENT);
    assertTrue(aa.compareTo(ab) == SMALLER_THEN_ARGUMENT);
    assertTrue(ba.compareTo(bb) == SMALLER_THEN_ARGUMENT);
    assertTrue(b.compareTo(a) == BIGGER_THEN_ARGUMENT);
    assertTrue(ab.compareTo(aa) == BIGGER_THEN_ARGUMENT);
    assertTrue(bb.compareTo(ba) == BIGGER_THEN_ARGUMENT);
}
```

### Apendix E - redundent comment in empty catch block
From book:
```cpp
try
{
    doSending();
}
    catch(SocketException e)
{
    // normal. someone stopped the request.
}
```
My suggestion:
```cpp
using RequestStoppedException = SocketException
try
{
    doSending();
}
    catch(RequestStoppedException e)
{}
```
