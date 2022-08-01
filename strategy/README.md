Strategy (Policy) Pattern
- algorithm vary independent from clients that use it

Steps:
1. defines family of algorithms
2. encapsulate each one
3. make them interchangeable

Use Cases:
1. many related classes differ only in behavior
2. different variants of algorithm
3. algorithm uses data clients shouldn't know about
4. cod has too many conditionals

Mermaid Class Diagram:
classDiagram
Context o--> Strategy
Context: ContextInterface()
Strategy: AlgorithmInterface()
Strategy <|-- ConcreteStrategyA
Strategy <|-- ConcreteStrategyB
Strategy <|-- ConcreteStrategyC

Benefits:
1. families of related algorithms
2. alternative to subclassing)
3. strategies eliminate conditionals
4. choice of implementaion

Drawbacks:
1. clients need to be aware of diff strategies
2. communication overhead between Strategy & Context
3. increased number of objects