# credo - A personal belief management framework

## Motivation

`credo` is meant to set a standard for what it means to have a "belief".  `credo` is a cognitive tool to allow people to evaluate and develop their own core value system. `credo` is a rigorous practice rooted in decades of process automation research that will challenge you to set a higher bar for what it is you hold to be true.


### Core Principles 

`credo` is a cognitive framwork based in Agile software development practices that can be used to document, validate, and modify beliefs over time.
It is intended as a mechanism for "getting to the truth" of a situation rather than as a way to "be right".  

The fundamental assumptions of `credo` are:

- In order for something to be a fact, there must be evidence to support it.
- People's beliefs should be respected even when we disagree with them.
- You might be wrong.

## Framework

At the highest level `credo` recognizes two concepts:

1. `topic`
2. `belief`

A `topic` is a high level description, or tag, that may be associated with a belief.  A single topic may have many beliefs.

`credo` defines between three classes of belief: 

1. `feeling`
2. `opinion`
3. `stance`


All beliefs require the following characteristics

- A topic
- A belief type
- A title
- A summary

### `feeling`

A feeling is the rawest form of a belief. Feelings will be part of a persons value system, but will lack ready evidence to support it.
.
A feeling has the following characteristics:

- 3 associated caveats


### `opinion`

Opinions are a refined class of belief.  They are different from a feeling in that there are sources that one can cite to support the opinion.

In the context of `credo`, a valid opinion must contain:

- Three independent sources supporting the belief (digital copies that can be added to source)

### `stance`

A stance is the most developed form of belief, and also has the highest standard of qualification.

A stance has the following requirements:

- Three independent sources supporting the belief (digital copies that can be added to source)
- Three independent sources opposing the belief (digital copies that can be added to source)
- A summary of each source supporting the belief.
- A summary of each source opposing the belief.
- A synthesis of the supporting and opposing evidence that forms the basis of the `stance`

## Examples

```
- topic: Immigration
  belief: feeling
  title: Immigration is a net positive for the United States
  summary: I believe diversity is good for communities, work environments, and for countries as a whole. Diversity fosters differences of thought, introduces new ideas, and requires people to challenge their preconeptions.  Immigration is a fundamental mechanism of national diversification, and because of it should be encouraged and responsibly managed
  caveats:
    - I'm referring to legal immigration
    - I don't really know about the epirical effects of diversity on communities
    - Immigration and "diversity" are not necessarily equivalent. Indeed, the US is probably an excellent example of this.  There are definitely communities that experience lots of immigration but little actual diversity. 
  

- topic: Immigration
  belief: opinion
  title: The cost of enforcing aggresive deportation policies is greater than the total tax burded imposed by illegal immigrants.
  summary: John Oliver went through a lengthy breakdown of Donald trump's proposals to build a wall along the mexican border and demonstrated the proposal to be impractical, infeasible, and ineffectual.
  source:
    - Department of Homeland Security Deportation Budgets <pdf, link, dates>
    - John Oliver Episode Number, Season, Date of Air.
    - Study Referenced by John Oliver during Episode
 
```

## Usage

The `credo` framework itself is encapsulated in the examples and documentation provided. Implementations of `credo` may vary and evolve over time, but the initial usage is intended to be via version control.

Using version control to manage your `credo` has the following advantages:

- Open source and transparent
- Inherently flexible.  Beliefs change over time. Using the Pull request paradigm you can accept arguments for differing viewpoints on beliefs you hold. 
- Versionable
- Self documenting

Updates to your `credo` should be done using conventional changelog format and should be limited in scope to a single belief per pull request.


