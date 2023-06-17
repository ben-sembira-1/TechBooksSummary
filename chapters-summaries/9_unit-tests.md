# Chapter 9 - Unit Tests
**Name, put your summary here**

## Summarizing Instructions
When writing summaries:
1. For each sub-chapter in the chapter:
    1. **While Reading**: Add lots of points under the [Random Points](#random-points) section.
    1. **If you do not fully agree with something**: Add a point in the [Contraversial Points](#contraversial-points) section.
    1. **After finishing the sub-chapter**: Add rules to the [Rules](#rules) section
1. After finishing the chapter, write an [Overall Summary](#overall-summary) with all the main ideas.

## Random Points
1. About clean tests, I totaly agree, about TDD, I need to think more about it.
1. He gave a

## Rules
1. Here you write all the rules that were written in the chapter
1. _for rules that are not written in the chapter, write as italic text_

## Contraversial Points
1. He gave an example of tests that does multiple assertions. I do not like the shortcuts he did.

## Overall Summary
Here you are supposed to write not more then just a couple of sentences. The idea here is to give 

## Appendix

### Appendix A - short assertions
His code:
```Java
@Test
 public void turnOnCoolerAndBlowerIfTooHot() throws Exception {
 tooHot();
 assertEquals("hBChl", hw.getState());
 }
```

My code:
```Java
@Test
 public void turnOnCoolerAndBlowerIfTooHot() throws Exception {
 tooHot();
 assertMulptipeTrues(hw.heaterState(), hw.blowerState(), hw.loTempAlarm());
 assertMulptipeFalses(hw.coolerState(), hw.hiTempAlarm());
 }
```

Or alternative code:
```Java
@Test
 public void turnOnCoolerAndBlowerIfTooHot() throws Exception {
 tooHot();
 assertEqualFields(
    {
        heater: true,
        blower: true,
        loTempAlarm: true,
        
        cooler: false,
        hiTempAlarm: false,
    },
    hw.getState()
 }
```
