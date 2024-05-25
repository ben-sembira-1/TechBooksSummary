# Chapter 9 - Unit Tests

## Random Points
1. Clean tests are as important if not more then production code. They are the real thing that makes code flexible and liable.
1. About TDD, is it always a good idea? Maybe.. But sometimes when a developer is not experienced enough it can be too hard to predict how the API will look like. In general, I agree - A lot because it makes developers create testable code, and because it can lower the amount of irelavnt code that developers add just for fun.
1. It is a good idea to seperate tests by concepts.
1. Minimize assertions per test.
1. Tests can lack where production code can't - In efficency (As long as the tests stay fast to run).

## Rules
1. F.I.R.S.T
    1. Fast
    1. Independent (Nice reason - Helps diagnosis When something failes)
    1. Repeatable
    1. Self-Validating
    1. Timely (Contraversial?)

## Contraversial Points
1. He gave an example of tests that does multiple assertions. I do not like the shortcuts he did. [alternative](#appendix-a---short-assertions)

## Overall Summary
Tests are important. Very important. And we should treat them as production code.
The F.I.R.S.T acronym is a pretty good summary to remember.

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
